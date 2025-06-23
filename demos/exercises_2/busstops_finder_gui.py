import requests
import streamlit as st
from streamlit_folium import st_folium
import folium


class VBBTransportAPI:
    BASE_URL = "https://v6.vbb.transport.rest"

    def __init__(self):
        self.session = requests.Session()

    def _get(self, endpoint: str, params: dict = None) -> dict | list:
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def search_locations(self, query: str, limit: int = 10) -> list[dict]:
        return [
            loc for loc in self._get("/locations", {"query": query, "results": limit})
            if loc.get("type") == "stop"
        ]

    def get_departures(self, stop_id: str, limit: int = 5) -> list[dict]:
        return self._get(f"/stops/{stop_id}/departures", {"results": limit})

    def get_journey(self, from_id: str, to_id: str) -> dict:
        return self._get("/journeys", {"from": from_id, "to": to_id})


# --- Streamlit GUI ---

st.set_page_config(page_title="🚌 VBB Berlin - Journey Planner", layout="centered")
st.title("🚌 VBB Berlin - Journey Planner & Departures")

api = VBBTransportAPI()

with st.form("search_form"):
    col1, col2 = st.columns(2)
    with col1:
        from_query = st.text_input("From:", "Alexanderplatz")
    with col2:
        to_query = st.text_input("To:", "Potsdamer Platz")

    submitted = st.form_submit_button("Plan Journey")

if submitted:
    from_stops = api.search_locations(from_query)
    to_stops = api.search_locations(to_query)

    if not from_stops or not to_stops:
        st.error("No matching stops found for one or both locations.")
    else:
        from_stop = from_stops[0]
        to_stop = to_stops[0]

        st.session_state["journey_data"] = api.get_journey(from_stop["id"], to_stop["id"])
        st.session_state["from_stop"] = from_stop
        st.session_state["to_stop"] = to_stop

# Display journey if data exists
if "journey_data" in st.session_state:
    journey_data = st.session_state["journey_data"]
    from_stop = st.session_state["from_stop"]
    to_stop = st.session_state["to_stop"]

    if "journeys" in journey_data and journey_data["journeys"]:
        journey = journey_data["journeys"][0]
        legs = journey.get("legs", [])

        st.subheader("🛣 Journey Overview")
        for leg in legs:
            mode = leg.get("mode", "walk")
            icon = "🚶"
            if mode == "train":
                icon = "🚆"
            elif mode == "subway":
                icon = "🚇"
            elif mode == "tram":
                icon = "🚋"
            elif mode == "bus":
                icon = "🚌"

            line = leg.get("line", {}).get("name", "")
            departure = leg.get("departure", "N/A")
            arrival = leg.get("arrival", "N/A")
            origin = leg.get("origin", {}).get("name", "")
            destination = leg.get("destination", {}).get("name", "")
            direction = leg.get("direction", "")

            st.markdown(
                f"{icon} **{mode.upper()} {line}** → {direction}  \n"
                f"From `{origin}` at **{departure}** → To `{destination}` at **{arrival}**"
            )

        # Map
        st.subheader("🗺 Map of Journey")
        start_coords = [
            from_stop["location"]["latitude"],
            from_stop["location"]["longitude"],
        ]
        journey_map = folium.Map(location=start_coords, zoom_start=13)

        for leg in legs:
            orig = leg.get("origin", {})
            dest = leg.get("destination", {})
            if all(k in orig for k in ["latitude", "longitude"]) and all(k in dest for k in ["latitude", "longitude"]):
                orig_coords = [orig["latitude"], orig["longitude"]]
                dest_coords = [dest["latitude"], dest["longitude"]]
                folium.Marker(orig_coords, tooltip=orig.get("name")).add_to(journey_map)
                folium.Marker(dest_coords, tooltip=dest.get("name")).add_to(journey_map)
                folium.PolyLine(locations=[orig_coords, dest_coords], color="blue").add_to(journey_map)

        st_folium(journey_map, width=700, height=450)
    else:
        st.warning("No journey data available.")

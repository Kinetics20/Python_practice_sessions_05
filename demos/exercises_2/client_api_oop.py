import requests


class Location:
    def __init__(self, id: str, name: str, type: str, latitude: float, longitude: float):
        self.id = id
        self.name = name
        self.type = type
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self) -> str:
        return f"<Location name='{self.name}', type='{self.type}', lat={self.latitude}, lon={self.longitude}>"


class Departure:
    def __init__(self, line: str, direction: str, when: str):
        self.line = line
        self.direction = direction
        self.when = when

    def __repr__(self) -> str:
        return f"<Departure {self.line} to {self.direction} at {self.when}>"


class JourneyLeg:
    def __init__(self, origin: str, destination: str, departure: str, arrival: str, mode: str):
        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.mode = mode

    def __repr__(self) -> str:
        return f"<JourneyLeg {self.mode}: {self.origin} → {self.destination} ({self.departure} → {self.arrival})>"


class VBBTransportAPI:
    BASE_URL = "https://v6.vbb.transport.rest"

    def __init__(self):
        self.session = requests.Session()

    def _get(self, endpoint: str, params: dict = None) -> dict | list:
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def search_locations(self, query: str, limit: int = 5) -> list[Location]:
        data = self._get("/locations", {"query": query, "results": limit})
        return [
            Location(
                id=item.get("id", ""),
                name=item.get("name", "Unknown"),
                type=item.get("type", "unknown"),
                latitude=item.get("latitude", 0.0),
                longitude=item.get("longitude", 0.0),
            )
            for item in data if "latitude" in item and "longitude" in item
        ]

    def get_departures(self, station_id: str, limit: int = 5) -> list[Departure]:
        data = self._get("/stops/" + station_id + "/departures", {"results": limit})
        return [
            Departure(
                line=item.get("line", {}).get("name", "N/A"),
                direction=item.get("direction", "Unknown"),
                when=item.get("when", "Unknown")
            )
            for item in data
        ]

    def plan_journey(self, from_location: str, to_location: str) -> list[JourneyLeg]:
        data = self._get("/journeys", {"from": from_location, "to": to_location})
        journey_legs = []
        for journey in data.get("journeys", []):
            for leg in journey.get("legs", []):
                journey_legs.append(JourneyLeg(
                    origin=leg.get("origin", {}).get("name", "Unknown"),
                    destination=leg.get("destination", {}).get("name", "Unknown"),
                    departure=leg.get("departure", "Unknown"),
                    arrival=leg.get("arrival", "Unknown"),
                    mode=leg.get("mode", "unknown")
                ))
        return journey_legs

if __name__ == "__main__":
    api = VBBTransportAPI()

    print("📍 Searching for: Hauptbahnhof")
    locations = api.search_locations("Hauptbahnhof")
    for loc in locations:
        print("➡️", loc)

    if locations:
        loc_id = locations[0].id
        print(f"\n🚌 Departures from {locations[0].name}:")
        departures = api.get_departures(loc_id)
        for d in departures:
            print("  -", d)

        print("\n🧭 Journey from Hauptbahnhof to Alexanderplatz:")
        journey = api.plan_journey("Hauptbahnhof", "Alexanderplatz")
        for leg in journey:
            print("  -", leg)

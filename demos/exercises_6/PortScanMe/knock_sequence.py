import socket
import time

HOST = 'py10-portscan.ctf-hackarcana.net'
ports = {
    0: 31234,
    1: 31888,
    2: 31111,
    3: 31999
}
PASSWORD = b"LetMeIn"
TIMEOUT = 2

def knock_sequence():
    for ordinal in range(4):
        port = ports[ordinal]
        print(f"[↪️ ] Connecting to port {port} (ordinal {ordinal})...")
        try:
            with socket.create_connection((HOST, port), timeout=TIMEOUT) as s:
                s.sendall(PASSWORD)
                data = s.recv(2048)
                print(f"[✅] Got response: {data.decode(errors='ignore').strip()}")
        except Exception as e:
            print(f"[❌] Failed at ordinal {ordinal} on port {port}: {e}")
        time.sleep(0.5)  # mała przerwa między knockami

if __name__ == "__main__":
    knock_sequence()

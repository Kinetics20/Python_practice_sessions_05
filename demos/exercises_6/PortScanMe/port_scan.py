import socket

HOST = 'py10-portscan.ctf-hackarcana.net'
PORT_RANGE = range(31000, 32000)
TIMEOUT = 1
PASSWORD = b"LetMeIn"

def scan():
    open_ports = []

    for port in PORT_RANGE:
        try:
            with socket.create_connection((HOST, port), timeout=TIMEOUT) as s:
                s.sendall(PASSWORD)
                data = s.recv(1024)
                if data:
                    print(f"[+] Port {port} responded with: {data.decode(errors='ignore')}")
                    open_ports.append((port, data.decode(errors='ignore').strip()))
        except:
            continue

    print("\n[✅] Open ports and responses:")
    for port, response in open_ports:
        print(f"Port: {port} -> Response: {response}")

if __name__ == "__main__":
    scan()

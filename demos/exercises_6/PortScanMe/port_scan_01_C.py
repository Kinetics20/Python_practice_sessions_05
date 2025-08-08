import socket
from concurrent.futures import ThreadPoolExecutor
import time
from itertools import permutations


def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return port if result == 0 else None
    except:
        return None


def find_open_ports(host, start_port=31000, end_port=31999):
    print(f"Scanning ports {start_port}-{end_port} on {host}...")
    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, host, port): port for port in range(start_port, end_port + 1)}

        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)
                print(f"Found open port: {result}")

    return sorted(open_ports)


def connect_and_send(host, port, timeout=3):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))

        sock.sendall(b"LetMeIn")
        response = sock.recv(1024)
        sock.close()

        return response.decode('utf-8', errors='ignore').strip()
    except Exception as e:
        return f"ERROR: {e}"


def try_sequence(host, port_sequence):
    print(f"\nTrying sequence: {port_sequence}")

    responses = []

    for i, port in enumerate(port_sequence):
        print(f"Step {i}: Connecting to port {port}...")

        response = connect_and_send(host, port, timeout=5)
        responses.append(response)

        print(f"  Response: '{response}'")

        if "flag" in response.lower() or "Good work" in response:
            print(f"🚩 FLAG FOUND: {response}")
            return True

        if "wrong order" in response:
            print(f"❌ Wrong order at step {i}")
            return False

        if response == str(i):
            print(f"✅ Correct step {i}")
            continue
        else:
            print(f"❌ Unexpected response at step {i}: '{response}'")

        time.sleep(0.2)

    return False


def find_correct_sequence(host, open_ports):
    print(f"\n🔍 Testing all possible sequences of {len(open_ports)} ports...")

    known_first = 31403
    other_ports = [p for p in open_ports if p != known_first]

    print(f"Known first port (ordinal 0): {known_first}")
    print(f"Other ports to arrange: {other_ports}")

    for perm in permutations(other_ports):
        sequence = [known_first] + list(perm)

        if try_sequence(host, sequence):
            print(f"🎉 Success with sequence: {sequence}")
            return sequence

        time.sleep(0.5)

    print("❌ No successful sequence found")
    return None


def solve_challenge_v2():
    host = "py10-portscan.ctf-hackarcana.net"

    print(f"🎯 Starting port knocking challenge on {host}")

    open_ports = [31024, 31337, 31403, 31999]
    print(f"Using known open ports: {open_ports}")

    correct_sequence = find_correct_sequence(host, open_ports)

    if correct_sequence:
        print(f"\n✅ Found correct sequence: {correct_sequence}")
        print("🎉 Challenge completed!")
    else:
        print("\n❌ Could not find correct sequence")

        print("\nTrying educated guesses...")

        educated_guesses = [
            [31403, 31024, 31337, 31999],
            [31403, 31024, 31999, 31337],
            [31403, 31337, 31024, 31999],
            [31403, 31337, 31999, 31024],
            [31403, 31999, 31024, 31337],
            [31403, 31999, 31337, 31024],
        ]

        for guess in educated_guesses:
            print(f"\nTrying educated guess: {guess}")
            if try_sequence(host, guess):
                print(f"🎉 Success with educated guess: {guess}")
                break
            time.sleep(1)


if __name__ == "__main__":
    solve_challenge_v2()

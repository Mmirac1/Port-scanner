import socket
import threading

def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target_ip, port))
        print(f"Port {port} is open")
        open_ports.append(port)
    except:
        pass
    finally:
        sock.close()

def scan_target(target_ip, start_port, end_port):
    global open_ports
    open_ports = []
    print(f"Scanning target {target_ip}...")
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        thread.start()

    return open_ports
    
if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    open_ports = scan_target(target_ip, start_port, end_port)
    print(f"The ports from {start_port} to {end_port} have been scanned.")
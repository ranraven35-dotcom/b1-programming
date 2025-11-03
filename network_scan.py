devices = [
    ("192.168.1.10", [22, 80, 443]),
    ("192.168.1.11", [21, 22, 80]),
    ("192.168.1.12", [23, 80, 3389])
]

risky_ports = [21, 23, 3389]

print("Scanning network devices...")
risk_count = 0

for ip, open_ports in devices:
    for port in open_ports:
        for risky_port in risky_ports:
            if port == risky_port:
                print("WARNING: " + ip + " has risky port " + str(port) + " open")
                risk_count = risk_count + 1

print("Scan complete: " + str(risk_count) + " security risks found")

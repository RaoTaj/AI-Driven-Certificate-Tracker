import ssl
import socket
from datetime import datetime
import pandas as pd

def fetch_certificates(hosts, port=443):
    results = []
    for host in hosts:
        try:
            context = ssl.create_default_context()
            conn = context.wrap_socket(socket.socket(), server_hostname=host)
            conn.settimeout(3)
            conn.connect((host, port))
            cert = conn.getpeercert()
            conn.close()

            expiry_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
            days_left = (expiry_date - datetime.utcnow()).days

            status = "Healthy"
            if days_left < 30:
                status = "Warning"
            if days_left < 7:
                status = "Critical"

            results.append({
                "Host": host,
                "ExpiryDate": expiry_date,
                "DaysLeft": days_left,
                "Issuer": dict(x[0] for x in cert['issuer']).get('organizationName', 'Unknown'),
                "Status": status
            })

        except Exception as e:
            results.append({
                "Host": host,
                "Error": str(e),
                "Status": "Unreachable"
            })
    return results


if __name__ == "__main__":
    hosts = ["google.com", "yahoo.com", "expired.badssl.com"]
    data = fetch_certificates(hosts)
    df = pd.DataFrame(data)
    df.to_csv("cert_logs.csv", index=False)
    print("✅ Certificate logs saved to cert_logs.csv")

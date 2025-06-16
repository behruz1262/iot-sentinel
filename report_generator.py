import qrcode
import json
from datetime import datetime

def generate_report(device_data, filename="iot_privacy_report.json"):
    with open(filename, "w") as f:
        json.dump(device_data, f, indent=4)
    print(f"📄 Report saved as {filename}")

    img = qrcode.make(f"https://yourwebsite.com/reports/{filename}")
    img.save("report_qr.png")
    print("🔗 QR code saved as report_qr.png")
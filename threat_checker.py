import requests

def check_ip_threat(ip):
    url = f"https://threatfox.abuse.ch/api/v1/"
    data = {
        "query": "search_ioc",
        "search_term": ip
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200 and "data" in response.json():
            print(f"⚠️ {ip} found in threat intelligence database!")
            return True
    except Exception as e:
        print(f"Error checking threat for {ip}: {e}")
    return False
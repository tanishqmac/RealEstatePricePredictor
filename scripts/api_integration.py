try:
    import requests
except ModuleNotFoundError:
    print("Module 'requests' not found. Please install it using: pip install requests")

def fetch_real_time_data():
    # Sample API endpoint for real estate data
    api_endpoint = "https://api.sampleapis.com/real-estate/properties"
    try:
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch real-time data. Status Code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching real-time data:", e)
        return None
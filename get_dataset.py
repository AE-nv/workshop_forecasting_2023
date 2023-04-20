import requests

garage_data = requests.get("https://data.stad.gent/api/records/1.0/search/?dataset=bezetting-parkeergarages-real-time")

if garage_data.status_code == 200:
    j = garage_data.json()
    relevant_info = [{key: record["fields"].get(key) for key in ['name', 'availablecapacity']} for record in j.get("records")]
    print(relevant_info)

import requests
from bs4 import BeautifulSoup
import json

def save_json(data):
    with open("zones.json", "w") as json_file:
        # Append info to the JSON file
        json.dump(data, json_file, indent=4)
    print('Data has been saved to zones.json')

def main():
    URL = 'https://algona.municipal.codes'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        zones = []

        # Get the page of zones
        soup = BeautifulSoup(response.content, 'html.parser')
        zones_link_el = soup.find('span', string='22').find_previous('a')
        zone_link = URL + zones_link_el['href']

        # Find each link in the zones page and add to a list
        response2 = requests.get(zone_link, headers=headers)
        soup2 = BeautifulSoup(response2.content, 'html.parser')
        zones_links_el = soup2.find_all('li', class_='tocItem level4')
        zones_links = []
        for item in zones_links_el:
            for link in item.find_all('a'):
                zones_links.append(URL + "/Code/" + link['href'])

        # Iterate through each zone link and get the data
        for link in zones_links:
            request = requests.get(link, headers=headers)
            soup = BeautifulSoup(request.content, 'html.parser')

            title = soup.find('span', class_="name").getText(strip=True)
            description = soup.find('p').getText(strip=True)

            zone_info = {
                "title": title,
                "description": description,
            }
            zones.append(zone_info)
        save_json(zones)


if __name__ == "__main__":
    main()

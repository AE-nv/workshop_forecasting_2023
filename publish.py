import json
import time
import pika
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://data.stad.gent/explore/dataset/bezetting-parkeergarages-real-time/table/'
SCRAPE_INTERVAL_SECONDS = 300

options = webdriver.ChromeOptions()
options.add_argument('--headless')

while True:
    # get parking data
    browser = webdriver.Chrome(options=options)
    browser.get(URL)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('tr', {'class': 'odswidget-table__internal-table-row'})

    # parse data
    parking_info = []

    for parking in results:
        elements = parking.findChildren('span')
        parking_info.append({'name': elements[0].text, 'total': elements[2].text, 'available': elements[3].text})

    print(f"Got parking information for {len(parking_info)} parkings at {datetime.now()}")

    # push to rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters('20.107.148.34', credentials=pika.PlainCredentials('default_user_fczmvlFMM1tA80pB_5J', '9X-7yuoGOocaXY0yJvbM86YOeDqukj6x')))
    channel = connection.channel()
    channel.queue_declare(queue='ghent_parking_occupancy')
    channel.basic_publish(exchange='',
                        routing_key='ghent_parking_occupancy',
                        body=json.dumps(parking_info))
    connection.close()

    browser.close()

    print(f'Waiting {SCRAPE_INTERVAL_SECONDS} seconds to scrape again')
    time.sleep(SCRAPE_INTERVAL_SECONDS)
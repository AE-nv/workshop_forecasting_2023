import json
import pika
from datetime import datetime
from prometheus_client import CollectorRegistry, push_to_gateway, Gauge

# # define prometheus metric
registry = CollectorRegistry()
g = Gauge('parking_spaces_test', 'Available parking spaces', registry=registry, labelnames=['parking'])


# # define what to do with message
def callback(ch, method, properties, body):
    print(f"Received a message at {datetime.now()}")
    parking = json.loads(body)
    print(parking)

    # for parking in body:
    #     print(parking)
    #     available = int(parking['availablecapacity'])
    #     g.labels(parking['name']).set(available)

    available = int(parking['availablecapacity'])
    g.labels(parking['name']).set(available)

    # push to prometheus
    push_to_gateway('40.127.226.4:9091', job=parking["group_no"], registry=registry)
    print(f"Pushed metrics for {len(body)} parkings to prometheus for group {parking['group_no']}")

    # acknowledge message in rabbitmq
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print(f"Acknowledged message at {datetime.now()}")


# # set up connection to queue
with pika.BlockingConnection(pika.ConnectionParameters(
        '20.82.209.144',
        credentials=pika.PlainCredentials(
            'ceneka',
            'ceneka_data_23'))
) as conn:
    channel = conn.channel()
    channel.queue_declare(queue='ghent_parking_occupancy_test')

    channel.basic_consume(queue='ghent_parking_occupancy_test', on_message_callback=callback)
    channel.start_consuming()

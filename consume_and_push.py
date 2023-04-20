import json
import pika
from datetime import datetime
from prometheus_client import CollectorRegistry, push_to_gateway, Gauge

# GROUP_NUMBER = "1"
#
# # define prometheus metric
# registry = CollectorRegistry()
# g = Gauge('parking_spaces', 'Available parking spaces', registry=registry, labelnames=['parking'])
#
# # set up connection to queue
connection = pika.BlockingConnection(pika.ConnectionParameters('20.107.148.34', credentials=pika.PlainCredentials('default_user_fczmvlFMM1tA80pB_5J', '9X-7yuoGOocaXY0yJvbM86YOeDqukj6x')))
channel = connection.channel()
channel.queue_declare(queue='ghent_parking_occupancy')

# # define what to do with message
def callback(ch, method, properties, body):
    print(f"Received a message at {datetime.now()}")
    body = json.loads(body)

    for parking in body:
        print(parking)
        #available = int(parking['available'].replace(',',''))
        #g.labels(parking['name']).set(available)

    # push to prometheus
    #push_to_gateway('20.67.210.98:9091', job=GROUP_NUMBER, registry=registry)
    print(f"Pushed metrics for {len(body)} parkings to prometheus")

    # acknowledge message in rabbitmq
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print(f"Acknowledged message at {datetime.now()}")

# consume messages
channel.basic_consume(queue='ghent_parking_occupancy', on_message_callback=callback)
channel.start_consuming()

# registry = CollectorRegistry()
# g = Gauge('test_gauge2', 'Testing gauges', registry=registry, labelnames=['test'])

# for i in range(1, 101):
#     print(i)
#     g.labels("shana").set(i)
#     g.labels("thibauld").set(i + 1)
#     push_to_gateway('20.223.97.131:9091', job="1", registry=registry)

# g.labels("thibauld").set(10)
# push_to_gateway('20.223.97.131:9091', job="1", registry=registry)


#test_gauge{test="thibauld"}
#test_gauge
#parse "prometheus-server": invalid URI for request in Grafana
# Consume message from Q called "Worker_queue" and print it

import pika
import time

# Connect to local rabbitmq server
credentials = pika.PlainCredentials('user', 'password')
config = pika.ConnectionParameters('localhost', 5672, 'vhost', credentials)
connection = pika.BlockingConnection(config)

# channel, exchange and queue
channel = connection.channel()

# Callback function
def callback(ch, method, properties, body):
    print(f" [x] Received {body} in Worker 1")
    # sleep for 5 seconds
    time.sleep(5)

    # Acknowledge message
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Consume message
channel.basic_consume(queue='worker_queue', on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
## All messages from the q 'bad' will be logged to the file 'bad.log'
## All messages from the q 'not_bad' will be logged to the file 'not_bad.log'

import pika
import logging

# URL to connect to RabbitMQ
RABBITMQ_URL = "amqp://user:password@localhost:5672/vhost"

# Open up files in append mode
bad_log = open("bad.log", "a")
not_bad_log = open("not_bad.log", "a")

# Create a connection to RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
channel = connection.channel()

# consume messages from the queue 'bad'
def callback(ch, method, properties, body):
    bad_log.write(body.decode() + "\n")
    # Acknowledge the message
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='bad', on_message_callback=callback)

# consume messages from the queue 'not_bad'
def callback(ch, method, properties, body):
    not_bad_log.write(body.decode() + "\n")
    # Acknowledge the message
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='not_bad', on_message_callback=callback)

# Start consuming messages
channel.start_consuming()
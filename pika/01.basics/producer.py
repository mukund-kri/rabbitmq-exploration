## a basic producer in pika

import pika

# Connect to RabbitMQ
# Credentials
creds = pika.PlainCredentials('user', 'password')
params = pika.ConnectionParameters('localhost', 5672, 'vhost', creds)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Create queue test if it doesn't exist
channel.queue_declare(queue='test', durable=True)

# Publish a message
channel.basic_publish(exchange='',
                      routing_key='test',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))

print(" [x] Sent 'Hello World!'")
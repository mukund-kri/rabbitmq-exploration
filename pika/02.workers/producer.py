## Produce ten messages to the topic. This to test worker consumers.
import pika

numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']

# Connect to local rabbitmq server
credentials = pika.PlainCredentials('user', 'password')
config = pika.ConnectionParameters('localhost', 5672, 'vhost', credentials)
connection = pika.BlockingConnection(config)

# channel, exchange and queue
channel = connection.channel()

# Publish messages
for number in numbers:
    channel.basic_publish(exchange='worker_exchange', routing_key='worker_key', body=number)
    print(f" [x] Sent {number}")

# Clean up
connection.close()
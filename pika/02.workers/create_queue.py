# Create durable exchange and queue and binding.
import pika

# Connect to local rabbitmq server
credentials = pika.PlainCredentials('user', 'password')
config = pika.ConnectionParameters('localhost', 5672, 'vhost', credentials)
connection = pika.BlockingConnection(config)

# channel, exchange and queue
channel = connection.channel()

# Create exchange
channel.exchange_declare(exchange='worker_exchange', exchange_type='direct', durable=True)

# Create queue
channel.queue_declare(queue='worker_queue', durable=True)

# Bind exchange and queue
channel.queue_bind(exchange='worker_exchange', queue='worker_queue', routing_key='worker_key')

connection.close()
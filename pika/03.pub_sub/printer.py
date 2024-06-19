## Consumer 1, print the message to the console

import pika

# Connect to RabbitMQ server
credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, 'vhost', credentials))
channel = connection.channel()

# create a non-durable queue with a random name and bind to an exchange called 'logs'
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

# Define a callback function to print the message to the console
def callback(ch, method, properties, body):
    print(f"   [x] Received {body}")

# Set up the consumer to consume messages from the queue
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

# Start consuming messages
channel.start_consuming()
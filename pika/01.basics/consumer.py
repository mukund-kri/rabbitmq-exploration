import pika


# Connect to RabbitMQ
# Credentials
creds = pika.PlainCredentials('user', 'password')
params = pika.ConnectionParameters('localhost', 5672, 'vhost', creds)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Create queue test if it doesn't exist
channel.queue_declare(queue='test', durable=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

for method_frame, properties, body in channel.consume('test'):
    print(method_frame, properties, body)
    channel.basic_ack(method_frame.delivery_tag)

requeued_messages = channel.cancel()
connection.close()

import pika

numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']


# Connect to RabbitMQ server
credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, 'vhost', credentials))
channel = connection.channel()

# Publish messages to the exchange
for number in numbers:
    channel.basic_publish(exchange='logs', routing_key='', body=number)
    print(f" [x] Sent {number}")

# Now close the connection
connection.close()
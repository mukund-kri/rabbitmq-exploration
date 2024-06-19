## Create the exchange for this example. Make it durable. Only the queue will be non-durable.


import pika

# Connect to RabbitMQ server
credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, 'vhost', credentials))
channel = connection.channel()

# Create the exchange for this example. Make it durable. 
channel.exchange_declare(exchange='logs', exchange_type='fanout', durable=True)

# Now close the connection
connection.close()
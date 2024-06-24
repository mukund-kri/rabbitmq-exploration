## Create a exchange called "routing_example"


import pika

# URL to connect to RabbitMQ
RABBITMQ_URL = "amqp://user:password@localhost:5672/vhost"

# Create a connection to RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))

# Create the exchange
channel = connection.channel()
channel.exchange_declare(exchange='routing_example', exchange_type='direct')

# Declare the queues 'bad' and 'not_bad'
channel.queue_declare(queue='bad')
channel.queue_declare(queue='not_bad')

# Bind the queues to the exchange
channel.queue_bind(exchange='routing_example', queue='not_bad', routing_key='log.debug')
channel.queue_bind(exchange='routing_example', queue='not_bad', routing_key='log.info')
channel.queue_bind(exchange='routing_example', queue='bad', routing_key='log.warning')
channel.queue_bind(exchange='routing_example', queue='bad', routing_key='log.error')

# Close the connection
connection.close()

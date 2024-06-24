## A rabbitmq consumer with SelectConnection

import pika

# What to do when a message is received
def on_message(channel, method, header, body):
    print(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)

# What to do when a channel is opened
def on_open_channel(channel):
    # register the callback when a message is received
    print('Channel opened')
    channel.basic_consume('async_queue', on_message)

# What to do when a connection is opened
def on_open(connection):
    print('Connection opened')
    connection.channel(on_open_channel)

# Connection parameters
params = pika.ConnectionParameters('amqp://user:password@localhost/vhost')
connection = pika.SelectConnection(params, on_open)
print('Connected to RabbitMQ')

try:
    print('Starting ioloop')
    connection.ioloop.start()
    print('Connection closed')
except KeyboardInterrupt as e:
    print(e)
    connection.close()
    connection.ioloop.start()
except Exception as e:
    print(e)
    #connection.close()
    connection.ioloop.start()

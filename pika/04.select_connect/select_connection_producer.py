import pika

def on_channel_open_error(channel, error_message):
    print('Channel Open Failed: ' + error_message)
    #connection.ioloop.stop()
    exit(1)

# Step #3
def on_open(connection):
    print('Connection Opened')
    connection.channel(on_open_callback=on_channel_open, on_open_error_callback=on_channel_open_error)

def on_open_error(connection, error_message):
    print('Connection Open Failed: ' + error_message)
    #connection.ioloop.stop()
    exit(1)

# Step #4
def on_channel_open(channel):
    print('Channel Opened')
    channel.basic_publish('async_exchange',
                            'test_routing_key',
                            'message body value',
                            pika.BasicProperties(content_type='text/plain',
                                                 delivery_mode=pika.DeliveryMode.Transient))

    connection.close()

# Step #1: Connect to RabbitMQ
parameters = pika.URLParameters('amqp://user:password@localhost:5672/vhost')

connection = pika.SelectConnection(parameters=parameters,
                                   on_open_callback=on_open,
                                   on_open_error_callback=on_open_error,)
print('Connecting to RabbitMQ')
print(connection.is_open)

try:

    print('Starting IOLoop')
    # Step #2 - Block on the IOLoop
    connection.ioloop.start()

# Catch a Keyboard Interrupt to make sure that the connection is closed cleanly
except KeyboardInterrupt:

    # Gracefully close the connection
    connection.close()

    # Start the IOLoop again so Pika can communicate, it will stop on its own when the connection is closed
    connection.ioloop.start()
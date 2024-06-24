## Generate a whole bunch of messages

import pika


# URL to connect to RabbitMQ
RABBITMQ_URL = "amqp://user:password@localhost:5672/vhost"

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
log_levels = ["log.debug", "log.info", "log.warning", "log.error"]

# Create a connection to RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
channel = connection.channel()

# Publish messages to the exchange 'routing_example'
for number in numbers:
    for log_level in log_levels:
        body = "Message: {number} Log Level: {log_level}".format(number=number, log_level=log_level)
        channel.basic_publish(exchange='routing_example', routing_key=log_level, body=body)

# Close the connection
connection.close()
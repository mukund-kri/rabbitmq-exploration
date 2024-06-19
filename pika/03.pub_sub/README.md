# Publish-Subscribe exchanges

## Aim

To demo the publish-subscribe exchanges in RabbitMQ.

## Description

We will create a simple publish-subscribe system using RabbitMQ. It will consist of ...

1. A producer that sends messages to an exchange.
2. A consumer that will print messages to the console.
3. A consumer that will log the messages to a file.

Notes:

- The consumer will create temporary queues and bind them to the exchange. 
- No name is given to the queue, so RabbitMQ will generate a random name.
- The queue is deleted when the consumer connection is closed.
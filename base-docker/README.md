# Base RabbitMQ image

This code  shows how to create a RabbitMQ development image with the management plugin
enabled.

## Notes

- In `docker-compose.yml` file look at the rabbitmq service definition.
- The `RABBITMQ_DEFAULT_USER` and `RABBITMQ_DEFAULT_PASS` environment variables are used to set the default user and password.
- The `RABBITMQ_DEFAULT_VHOST` environment variable is used to set the default virtual host.
- port 5672 is exposed for AMQP traffic.
- port 15672 is exposed for the management plugin.

That's it! simple.
# Pika in Async mode

Setting up a connection to RabbitMQ in async mode is a bit more complex than in sync 
mode. The following example shows how to use the `SelectConnection` class to connect
to RabbitMQ in async mode.


## Status

I have failed to get this to work, and I don't understand why.

- The example code from the Pika documentation works. But it's long winded and wraped
    in a class.
- My attempts to write it from first principles have failed. I don't understand why.

## What now?

Abandon this for now. Focus on aio-pica library for now.

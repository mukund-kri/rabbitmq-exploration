# Routing

## Overview

The exchanges can "route" messages to queues based on the message routing key.

The routes are specified by the binding between the exchange and the queue.

Key concepts:

1. Routing Keys
2. Bindings

## Code

1. create.py :: Create the exchange.
2. producer.py :: Publish messages to the exchange.
3. consumer.py :: Create temporary queue and bind it to the exchange.
                  These binding are the routing rules.
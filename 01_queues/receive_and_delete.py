# Author: Apache X692
# Created on: 08/01/2025
#
# receive_and_delete.py

from azure.servicebus import ServiceBusClient


def receive_message(connection_string, queue_name):
    servicebus_client = ServiceBusClient.from_connection_string(connection_string)
    receiver = servicebus_client.get_queue_receiver(queue_name)

    with receiver:
        for message in receiver:
            print(f"Received: {message}")
            receiver.complete_message(message)

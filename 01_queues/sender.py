# Author: Apache X692
# Created on: 08/01/2025
#
# sender.py
from azure.servicebus import ServiceBusClient, ServiceBusMessage


def send_message(connection_string, queue_name, message_body):
    servicebus_client = ServiceBusClient.from_connection_string(connection_string)
    sender = servicebus_client.get_queue_sender(queue_name)

    with sender:
        message = ServiceBusMessage(message_body)
        sender.send_messages(message)
        print(f"Sent: {message_body}")

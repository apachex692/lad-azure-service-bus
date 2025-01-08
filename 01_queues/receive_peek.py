from azure.servicebus import ServiceBusClient


def peek_and_remove_messages(connection_string, queue_name):
    servicebus_client = ServiceBusClient.from_connection_string(connection_string)
    receiver = servicebus_client.get_queue_receiver(queue_name)

    with receiver:
        messages = receiver.peek_messages(max_message_count=10)

        for message in messages:
            print(f"Peeked: {message}")
            receiver.complete_message(message)
            print(f"Removed: {message}")

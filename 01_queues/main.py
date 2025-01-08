# Author: Apache X692
# Created on: 08/01/2025
#
# main.py
from os import getenv

from dotenv import load_dotenv

import receive_and_delete
import receive_peek
import sender


def main():
    load_dotenv()

    connection_string = getenv("AZURE_SERVICE_BUS_CONNECTION_STRING")
    queue_name = getenv("AZURE_SERVICE_BUS_QUEUE_NAME")

    for index in range(10):
        sender.send_message(
            connection_string, queue_name, "{'id': %d}" % (index + 1)
        )

    receive_and_delete.receive_message(connection_string, queue_name)
    #receive_peek.peek_and_remove_messages(connection_string, queue_name)


if __name__ == "__main__":
    main()

from socket import *
import sqlite3 as sl

databaseCon = sl.connect("chatapp.db")


def create_account(message):
    return "create account"


def start_chat(message):
    return "start chat"


def send_message(message):
    return "send message"


def no_such_func(message):
    return "ERROR: function " + message + " not found"


def use_protocol(message):
    return {
        "CREATE_ACC": create_account,
        "START_CHAT": start_chat,
        "SEND_MSG": send_message,
    }.get(message, no_such_func)(message)


def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("", serverPort))
    print("The server is ready to receive")
    while True:
        # get message from user
        message, clientAddress = serverSocket.recvfrom(2048)
        # use protocol to decide what to do
        res = use_protocol(message.decode())
        serverSocket.sendto(res.encode(), clientAddress)


if __name__ == "__main__":
    main()

from helpers import *


def main():
    """
    Main function to handle bot interactions.
    """
    contacts = {}
    print(BotMessage.WELCOME)

    while True:
        user_input = input(BotMessage.ENTER_A_COMMAND)
        command, *args = parse_input(user_input)

        if command in [BotCommand.CLOSE, BotCommand.EXIT]:
            print(BotMessage.GOODBYE)
            break
        elif command == BotCommand.HELLO:
            print(BotMessage.HOW_CAN_I_HELP)
        elif command == BotCommand.ADD:
            print(add_contact(args, contacts))
        elif command == BotCommand.CHANGE:
            print(change_contact(args, contacts))
        elif command == BotCommand.PHONE:
            print(show_phone(args, contacts))
        elif command == BotCommand.ALL:
            print(show_all(contacts))
        else:
            print(Error.INVALID_COMMAND)

if __name__ == "__main__":
    main()
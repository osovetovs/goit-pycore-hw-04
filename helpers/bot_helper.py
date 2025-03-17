from helpers import *


def parse_input(user_input: str) -> tuple:
    """
    Parse the user input string into a command and its arguments.

    :param user_input: The input entered by the user.
    :return: A tuple containing the command and a list of arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: list, contacts: dict) -> str:
    """
    Add a new contact.

    :param args: List containing name and phone.
    :param contacts: Dictionary of contacts.
    :return: Confirmation or an error message.
    """
    if len(args) != 2:
        return Error.INVALID_COMMAND

    name, phone = args
    contacts[name] = phone
    return BotMessage.CONTACT_ADDED

def change_contact(args: list, contacts: dict) -> str:
    """
    Change an existing contact's phone number.

    :param args: List containing name and new phone.
    :param contacts: Dictionary of contacts.
    :return: Confirmation or an error message.
    """
    if len(args) != 2:
        return Error.INVALID_COMMAND

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return BotMessage.CONTACT_UPDATED
    else:
        return BotMessage.CONTACT_NOT_FOUND

def show_phone(args: list, contacts: dict) -> str:
    """
    Show a contact's phone number.

    :param args: List containing the contact's name.
    :param contacts: Dictionary of contacts.
    :return: Contact's phone number or an error message.
    """
    if len(args) != 1:
        return Error.INVALID_COMMAND
    name = args[0]
    return contacts.get(name, BotMessage.CONTACT_NOT_FOUND)

def show_all(contacts: dict) -> str:
    """
    Show all stored contacts.

    :param contacts: Dictionary of contacts.
    :return: All contacts as a formatted string or an error message.
    """
    if not contacts:
        return BotMessage.NO_CONTACTS_FOUND
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])
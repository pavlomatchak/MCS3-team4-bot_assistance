from address_book import AddressBook
from notebook import Notebook
from birthday import BirthdayFormatError, BirthdayValueError
from phone import PhoneFormatError
from record import Record
from address import AddressFormatError, AddressEmptyError
from ct_email import EmailFormatError
import os
import platform
import difflib

def clear_console():

    system = platform.system()

    if system == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except KeyError:
            return "Contact not found!"
        except IndexError:
            return "Give me name please."
        except TypeError:
            return "Give me name and phone please"
    return inner


@input_error
def add_contact(args, contacts: AddressBook):
    try:
        name, phone = args
        contact = Record(name)
        contact.add_phone(phone)
        result = contacts.add_record(contact)
        contacts.save_records()
        return result
    except PhoneFormatError as e:
        return e


@input_error
def change_contact(args, contacts: AddressBook):
    try:
        name, phone1, phone2 = args
        contact = contacts.find(name)
        result = contact.edit_phone(phone1, phone2)
        contacts.save_records()
        return result
    except PhoneFormatError as e:
        return e


@input_error
def delete_contact(args, contacts: AddressBook):
    try:
        name = args[0]
        contacts.delete(name)
        contacts.save_records()
        return 'Contact removed'
    except KeyError:
        return 'Contact not found'


@input_error
def show_phone(args, contacts: AddressBook):
    contact = contacts.find(args[0])
    return f'{contact.name.value}: { ", ".join([phone.value for phone in contact.phones])}'


def show_all(contacts: AddressBook):
    return str(contacts)


def show_contact(args, contacts: AddressBook):
    try:
        name = args[0]
        contact = contacts.find(name)
        return str(contact)
    except IndexError:
        return 'You need to give name.'
    except KeyError:
        return 'Contact not found.'


def add_birthday(args, contacts: AddressBook):
    try:
        name, birthday = args
        contact = contacts.find(name)
        if hasattr(contact, 'birthday'):
            return 'Contact already has birthday.'
        else:
            contact.add_birthday(birthday)
            contacts.save_records()
            return 'Birthday added.'
    except BirthdayFormatError as e:
        return e
    except BirthdayValueError as e:
        return e
    except ValueError:
        return 'You need to give name and birthday.'
    except KeyError:
        return 'Contact not found.'


def show_birthday(args, contacts: AddressBook):
    try:
        name = args[0]
        contact = contacts.find(name)
        return contact.show_birthday()
    except IndexError:
        return 'You need to give name.'
    except KeyError:
        return 'Contact not found.'


def change_birthday(args, contacts: AddressBook):
    try:
        name, birthday = args
        contact = contacts.find(name)
        if not hasattr(contact, 'birthday'):
            return 'Contact has no birthday to change.'
        else:
            contact.add_birthday(birthday)
            contacts.save_records()
            return 'Birthday changed.'
    except BirthdayFormatError as e:
        return e
    except BirthdayValueError as e:
        return e
    except ValueError:
        return 'You need to give name and birthday.'
    except KeyError:
        return 'Contact not found.'


def delete_birthday(args, contacts: AddressBook):
    try:
        name = args[0]
        contact = contacts.find(name)

        if hasattr(contact, 'birthday'):
            contact.remove_birthday()
            contacts.save_records()
            return f'Birthday for {name} deleted.'
        else:
            return 'Contact has no birthday to delete.'
    except IndexError:
        return 'You need to give the name.'
    except KeyError:
        return 'Contact not found.'
    except AttributeError:
        return 'Contact has no birthday to delete.'


def birthdays(args, contacts: AddressBook):
    try:
        count_days = int(args[0])
        return contacts.get_birthdays_for_days(count_days)
    except ValueError:
        return 'You need to give number of days.'
    except IndexError:
        return 'You need to give number of days.'


def add_address(args, contacts: AddressBook):
    try:
        name, *address = args
        address_str = (" ").join(address).title()
        contact = contacts.find(name)
        if hasattr(contact, 'address'):
            return 'Contact already has address.'
        else:
            contact.add_address(address_str)
            contacts.save_records()
            return 'Address added.'
    except AddressFormatError as e:
        return e
    except AddressEmptyError as e:
        return e
    except IndexError:
        return 'You need to give name and address.'
    except KeyError:
        return 'Contact not found.'


def show_address(args, contacts: AddressBook):
    try:
        name = args[0]
        contact = contacts.find(name)
        return contact.show_address()
    except IndexError:
        return 'You need to give name.'
    except KeyError:
        return 'Contact not found.'


def change_address(args, contacts: AddressBook):
    try:
        name, *address = args
        address_str = (" ").join(address).title()
        contact = contacts.find(name)
        if not hasattr(contact, 'address'):
            return 'Contact has no address to change.'
        else:
            contact.add_address(address_str)
            contacts.save_records()
            return 'Address changed.'
    except AddressFormatError as e:
        return e
    except AddressEmptyError as e:
        return e
    except IndexError:
        return 'You need to give name and address.'
    except KeyError:
        return 'Contact not found.'


def delete_address(args, contacts: AddressBook):
    try:
        name = args[0]
        contact = contacts.find(name)

        if hasattr(contact, 'address'):
            contact.delete_address()
            contacts.save_records()
            return 'Address deleted.'
        else:
            return 'Contact has no address to delete.'
    except IndexError:
        return 'You need to give the name of the contact.'
    except KeyError:
        return 'Contact not found.'


def search_contact(args, contacts: AddressBook):
    return contacts.search(args[0].strip())


def add_note(args, notes: Notebook):
    text = ' '.join(args)
    return notes.create_note(text)


def update_note(args, notes: Notebook):
    id, *text = args
    return notes.update_note(id, ' '.join(text))


def search_note(args, notes: Notebook):
    text = ' '.join(args)
    return notes.search_note(text)


def delete_note(args, notes: Notebook):
    id = args[0]
    return notes.remove_note(id)


def all_notes(notes: Notebook):
    return notes


def add_tags(args, notes: Notebook):
    id, *tags = args
    if len(tags) == 0:
        return 'Please enter tags'
    return notes.add_tags(id, tags)
    
def delete_tag(args, notes: Notebook):
    id, tag = args
    return notes.remove_tag(id, tag)


def search_tags(args, notes: Notebook):
    return notes.search_by_tags(args)


def add_email(args, contacts: AddressBook):
    try:
        name, email = args
        contact = contacts.find(name)
        if hasattr(contact, 'email'):
            return 'Contact already has email.'
        else:
            contact.add_email(email)
            contacts.save_records()
            return 'Email added.'
    except EmailFormatError as e:
        return e
    except ValueError:
        return 'You need to give name and email.'
    except KeyError:
        return 'Contact not found.'


def show_email(args, contacts: AddressBook):
    try:
        name = args[0]
        contact = contacts.find(name)
        return contact.show_email()
    except IndexError:
        return 'You need to give name.'
    except KeyError:
        return 'Contact not found.'


def change_email(args, contacts: AddressBook):
    try:
        name, email = args
        contact = contacts.find(name)
        if not hasattr(contact, 'email'):
            return 'Contact has no email to change.'
        else:
            contact.add_email(email)
            contacts.save_records()
            return 'Email changed'
    except EmailFormatError as e:
        return e
    except ValueError:
        return 'You need to give name and email.'
    except KeyError:
        return 'Contact not found.'


def delete_email(args, contacts: AddressBook):
    try:
        name = args[0]
        contact = contacts.find(name)

        if hasattr(contact, 'email'):
            contact.delete_email()
            contacts.save_records()
            return 'Email deleted.'
        else:
            return 'Contact has no email to delete.'
    except IndexError:
        return 'You need to give the name of the contact.'
    except KeyError:
        return 'Contact not found.'


def check_suggestion(keyword, items):
    matches = difflib.get_close_matches(keyword, items, n=3)

    if matches:
        return 'Did you mean\n'+'\n'.join([f'{match}?' for match in matches])
    else:
        return "Invalid command."


def parseCommands(input):
    if input == '':
        return '', []

    cmd, *args = input.strip().lower().split()
    return cmd, args

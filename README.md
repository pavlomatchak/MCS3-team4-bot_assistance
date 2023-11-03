# Contact Assistant README

The Contact Assistant is a versatile tool that allows you to manage contacts and notes effectively. Below is a list of available commands and their descriptions for both the AddressBook and Notes functionality

## AddressBook Functions

- `add`: Add a new contact to the AddressBook.
- `phone`: Display the phone numbers of a contact from the AddressBook.
- `change`: Change the information of an existing phone number in the AddressBook.
- `add-birthday`: Add a birthday for a contact in the AddressBook.
- `show-birthday`: Show the birthday of a contact in the AddressBook.
- `change-birthday`: Change the birthday of a contact from the AddressBook.
- `birthdays`: Show the birthdays of all contacts in the AddressBook for the next N days.
- `add-address`: Add an address for a contact in the AddressBook.
- `show-address`: Show the address of a contact from the AddressBook.
- `change-address`: Change the address of a contact from the AddressBook.
- `add-email`: Add an email address for a contact in the AddressBook.
- `show-email`: Show the email address of a contact from the AddressBook.
- `change-email`: Change the email address of a contact from the AddressBook.
- `all`: Show all contacts in the AddressBook.
- `show`: Show all contact info in the AddressBook.
- `search`: Search for a contact in the AddressBook by name or other criteria.
- `delete`: Delete contact from the AddressBook.

## Notes Functions

- `add-note`: Add a new note to the Notebook.
- `update-note`: Update an existing note in the Notebook.
- `search-note`: Search for a note in the Notebook by content or other criteria.
- `remove-note`: Remove a note from the Notebook.
- `all-notes`: Display all notes in the Notebook.
- `add-tags`: Add note tag to the Notebook.
- `remove-tag`: Remove note tag from the Notebook.

## Usage

To use these functions, you can interact with the Contact Assistant by specifying the desired command and providing any required arguments. For example, to add a new contact, you would use the "add" command and provide the necessary contact details. Below are examples of how to use the commands.

Feel free to explore and utilize the various commands provided by the Contact Assistant to manage your contacts and notes efficiently.

### Examples of use by command:

- `add`:
  > add Anton 0500102030
- `phone`:
  > phone Anton
- `change`:
  > change Anton 0500102030 0670405060
- `add-birthday`:
  > add-birthday Anton 08.11.1981
- `show-birthday`:
  > show-birthday Anton
- `change-birthday`:
  > change-birthday Anton 08.12.1981
- `birthdays`:
  > birthdays 7
- `add-address`:
  > add-address Anton Kyivska St.1, Apt.1, Kyiv, Ukraine, 01001
- `show-address`:
  > show-address Anton
- `change-address`:
  > change-address Anton Pushkinska St.12, Apt.15, Kyiv, Ukraine, 01005
- `add-email`:
  > add-email Anton anton.mail@gmail.com
- `show-email`:
  > show-email Anton
- `change-email`:
  > change-email Anton anton.mail@yahoo.com
- `all`:
  > all
- `show`:
  > show Anton
- `search`:
  > search ant
- `delete`:
  > delete Anton
- `add-note`:
  > add-note 02.11.2023 - training results: 15 km run
- `update-note`:
  > update-note 1 02.11.2023 - training results: 15.5 km run
- `search-note`:
  > search-note training
- `remove-note`:
  > remove-note 1
- `all-notes`:
  > all-notes
- `add-tags`:
  > add-tags 1 training
- `remove-tag`:
  > remove-tag 1 training

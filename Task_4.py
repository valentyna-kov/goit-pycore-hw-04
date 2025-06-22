

def parse_input(user_input: str)-> tuple[str, ...]:
    """
        Parses the User's input into a command and its arguments,
 checks if the command in lower case and does not contain spaces at the beginning and end of the line.
    If the User's input is empty, an empty tuple is returned.

    Args:   
        user_input (str): User's input
    Returns:   
        tuple[str, ...]: Tuple with command and arguments
    """

    if not user_input.strip(): 
        return ("",)  # Returns a tuple with an empty string if User's input is empty
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args:tuple[str, ...] , contacts: dict)-> str:  
    """
    Adds/updates Contact's phone number.
    If it exists, it hint the User to update it

    Args: 
        args (tuple[str, str]): Tuple contains Contacts with name & phone number
        Contacts (dict): Dictionary contains keys (Contact Name) & values (Phone Number) 
    
    """
    if len(args) != 2:
        return "Provide a correct Contact Name & Phone Number"
    
    name, phone = args
    if name in contacts:
        user_result = input(f"With this phone number: {contacts[name]} a Contact {name} exists. Type 'Yes' to update the Contact's phone number. Type 'No' to keep the Contact as is ").strip().lower()   
        if user_result != 'yes': 
            return " "
        else:
            contacts[name] = phone
            return "Contact is updated."
    else:
        contacts[name] = phone
        return "Contact is created."
    
def change_contact(args: tuple[str, ...], contacts: dict) -> str:   
    """
    Updates Contact's phone number.
   
     Args: 
        args (tuple[str, str]): Tuple contains the Contact Name & Phone Number.
        Contacts (dict): Dictionary contains  keys (Contact Name) & values (Phone Numbers)
    """
    if len(args) != 2:
        return "Incorrect input. Provide Contact's Name & Phone Number"
    
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact is updated."
    else:
        return "Contact does not exist."
    
def show_phone(args: tuple[str, ...], contacts: dict) -> str:
    """
    Returns the Phone Number by Contact Name.
    
    Args: 
        name (str): Contact's Name
        Contacts (dict): Dictionary contains keys (Contact Name) & values(Phone Number).
    """
    if len(args) != 1:
        return "Provide Contact Name"
    name = args[0].strip()
    if name in contacts:
        return f"Phone number for {name} is {contacts[name]}."
    else:
        return "Contact does not exist."
    
def show_all(contacts: dict) -> str:  
    """
    Returns all Contacts (Conatct Name, Phone Number) 
    
    Args: 
        contacts (dict): dictionary contains keys (Contact Names) & values (Phone Number)  
    """

    if not contacts: 
        return " "
    result=""
    for name, phone in contacts.items():
        result += f"\n{name}: {phone}"
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))   
        elif command == "phone":
            print(show_phone(args, contacts))    
        elif command == "all":
            print(show_all(contacts))  
        else:
            print("Invalid command.")
    

if __name__ == "__main__":
    main()
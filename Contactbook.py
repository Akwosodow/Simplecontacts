import os
import Contacts

contactlist=[]
titlemessages=["Welcome to contactbook.py", "File saved as Contacts.csv", "Contacts loaded from Contacts.csv", "Contacts.csv not found"]

def userinp(message = "Select Option: "):
    try:
        userinput=int(input(message))
    except ValueError:
        userinput=None
    return(userinput)

def add_page(contactlist):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Due to the way the sorting algorithm is
    coded the format of a contact is as follows:
    1. Firstname
    2. Lastname
    3+ additional information
    
    when typed out this should look like:

    firstname,lastname,additional1,additional2...

    You can store pretty anything past the first
    two as theres currently no checks on anything else.
    """)

    return(Contacts.add_contact(input("Contact to add:" ).split(","), contactlist))


def view_page(contactlist):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Contacts: 
    """)
    for con in contactlist:
        print(con)
    print("""
    
    Sort options:
    Firstname            [1]
    Lastname             [2]

    Exit                 [3]
    """)

    match userinp():
        case 1:
            contactlist=Contacts.sort_contacts(contactlist, False)
        case 2:
            contactlist=Contacts.sort_contacts(contactlist, True)
        case 3:
            return(0)
    
    view_page(contactlist)

def deletion_page(contactlist):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Contacts: 
    """)
    for i, con in enumerate(contactlist):
        print(i, con)

    contactlist = Contacts.del_Contact(userinp("Index of contact to delete: "), contactlist)
    return(contactlist)

def edit_page(contactlist):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Contacts: 
    """)
    for i, con in enumerate(contactlist):
        print(i, con)

    contact = userinp("Which contact would you like to edit: ")

    if contact != None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
    Contact: 
    """)
        try:
            for i, info in enumerate(contactlist[contact]):
                print(i, info)
                
            info = userinp("Which contact would you like to edit: ")
            if info != None:
                contactlist = Contacts.edit_contact(contact, info, input("Change too: "), contactlist)

        except IndexError:
            print("Contact not found")

    return(contactlist)


    return(contactlist)

def exitconf(contactlist):
    userinput=0
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Do you want to save before
    you exit?

    Yes                  [1]
    No                   [2]

    """)

    match userinp():
        case 1:
            Contacts.save_contacts(contactlist)
            return(0)
        case 2:
            return(0)

def app(contactlist: list, titlemessage: str):
    userinput=0
    os.system('cls' if os.name == 'nt' else 'clear')
    msg=0
    print(f"""
    {titlemessage}
    Options:

    View contacts        [1]
    Save contacts        [2]
    Load contacts        [3]
    Sort contacts        [4]

    New Contact          [5]
    Edit Contact         [6]
    Delete contact       [7]

    Exit                 [8]

    """)
    
    match userinp():
        case 1:
            view_page(contactlist)
        case 2:
            Contacts.save_contacts(contactlist)
            msg=1
        case 3:
            try:
                contactlist = Contacts.load_contacts()
                msg=2
            except:
                msg=3
        case 4:
            contactlist = Contacts.sort_contacts(contactlist)
        case 5:
            contactlist = add_page(contactlist)
        case 6:
            contactlist = edit_page(contactlist)
        case 7:
            contactlist = deletion_page(contactlist)
        case 8:
            return(exitconf(contactlist))

    app(contactlist, titlemessages[msg])
app(contactlist, titlemessages[0])
import os
import Contacts

contactlist=[]
def view_page(contactlist):
    print(contactlist)
    input("press enter to exit")

def exitconf(contactlist):
    userinput=0
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Do you want to save before
    you exit?

    Yes                  [1]
    No                   [2]

    """)

    try:
        userinput=int(input("Select Option: "))
    except ValueError:
        userinput=0

    match userinput:
        case 1:
            Contacts.save_contacts(contactlist)
            return(0)
        case 2:
            return(0)

def app(contactlist: list):
    userinput=0
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Welcome to Contactbook.py
    Options:

    View contacts        [1]
    Save contacts        [2]
    Load contacts        [3]
    sort contacts        [4]

    New Contact          [5]
    Delete contact       [6]

    Exit                 [7]

    """)
    try:
        userinput=int(input("Select Option: "))
    except ValueError:
        userinput=0
    
    match userinput:
        case 1:
            view_page(contactlist)
        case 2:
            Contacts.save_contacts(contactlist)
        case 3:
            try:
                contactlist = Contacts.load_contacts(input("Enter file name (leave blank for default): "))
            except:
                print("file not found")
        case 4:
            contactlist = Contacts.sort_contacts(contactlist)
        case 5:
            print("yeah I'll do this later thanks")
        case 6:
            contactlist = Contacts.del_Contact(int(input("Index of contact to delete: ")), contactlist)
        case 7:
            return(exitconf(contactlist))

    app(contactlist)

app(contactlist)
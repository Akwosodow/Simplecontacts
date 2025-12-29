
def del_Contact(idx: int, conlist=[]) -> "removes contact from list":
    conlist[idx]=None
    return(conlist)

def add_contact(cont: list, conlist=[]) -> list:
    """
    Takes in an array with contact information and adds it to the specified contact list
    """
    for i, con in enumerate(conlist):
        if type(conlist[i])!=list:
            conlist[i]=cont
            return(conlist)
    conlist.append(cont)
    return(conlist)

def save_contacts(conlist=[], name = "Contacts.csv") -> "saves as file":
    """
    Takes in a contact list and outputs a comma seperated values file with one contact per line
    """
    with open(name, "wt") as save:  
        for i, con in enumerate(conlist):
            for j, info in enumerate(con):
                save.write(info + ",") if info!=con[-1] else save.write(info)
            save.write("\n") if con!=conlist[-1] else 1==1
    
def load_contacts(name = "Contacts.csv") -> "loads a contact file":
    """
    Loads a specified CVS file and interprets it as a contact list
    """
    final = []
    with open(name, "rt") as f:
        final = f.read().split("\n")
        for i, con in enumerate(final):
            final[i]=con.split(",")
        return(final)

def sort_contacts(contactlist=[], sortby=False):
    """
    Sorts the given contact list using merge sort
    The sortby value defines whether the list is sorted by first or last name (0, 1 respectively)
    """
    mid = len(contactlist)//2
    if mid==0:
        return(contactlist)
    return(merge(sort_contacts(contactlist[:mid]), sort_contacts(contactlist[mid:]), sortby))

def merge(left, right, sortby):
    i, j = 0, 0
    index = 0
    orgsortby = sortby
    swapped=False
    merged=[]
    while i<len(left) and j<len(right):
        try:
            if left[i][sortby][index]==right[j][sortby][index]:
                index+=1
            elif left[i][sortby][index]<right[j][sortby][index]:
                merged.append(left[i])
                i+=1
                index=0
                sortby=orgsortby
            else:
                merged.append(right[j])
                j+=1
                index=0
                sortby=orgsortby
        except IndexError:
            if len(left[i][sortby])>index:
                merged.append(right[j])
                j+=1
            elif len(right[j][sortby])>index:
                merged.append(left[i])
                i+=1
            elif swapped==True:
                merged.append(left[i])
                merged.append(right[j])
                i+=1
                j+=1
                swapped=False
                sortby=orgsortby
            else:
                sortby = not sortby
                swapped=True
            index=0

    while i<len(left):
        merged.append(left[i])
        i+=1
    while j<len(right):
        merged.append(right[j])
        j+=1

    return(merged)
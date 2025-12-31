# Simplecontacts
The experience of editing a CSV file with all of the modern QOL features of computers taken away


## Usage
1. Run contactbook.py
2. Select a given option by typing the letter specified
3. Further menus will function the same as the main menu
4. Some menus have indexes you need to select, these are the values you will see next to the list of contacts provided
5. From here most options are self explainatory however see below for creating a new contact

## New contacts
Because of how the sort function is coded only the first two segments of any contact actually matter to the functionality of this program. The sort is coded to expect a firstname in the first index and a lastname in the second, following that nothing else is checked which allows you to add whatever additional information you wish. To avoid any issues with sorting that may arise from spaces being in strings you can follow this format when creating contacts:

#### Firstname,lastname,additional1,addtional2...

where only commas seperate each individual value.

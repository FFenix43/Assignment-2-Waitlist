# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        if not current:
            print("The waitlist is empty.")
            return
        while current:
            print(current.name)
            current = current.next

    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, name):
        current = self.head
        previous = None
        while current:
            if current.name == name:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True  # Customer removed successfully
            previous = current
            current = current.next
        return False  # Customer not found
    


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    

    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            removed = waitlist.remove(name)
            
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
manager = waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?

The linked list in the .py file behaves differently depending on which method the user calls. If the user calls for the add_front, the list adds the argument (name of the customer), and puts it in the front of the line, which should be number 1. Then, if the user chooses to call the add_end method, it takes the argument and appends it to the end of the list. And for the remove method, it searches for a match in the arguments and returns TRUE, meaning that the customer was removed successfully. And once the customer is removed, the next argument would take their place. For example, if there are three customers, Jessica, David, and Tomas, and if the user removes David, the list would be Jessica as first, and then Tomas as second and last. 


- What role does the head play?

The head is the only entry to the entire data list. And since the nodes are stored independently, the head holds the reference to the first node in the list. And when modifying the first node, it is necessary to update the head from the old node to the new one, which is done in the add-front method in the code.


- When might a real engineer need a custom list like this?

A real engineer would need, for example, a queue for users trying to enter Ticketmaster to buy a ticket, and they might need it to add customers to the list as they enter or removed if they leave the website, to let the customer enter the website to buy the tickets without crashing the network.


'''

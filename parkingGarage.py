# Start Your Code here

#Creating a class called ParkingGarage, that retains a list of available spots and a dictionary containing outstanding tickets/tickets in use

class ParkingGarage():

    """
    The ParkingGarage class will allow people (via input choice) to park, pay or leave with their car. 
    Attributes for the class:
    -spots: expect list, tracking available spots to be used/parked in
    -tickets: expect dictionary (starts empty) - outstanding tickets/tickets in use, tracking their paid/not paid status
    Methods for the class:
    -takeTicket: user chooses to 'park'
    --Method will give user first available item in 'spots' list, and tell them the spot #
    --Method will remove the spot given to user from available spots and move to tickets dictionary
    --IF no spots available (self.spots len = 0), user will be advised garage is full
    --**Add feature to see if user wants to pay right away?
    -payForParking:
    --Method will ask for user's ticket number, then check dictionary to see if paid status = true
    --IF ticket is NOT paid, prompts user to input payment
    --ELIF ticket IS PAID, advises user ticket is already paid, and prints message that they can leave
    -leaveGarage:
    --Method will ask for user's ticket number, then check to see if ticket is paid in dictionary
    --IF ticket iS NOT paid, returns user to park/pay/leave loop
    --IF ticket IS PAID, prints 'goodbye' to user and updates 'spots' list with new 'open spot' and also removes entry in tickets dictionary 
    """

    def __init__(self, spots, tickets):
        self.spots = spots
        self.tickets = tickets

    #Method that allows user to park - removes spot from available spots and updates dictionary with new in-use ticket
    def takeTicket(self):
        if len(self.spots) == 0:
            print("Sorry, Garage is full")
        else:
            new_ticket = self.spots.pop(0)
            self.tickets[new_ticket] = ''
            print(f"Here's your ticket, your ticket number is {new_ticket}. Please keep this for when you leave!")

    #Method that allows user to pay for their ticket, changing their ticket/dictionary from 'Unpaid' to 'Paid', then prints statement that they can proceed to leave
    def payForParking(self):
        ticket = int(input("Please input your ticket number: "))
        if ticket in self.tickets:
            print("Thank you for paying. Please leave in 15 minutes")
            self.tickets[ticket] = 'paid'
        else:
            print("Sorry we could not find ticket number. Please re-enter ticket number.")

    #Method that allows the user to 'leave' the garage, which will check if their ticket is paid (if not, will direct them to payForParking)
    def leaveGarage(self):
        Ticket = int(input("Please input ticket number: "))
        if self.tickets[Ticket] == 'paid':
            print("Goodbye. Thanks for using the garage")
            #delete 
            del self.tickets[Ticket]
            #insert back into available tickets
            self.spots.insert(0, Ticket)
        elif self.tickets[Ticket] == '':
            print("Sorry you haven't paid yet. Please go back and pay")
        else:
            print("Sorry we could not find ticket number. Please re-enter ticket number.")

test_garage = ParkingGarage([1,2,3,4,5,6,7,8,9,10], {})

def run_garage(test_garage):
    print("Welcome to the parking garage.")
    while True:
        response = (input("What would you like to do?(Park/Pay/Leave/Quit) ")).lower()
        if response == 'park':
            test_garage.takeTicket()
        elif response == 'pay':
            test_garage.payForParking()
        elif response == 'leave':
            test_garage.leaveGarage()
        elif response == 'quit':
            break
        else:
            print("Sorry, your input was not recognized - please enter valid input.")

run_garage(test_garage)

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


test_garage = ParkingGarage([1,2,3,4,5,6,7,8,9,10], {})

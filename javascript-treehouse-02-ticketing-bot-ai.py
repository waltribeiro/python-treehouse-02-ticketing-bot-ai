ticket_price = 10

tickets_remaining = 100

# run this code continuously until we run out of tickets
while tickets_remaining >= 1:

    # output how many tickets are remaining using the tickets_remaining variable
    print("There are {} tickets remaining.".format(tickets_remaining))

    # gather the user's name and assign it to a new variable
    name = input("What is your name?  ")

    # prompt the user by name and ask how many tickets they would like 
    num_tickets = input("How many tickets would you like, {}?  ".format(name))
    num_tickets = int(num_tickets)
    amount_due = num_tickets * ticket_price
    print("The total due is ${}".format(amount.due))
    should_proceed = input("Do you want to proceed? Y/N  ")
    if should_proceed.lower() == "y":
        # todo: gather credit card information and process it
        print("SOLD!")
        tickets_remaining -= num-tickets
    else:
        print("Thank you anyways, {}".format(name))

# print("Sorry the tickets are all sold out")
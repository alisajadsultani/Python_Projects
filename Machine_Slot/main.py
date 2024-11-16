import numpy as np
import random as ra

# Generates a random row of three symbols for the slot machine.
def random_val():
    dict1 = {
        1 : 'A',
        2 : 'B',
        3 : 'C',
        4 : 'A',
        5 : 'B',
        6 : 'C',
        7 : 'A',
        8 : 'B',
        9 : 'C',
        10 : 'A',
        11 : 'B',
        12 : 'C',
       
    }
    one = ra.choice(list(dict1.values()))
    two = ra.choice(list(dict1.values()))
    three = ra.choice(list(dict1.values()))
    arr = np.array([one, two, three])
    return arr

balance = 0
# Generates a random row of three symbols for the slot machine.
def deposit_money():
    global balance
    deposit = int(input("Please deposit: $"))
    balance = balance + deposit
    print(f"Current balance is ${balance}")


# Checks if the player won and updates the balance accordingly.
def wining_check(num_lines, bet, comparison):
    global balance, bet_lines
    bet_lines = bet*num_lines
    balance -= bet_lines
    if num_lines == 1:
        if comparison[0] == True:
            balance += bet + bet
            print(f"You won!")
            print(f"Current balance is ${balance}")
        else:
            print("You didn't win!")
            print(f"Your current balance is: ${balance}")
    elif num_lines == 2:
        if comparison[0] == True or comparison[1] == True:
            balance += bet
            for x in comparison:
                if x == True:
                    balance += bet
            print(f"You won!")
            print(f"Current balance is ${balance}")
        else:
            print("You didn't win!")
            print(f"Your current balance is: ${balance}")
    elif num_lines == 3:
        if comparison[0] == True or comparison[1] == True or comparison[2] == True:
            balance += bet
            for x in comparison:
                if x == True:
                    balance += bet
            print(f"You won!")
            print(f"Current balance is ${balance}")
        else:
            print("You didn't win!")
            print(f"Your current balance is: ${balance}")
    else:
        print("Please choose a number betwen 1-3")



# Handles the main gameplay for a slot machine round.
def the_slot_Machine():
    num_lines = int(input("How many number of lines to bet on (1-3): "))
    bet = float(input("What would you like to bet on each line: "))
    if balance < (bet * num_lines):
        print(f"You're betting more than your balance of ${balance}.")
    elif balance <= 0:
        print(f"You have no money left. Please deposit to continue playing.")
    else:
        print(f"You are betting ${bet} on {num_lines}. Total bet is equal to: ${bet*num_lines}")

        row1 = random_val()
        row2 = random_val()
        row3 = random_val()
        slot_machine = np.array([row1, row2, row3])

        for row in slot_machine:
            print(' '.join(map(str, row.flatten())))

        comparison = np.all(slot_machine == slot_machine[:, [0]], axis=1)
        wining_check(num_lines, bet, comparison)
        


# Main game loop that manages deposits and gameplay.
exit = ''
deposit_money()
while(exit != 'q'):
    the_slot_Machine()
    answer = input("Press enter to play (q to exit or d to deposit): ")
    if answer == 'q':
        print("exiting...")
        break
    elif answer == 'd':
        deposit_money()

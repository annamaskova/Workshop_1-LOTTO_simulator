from random import randint

print("""
                                                                      
 __    _____ _____ _____ _____    _____ _           _     _           
|  |  |     |_   _|_   _|     |  |   __|_|_____ _ _| |___| |_ ___ ___ 
|  |__|  |  | | |   | | |  |  |  |__   | |     | | | | .'|  _| . |  _|
|_____|_____| |_|   |_| |_____|  |_____|_|_|_|_|___|_|__,|_| |___|_|  
                                                                      
""")


def lotto_draw():
    """
    draws 6 random numbers from 1 to 49
    :return: list of drawn numbers
    """
    counter = 1
    lotto_list = []
    while counter < 7:
        lotto_list.append(randint(1, 49))
        counter += 1
    return lotto_list


def user_guesses():
    """
    Asks the user to enter 6 numbers.
    Checks if it is a natural number in range 1-49.
    Checks that user chooses a different number each time.
    :return: List of numbers entered by the user, in ascending order.
    """
    position_list = ["first", "second", "third", "fourth", "fifth", "sixth"]
    index = 0
    user_guess_list = []
    while index < len(position_list):
        try:
            guess = int(input(f"Write your {position_list[index]} number: "))
        except ValueError:
            print("This is not an integer!")
            continue
        if guess in user_guess_list:
            print("You have chosen this number before. Choose a different one.")
            continue
        if guess not in range(1, 50):
            print("Your chosen number is not in range 1-49. Choose a different one.")
            continue
        index += 1
        user_guess_list.append(guess)
    return sorted(user_guess_list)


game_is_on = True

while game_is_on:
    numbers_lotto = lotto_draw()
    numbers_user = user_guesses()
    print("")
    print(f"Numbers written by user:", end=" ")
    for num in numbers_user:
        print(num, end=" ")
    print("")
    print(f"Numbers selected by lottery:", end=" ")
    for num in numbers_lotto:
        print(num, end=" ")
    print("\n")
    match_counter = 0
    for num in numbers_user:
        if num in numbers_lotto:
            match_counter += 1
    if match_counter == 1:
        print(f"You matched {match_counter} number with the lottery!")
    else:
        print(f"You matched {match_counter} numbers with the lottery!")
    print()
    print("------------------------------------------------------------------------")

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

import random

destinations = ['Here', 'There', 'Over Yonder',
                'Somewhere', 'This Place', 'That Place', 'Crazy Town']

restaurants = ['This resaurant', 'That Resaurant', 'Big Hole in the Wall', 'Food Truck eat Place',
               'Street Food', 'Go shopping and make your own food', 'Fasting and not eating']

transprtation_options = ['4 wheels', '2 wheels',
                         'no wheels', 'Track', 'Horse', 'Whale Riding', 'Whaling']

entertainment_options = ['Lets go shoot something', 'Lets go swimming', 'Lets watch a movie',
                         'Lets see a live show', 'Throw water ballons and strangers', 'Lets ride some rides', 'Musieum stuff']


def welcome_message():
    print("Welcome to day trip generator! Let's get started 😎")


def choose_destination(list_of_strings):
    destination_is_selected = True

    while destination_is_selected == True:
        destination = random.choice(destinations)
        print(destination)
        user_selection = input(
            f'Are you satisfied with the option of visiting "{destination}" as your destination option-yes or no? ')
        if user_selection == 'yes':
            destination_is_selected = False
            print("Good choice! Moving on. . . ")
            return destination
        else:
            user_selection == 'no'
            print('Lets try again')


def choose_restaurant(list_of_strings):
    restaurant_is_selected = True

    while restaurant_is_selected == True:
        restaurant = random.choice(restaurants)
        print(restaurant)
        user_selection = input(
            f'Are you satisfied with the option of visiting "{restaurant}" as your destination option-yes or no? ')
        if user_selection == 'yes':
            restaurant_is_selected = False
            print("Good choice! Moving on. . . ")
            return restaurant
        else:
            user_selection == 'no'
            print('Lets try again')


def choose_transprtation(list_of_strings):
    transprtation_is_selected = True

    while transprtation_is_selected == True:
        transprtation = random.choice(transprtation_options)
        print(transprtation)
        user_selection = input(
            f'Are you satisfied with the option of visiting "{transprtation}" as your destination option-yes or no? ')
        if user_selection == 'yes':
            transprtation_is_selected = False
            print("Good choice! Moving on. . . ")
            return transprtation
        else:
            user_selection == 'no'
            print('Lets try again')


def choose_entertainment(list_of_strings):
    entertainment_is_selected = True

    while entertainment_is_selected == True:
        entertainment = random.choice(entertainment_options)
        print(entertainment)
        user_selection = input(
            f'Are you satisfied with the option of visiting "{entertainment}" as your destination option-yes or no? ')
        if user_selection == 'yes':
            entertainment_is_selected = False
            print("Good choice! Moving on. . . ")
            return entertainment
        else:
            user_selection == 'no'
            print('Lets try again')


def end_of_choices_message():
    print("Congratulations! Now that your choices have been made let's confirm this is the trip you want. ")
    print('The trip options chosed are:')
    print(place)
    print(dine)
    print(transport)
    print(entertainment_choice)


def confirmed_choices_message():
    print(
        f'Congratulations! You have chosen to go to {place}, eat at {dine}, get there by {transport}, and while you are there you chose to {entertainment_choice}! ')


def farewell_message():
    print("Your trip is ready-let the fun begin! 🎉")


welcome_message()
place = choose_destination(destinations)
dine = choose_restaurant(restaurants)
transport = choose_transprtation(transprtation_options)
entertainment_choice = choose_entertainment(entertainment_options)
end_of_choices_message()
confirmed_choices_message()
farewell_message()

"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40


# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer

PREPARATION_TIME = 2




# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(time_elapsed):

    remaining_time = (EXPECTED_BAKE_TIME - time_elapsed)

    return remaining_time
   

    pass


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(layers):

    preparation_time = (layers*PREPARATION_TIME)

    return preparation_time



# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    prep_time = preparation_time_in_minutes(number_of_layers)
    elapsed_time = (prep_time + elapsed_bake_time)

    return elapsed_time

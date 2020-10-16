def prompt_input(prompt, errormsg):
    """
    Prompts the user for an integer using the prompt parameter.
    If an invalid input is given, an error message is shown using
    the error message parameter. A valid input is returned as an
    integer. Only accepts integers that are bigger than 1.
    """
    is_int = False
    while is_int == False:
        try:
            number = int(input(prompt))
        except ValueError or number == 1:
            print(errormsg)
        else:
            is_int = True
        if number == 1:
            print(errormsg)
            is_int = False
    return number
def check_prime(number):
    """
    Checks whether an integer is a prime number. Returns False
    if the number isn't a prime; if it is a prime, returns True
    """
prime_number = prompt_input("Give an integer that's bigger than 1:", "You had one job")
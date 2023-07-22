# Function are group of code to perform a specific task

def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()


#passing information to function

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()}!")
greet_user('jackson')

#arguments and parameters

#variable username in   definition of a function is called parameter
#parameter- a piece of info function need to perform its job

#the value "jackson" in function call is argument
#argument- is a piece of info that is passed from a function call to a function.
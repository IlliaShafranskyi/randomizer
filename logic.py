import random
import string

def random_pass(length):

    password = []

    for i in range(length):
        
        lowercase = random.choice(string.ascii_lowercase) #one random lowercase character
        uppercase = random.choice(string.ascii_uppercase) #uppercase character
        l_or_n = random.choice(["char", "number"])
       
        if(l_or_n == "char"):
            element = random.choice([lowercase, uppercase])
        else:
            element = random.randint(1, 9)
       
        password.append(str(element))
    
    return "".join(password)


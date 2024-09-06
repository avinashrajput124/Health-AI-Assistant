import random

def generate_random_name():
    first_names = [
        'Emma', 'Liam', 'Ava', 'Noah', 'Sophia', 'Jackson', 
        'Olivia', 'Aiden', 'Isabella', 'Mason','Avinash','David'
    ]
    
    last_names = [
        'Johnson', 'Smith', 'Williams', 'Brown', 'Davis', 'Rajput', 'warner',
        'Miller', 'Garcia', 'Martinez', 'Rodriguez', 'Taylor'
    ]
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    return first_name, last_name


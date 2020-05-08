import random
import sys
import time

anions = ['Acetate', 'Carbonate', 'Iodide', 'Nitrate', 'Phosphate', 'Sulphate']
cations = ['Aluminum', 'Calcium', 'Copper', 'IronII', 'IronIII', 'Cobalt', 'Nickel', 'Potassium', 'Sodium']


def decision(probability):
    return random.random() < probability


def print_slow(string, speed=0.1):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)


def print_immersive_dots():
    print_slow('....\n', speed=1)


def check_number(inp, data_type, suggestion):
    try:
        value = data_type(inp)
        return value
    except ValueError:
        print(f'Wrong kind of input. Please write {suggestion}.')
        return None


def check_text(inp, suggestion, options):
    if inp not in options:
        print(f'Wrong kind of input. Please write {suggestion}.')
        return None
    else:
        return inp

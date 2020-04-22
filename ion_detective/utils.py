import base64
import random
import sys
import time

anions = ['Acetate', 'Carbonate', 'Iodide', 'Nitrate', 'Phosphate', 'Sulphate']
cations = ['Aluminum', 'Calcium', 'Copper', 'IronII', 'IronIII', 'Cobalt', 'Nickle', 'Potassium', 'Sodium']

def _obfuscator(secret, compare):
    pass


def decision(probability):
    return random.random() < probability

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

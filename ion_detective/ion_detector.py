import random

from ion_detective.utils import anions, cations


class IonDetector:
    def __init__(self):
        self.__ion_probe = None
        self.__seed = None

    def generate_probe(self, ion_type: str, seed: int):
        random.seed(seed*1337)
        self.__seed = seed
        if ion_type == 'anions':
            ion_list = anions
        elif ion_type == 'cations':
            ion_list = cations
        else:
            raise ValueError('Know your ion type!')
        self.__ion_probe = random.sample(ion_list, k=3)

    def list_ions(self):
        print(f'Anions: {anions}\n')
        print(f'Cations: {cations}')

    def test_ion(self, ion_name):
        if ion_name not in anions and ion_name not in cations:
            print(f'{ion_name} not in the list of anions or cations. Call .list_ions() to get the correct names!')
            return None
        return True if ion_name in self.__ion_probe else False

    def truth_detector(self, function):
        anion_test = function(42, 'anions')
        if set(anion_test) == set(self.__ion_probe):
            print('Correct Anions!')

        cation_test = function(42, 'cations')
        if set(cation_test) == set(self.__ion_probe):
            print('Correct Cations!')

    def __test_truth(self, seed, ion_type):
        self.generate_probe(ion_type, seed)
        ions = anions if ion_type == 'anions' else cations
        positives = []
        for ion in ions:
            if self.test_ion(ion):
                positives.append(ion)
        return positives

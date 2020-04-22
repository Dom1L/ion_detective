import random

from ion_detective.utils import anions, cations


class IonDetective:
    def __init__(self):
        pass

    def generate_probe(self, ion_type, seed):
        random.seed(seed)
        if ion_type == 'anion':
            ion_list = anions
        elif ion_type == 'cations':
            ion_list = cations
        else:
            raise ValueError('Know your ion type!')
        # should be encrypted somehow
        self.ion_probe = random.sample(ion_list, k=3)

    def get_answers(self, your_solutions):
        pass

    # Anion Test
    def test_acetate(self):
        pass

    def test_carbonate(self):
        pass

    def test_iodide(self):
        pass

    def test_nitrate(self):
        pass

    def test_phosphate(self):
        pass

    def test_sulphate(self):
        pass

    # Cation Test
    def test_calcium(self):
        pass

    def test_iron2(self):
        pass

    def test_iron3(self):
        pass

    def test_cobalt(self):
        pass

    def test_potassium(self):
        pass

    def test_sodium(self):
        pass

    def separate_urotropine_group(self):
        pass
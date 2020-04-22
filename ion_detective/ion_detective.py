import random

from ion_detective.utils import anions, cations, decision


class IonDetective:
    def __init__(self):
        self._ion_probe = None

    def generate_probe(self, ion_type: str, seed: int):
        random.seed(seed)
        if ion_type == 'anion':
            ion_list = anions
        elif ion_type == 'cations':
            ion_list = cations
        else:
            raise ValueError('Know your ion type!')
        # should be encrypted somehow
        self._ion_probe = random.sample(ion_list, k=3)

    def get_answers(self, your_solutions: list):
        points = 0
        for ion in your_solutions:
            if ion in self._ion_probe:
                points += 1
        print(f'You achieved {points} out of 3 points!')

    # Anion Test
    def test_acetate(self):
        print('A spatula tip of the substance has to be rubbed into the mortar with KHSO4.')

        value = input('How much KHSO4 do you want to add? x times more than substance: x?')
        if int(value) < 4:
            return print('You smell nothing...')

        if 'Acetate' in self._ion_probe:
            print('It smells like vinegar....')
        else:
            print('You smell nothing...')

    def test_carbonate(self):
        random_failure = 0
        print('You have to mix your substance with a couple of drops of HCl 2M.')
        mg_value = input('How much substance do you use? Mg: ')
        drop_value = input('How many drops of 2M HCL do you use? Approximate amount of drops: ')

        if int(mg_value) != 10:
            random_failure += 0.3
        if not 5 <= int(drop_value) <= 10:
            random_failure += 0.3

        print('The test tube is quickly sealed with a stopper,  '
              'which  carries  a  gas  absorptiontube (filled with barium hydroxide solution).')

        if 'Carbonate' not in self._ion_probe or decision(random_failure):
            return print('Nothing seems to happen...')
        else:
            print('The mixture flares up and delivers acolorless and odourless gas.  '
                  'When slightly heated, a white precipitate is formed which dissolves in excess hydrochloric acid.')

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

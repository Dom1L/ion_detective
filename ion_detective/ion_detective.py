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
        random_failure = 0
        print('Dissolve a spatula tip of the sample substance in x mL water and acidify it with diluted nitric acid 2M.')
        ml_value = input('How much water do you want to add? mL: ')
        if int(ml_value) != 2:
            random_failure += 0.2

        print('After adding a few drops of silver nitrate 0.25M, shake and let stand.')
        print('After waiting a couple of minutes, you add 1.5 mL NH3-solution 10M.')

        if 'Iodide' not in self._ion_probe or decision(random_failure):
            print('Nothing seems to happen...')
        else:
            print('You see a pale yellow precipitate. You start shaking heavily, but it does not seem to dissolve.')

    def test_nitrate(self):
        print('In a test tube a few drops of your sample solution are mixed with about the same amount of '
              'cold saturated iron (II) sulphate solution and acidified with slightly diluted sulphuric acid. '
              'Then carefully undercoated with concentrated sulphuric acid.'
              ' To  do this, suck a Pasteur pipettefull, place it on the bottom of the RG and slowly squeeze the H2SO4 out. '
              'Before thepasteurised pipette is completely empty, it is pulled out of the glass, but the pressure on the '
              'nuggi  must  be  maintained  '
              '(otherwise  sample  solution  is  drawn  in  and  thephase boundary may be destroyed')

        if 'Nitrate' not in self._ion_probe:
            print('Nothing seems to happen...')
        else:
            print('You can observe a brown-ish ring form at the phase boundary.')

    def test_phosphate(self):
        random_failure = 0
        print('A spatula tip of substance has to be dissolved in 1 mL of water, acidified with diluted HNO3 and mixed with'
              '2 mL molybdate-vanadate.')

        yes_no = input('Make a new batch of molybdate-vanadate? Yes/No: ')
        if yes_no is 'No':
            random_failure += 0.66

        if 'Phosphate' in self._ion_probe or decision(random_failure):
            print('A yellow colouring occures. You slowly heat the solution and the colour intensifies!')
        else:
            print('The colour of your solution does not seem to change at all...')

    def test_sulphate(self):
        print('You start with approx. 3 mL sample solution. You are unsure whether you have to acidify or basify your solution')

        acid_base = input('Acidify/Basify: ')
        if acid_base is 'Basify':
            return print('You add NaOH and mix with 1 mL barium (II) chloride solution 0.25M, but nothings seems to happen...')
        else:
            print('You acidify your solution with diluted hydrochloric acid 2M and mix with 1 mL barium (II) chloride solution 0.25M.')

        if 'Sulphate' in self._ion_probe:
            print('You can see a white precipitate!')
        else:
            print('Nothing seems to happen...')

    # Cation Test
    def test_copper(self):
        print('A magnesia stick is annealed in the Bunsen burner flame. With the still hot rod, '
              'some of the substance is absorbed and kept in the burner flame.')

        if 'Copper' in self._ion_probe:
            print('You can see a green flame!')
        else:
            print('Nothing seems to happen...')

    def test_calcium(self):
        print('A magnesia stick is annealed in the Bunsen burner flame. With the still hot rod, '
              'some of the substance is absorbed and kept in the burner flame.')

        if 'Calcium' in self._ion_probe:
            print('You can see a brick-red flame! That has to mean something...')
        else:
            print('Nothing seems to happen...')

    def test_sodium(self):
        print('A magnesia stick is annealed in the Bunsen burner flame. With the still hot rod, '
              'some of the substance is absorbed and kept in the burner flame.')

        if 'Sodium' in self._ion_probe:
            print('You can see a yellow flame, what could that be?')
        else:
            print('Nothing seems to happen...')

    def test_aluminum(self):
        print('You mix approx. 2 mL solution with 0.5 mL diluted HCL and 0.5 mL tioacetamid reagent. '
              'Occuring precipitate is being filtered.'
              'You start adding drops of diluted NaOH solution.')

        if 'Aluminum' in self._ion_probe:
            print('You can see a gelatinous precipitate. It dissolves once you add more NaOH.'
                  'After adding ammonium chloride solution, you can see the white gelatinous precipitate forming again.')
        else:
            print('You add more and more solution, but nothing seems to happen (besides the change in pH).')

    def test_iron2(self):
        print('You add 1 mL of potassium hexacyanoferrate (III) solution 0.125M to your sample solution.')

        if 'IronII' in self._ion_probe:
            print('You can see a deep blue precipitate forming. '
                  'Even adding 5mL diluted HCL does not seem to dissolve the precipitate.')
        else:
            print('Nothing seems to happen...')

    def test_iron3(self):
        print('You mix a few drops of sample solution with a drop of KSCN solution.')

        if 'IronIII' in self._ion_probe:
            print('The colour of the solution turned red!')
        else:
            print('No colour change is observable...')

    def test_cobalt(self):
        print('You add a little KSCN to your sample solution.')

        if 'Cobalt' in self._ion_probe:
            print('The colour changes to blue!')
        else:
            print('Nothing seems to happen...')

    def test_nickel(self):
        print('You add NaOH to your sample solution.')

        if 'Nickel' in self._ion_probe:
            print('You can observe a green precipitate forming.')
        else:
            print('Nothing seems to happen...')

    def test_potassium(self):
        print('You mix approx. 1 mL of perchloricacid to your sample substance.'
              'In the next step you have to heat the solution...')

        heating = input('Heat the solution fast or slow? ')
        if heating == 'fast':
            return print('Congratulations! You did not read the instructions and blew up the laboratory. '
                         'This is not good...')

        if 'Potassium' in self._ion_probe:
            print('After cooling, you see white crystals forming. What could that be?')
        else:
            print('You let the solution cool down, but nothing happened.')

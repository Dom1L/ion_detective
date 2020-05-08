import re
import random

from ion_detective.utils import anions, cations, decision, print_slow, print_immersive_dots, check_number, check_text


class IonDetective:
    def __init__(self):
        self.__ion_probe = None
        self.__seed = None
        self.__answer_counter = 0
        print('IonDetective initialized! Call .generate_probe() to start!')

    def generate_probe(self, ion_type: str, seed: int):
        random.seed(seed)
        self.__seed = seed
        if ion_type == 'anions':
            ion_list = anions
        elif ion_type == 'cations':
            ion_list = cations
        else:
            raise ValueError('Know your ion type! Use either anions or cations')
        self.__ion_probe = random.sample(ion_list, k=3)
        print('Probe generated, now perform some experiments!\n')
        print('Use .list_ions() to see which ions are available.\n')
        print('Use .list_anion_tests() or .list_cation_tests() to see which experiments can be performed\n')

    def get_answers(self, your_solutions: list):
        if self.__answer_counter >= 1:
            print('You can only get your answers once!')
            return None
        elif self.__seed > 100:
            print('Only seeds lower than 100 can be used with this function!')
            return None
        elif len(your_solutions) > 3:
            print('You should not submit more than 3 answers!')
            return None

        points = 0
        correct_ions = []
        for ion in your_solutions:
            if ion in self.__ion_probe and ion not in correct_ions:
                points += 1
                correct_ions.append(ion)
        print_slow(f'You achieved {points} out of 3 points!')
        self.__answer_counter += 1

    def list_ions(self):
        print(f'Anions: {anions}\n')
        print(f'Cations: {cations}')

    def list_anion_tests(self):
        print('test_acetate(), \n'
              'test_carbonate(), \n'
              'test_iodide(), \n'
              'test_nitrate(), \n'
              'test_sulphate(), \n'
              'test_phosphate(),'
              )

    def list_cation_tests(self):
        print('test_copper(), \n'
              'test_calcium(), \n'
              'test_sodium(), \n'
              'test_aluminum(), \n'
              'test_iron2(), \n'
              'test_iron3(), \n'
              'test_cobalt(), \n'
              'test_nickel(), \n'
              'test_potassium()'
              )

    # Anion Tests
    def test_acetate(self):
        print_slow('You rub a spatula tip of your substance into the mortar with KHSO4. \n')

        value = None
        while value is None:
            value = input('How much KHSO4 do you want to add? x times more than substance: \n'
                          'x=')
            value = check_number(value, data_type=float, suggestion='a number')

        print_immersive_dots()

        if value < 4:
            return print_slow('You smell nothing...')

        if 'Acetate' in self.__ion_probe:
            print_slow('It smells like vinegar....')
        else:
            print_slow('You smell nothing...')

    def test_carbonate(self):
        random_failure = 0
        print_slow('You have to mix your substance with a couple of drops of HCl 2M. \n')

        value = None
        while value is None:
            value = input('How much substance do you use? \n'
                          'Mg: ')
            value = check_number(value, data_type=float, suggestion='a number')
        if value != 10:
            random_failure += 0.3
        print_immersive_dots()

        value = None
        while value is None:
            value = input('How many drops of 2M HCL do you use? Approximate amount of drops: \n'
                          ' ')
            value = check_number(value, data_type=float, suggestion='a number')

        if not 5 <= value <= 10:
            random_failure += 0.3
        print_immersive_dots()

        print_slow('The test tube is quickly sealed with a stopper, '
                   'which carries a gas absorption tube (filled with barium hydroxide solution). \n')

        print_immersive_dots()

        if 'Carbonate' not in self.__ion_probe or decision(random_failure):
            return print_slow('Nothing seems to happen...')
        else:
            print_slow('The mixture flares up and delivers a colorless and odourless gas. \n'
                       'When slightly heated, a white precipitate is formed which dissolves in excess hydrochloric acid.')

    def test_iodide(self):
        random_failure = 0
        print_slow(
            'Dissolve a spatula tip of the sample substance in x mL water and acidify it with diluted nitric acid 2M. \n')

        value = None
        while value is None:
            value = input('How much water do you want to add? \n'
                          'mL: ')
            value = check_number(value, data_type=float, suggestion='a number')

        if value != 2:
            random_failure += 0.2

        print_immersive_dots()
        print_slow('After adding a few drops of silver nitrate 0.25M, shake and let stand. \n')
        print_immersive_dots()
        print_slow('After waiting a couple of minutes, you add 1.5 mL NH3-solution 10M. \n')
        print_immersive_dots()

        if 'Iodide' not in self.__ion_probe or decision(random_failure):
            print_slow('Nothing seems to happen...')
        else:
            print_slow(
                'You see a pale yellow precipitate. You start shaking heavily, but it does not seem to dissolve.')

    def test_nitrate(self):
        print_slow('In a test tube a few drops of your sample solution are mixed with about the same amount of \n'
                   'cold saturated iron (II) sulphate solution and acidified with slightly diluted sulphuric acid. \n'
                   'Then carefully undercoated with concentrated sulphuric acid.')

        print_immersive_dots()

        if 'Nitrate' not in self.__ion_probe:
            print_slow('Nothing seems to happen...')
        else:
            print_slow('You can observe a brown-ish ring form at the phase boundary.')

    def test_phosphate(self):
        random_failure = 0
        print_slow('You dissolve a spatula tip of your substance in 1 mL of water. \n'
                   'After that, you acidify your solution with diluted HNO3 and mix with 2 mL molybdate-vanadate. \n')

        value = None
        while value is None:
            value = input('Make a new batch of molybdate-vanadate? \n'
                          'yes/no: ')
            value = re.sub('[^A-Za-z]+', '', value.lower().strip())
            value = check_text(value, options=['yes', 'no'], suggestion='yes or no')

        if value is 'no':
            random_failure += 0.66

        print_immersive_dots()

        if 'Phosphate' in self.__ion_probe or decision(random_failure):
            print_slow('A yellow colouring occures. You slowly heat the solution and the colour intensifies!')
        else:
            print_slow('The colour of your solution does not seem to change at all...')

    def test_sulphate(self):
        print_slow('You start with approx. 3 mL sample solution. \n'
                   'You are unsure whether you have to acidify or basify your solution... \n')

        value = None
        while value is None:
            value = input('acidify/basify: ')
            value = re.sub('[^A-Za-z]+', '', value.lower().strip())
            value = check_text(value, options=['acidify', 'basify'], suggestion='acidify or basify')

        print_immersive_dots()

        if value is 'basify':
            return print_slow(
                'You add NaOH and mix with 1 mL barium (II) chloride solution 0.25M, but nothings seems to happen...')
        else:
            print_slow('You acidify your solution with diluted hydrochloric acid 2M and '
                       'mix with 1 mL barium (II) chloride solution 0.25M. \n')

        if 'Sulphate' in self.__ion_probe:
            print_slow('You can see a white precipitate!')
        else:
            print_slow('Nothing seems to happen...')

    # Cation Test
    def test_copper(self):
        print_slow('You anneal a magnesia stick in the Bunsen burner flame. \n'
                   'With the still hot rod, some of your substance is absorbed and kept in the burner flame. \n')

        print_immersive_dots()

        if 'Copper' in self.__ion_probe:
            print_slow('You can see a green flame!')
        else:
            print_slow('Nothing seems to happen...')

    def test_calcium(self):
        print_slow('You anneal a magnesia stick in the Bunsen burner flame. \n'
                   'With the still hot rod, some of your substance is absorbed and kept in the burner flame. \n')

        print_immersive_dots()

        if 'Calcium' in self.__ion_probe:
            print_slow('You can see a brick-red flame! That has to mean something...')
        else:
            print_slow('Nothing seems to happen...')

    def test_sodium(self):
        print_slow('You anneal a magnesia stick in the Bunsen burner flame. \n'
                   'With the still hot rod, some of your substance is absorbed and kept in the burner flame. \n')

        print_immersive_dots()

        if 'Sodium' in self.__ion_probe:
            print_slow('You can see a yellow flame, what could that be?')
        else:
            print_slow('Nothing seems to happen...')

    def test_aluminum(self):
        random_failure = 0
        print_slow('You mix approx. 2 mL solution with 0.5 mL diluted HCL and 0.5 mL thioacetamid reagent. \n'
                   'You see precipitate forming...')

        value = None
        while value is None:
            value = input('Filter precipitate? yes/no: \n'
                          ' ')
            value = re.sub('[^A-Za-z]+', '', value.lower().strip())
            value = check_text(value, options=['yes', 'no'], suggestion='yes or no')

        if value == 'no':
            random_failure += 0.33

        print_slow('You start adding drops of diluted NaOH solution. \n')
        print_immersive_dots()

        if 'Aluminum' in self.__ion_probe or not decision(random_failure):
            print_slow('You can see a gelatinous precipitate. \n'
                       'It dissolves once you add more NaOH. \n'
                       'After adding ammonium chloride solution, '
                       'you can see the white gelatinous precipitate forming again.')
        else:
            print_slow('You add more and more solution, but nothing seems to happen (besides the change in pH).')

    def test_iron2(self):
        print_slow('You add 1 mL of potassium hexacyanoferrate (III) 0.125M to your sample solution. \n')

        print_immersive_dots()

        if 'IronII' in self.__ion_probe:
            print_slow('You can see a deep blue precipitate forming. \n'
                       'Even adding 5 mL diluted HCL does not seem to dissolve the precipitate!')
        else:
            print_slow('Nothing seems to happen...')

    def test_iron3(self):
        print_slow('You mix a few drops of sample solution with a drop of KSCN solution. \n')

        print_immersive_dots()

        if 'IronIII' in self.__ion_probe:
            print_slow('The colour of the solution turned red!')
        else:
            print_slow('No colour change is observable...')

    def test_cobalt(self):
        print_slow('You add a little KSCN to your sample solution. \n')

        print_immersive_dots()

        if 'Cobalt' in self.__ion_probe:
            print_slow('The colour changes to blue!')
        else:
            print_slow('Nothing seems to happen...')

    def test_nickel(self):
        print_slow('You add NaOH to your sample solution. \n')

        print_immersive_dots()

        if 'Nickel' in self.__ion_probe:
            print_slow('You can observe a green precipitate forming.')
        else:
            print_slow('Nothing seems to happen...')

    def test_potassium(self):
        print_slow('You mix approx. 1 mL of perchloricacid to your sample substance. \n'
                   'In the next step you have to heat the solution... \n')

        value = None
        while value is None:
            value = input('Heat the solution fast or slow? \n'
                          ' ')
            value = re.sub('[^A-Za-z]+', '', value.lower().strip())
            value = check_text(value, options=['fast', 'slow'], suggestion='fast or slow')

        print_immersive_dots()

        if value == 'fast':
            return print_slow('Congratulations! You did not read the instructions and blew up the laboratory. \n'
                              'This is not good...')

        if 'Potassium' in self.__ion_probe:
            print_slow('After cooling, you see white crystals forming. What could that be?')
        else:
            print_slow('You let the solution cool down, but nothing happened.')

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
        print('If a spatula tip substance is dissolved in 1 mL of water, acidified with diluted HNO3and mixed with 2 mL molybdate-vanadate '
              'reagent, a yellow colouring occurs. When heated, the yellow colour intensifies.(NH4)2MoO4/(NH4)3VO4 forms '
              'with phosphate ions in neutral to nitric acid solutionorange colored anions of mixed heteropolyacid[PV2Mo10O40]5−.'
              'This reaction is considered to be the best colorimetric method for the determination of phosphates. '
              'The molybdate-vanadate reagent has only a limited shelf life (maximum of one day), '
              'needs to be remanufactured regularly (therefore never produce too large quantities) and '
              'regularly checked by negative image samples. Failure to do so may result inpositive results even though '
              'there is no phosphate in the sample')

    def test_sulphate(self):
        print('Approx. 3 mL sample solution are acidified well with diluted hydrochloric acid 2Mand mixed with 1 mL barium (II) '
              'chloride solution 0.25M. A white precipitation occurs.')

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
        print('Ca. 2 mL Probenlösung werden mit 0.5 mL verdünnter Salzsäure R und etwa 0.5 mL Thioacetamid-Reagenz versetzt. '
              'Evtl auftretender Niederschlag wird abdekantiert. '
              'Nach tropfenweisem Zusatz von verdünnter NaOH-Lösung R zur Lösung entsteht ein weisser, gallertartiger Niederschlag, '
              'der sich bei weiterem Zusatz von NaOH wieder löst. Bei allmählichem Zusatz von Ammoniumchlorid-Lösung R bildet sich '
              'wieder ein weisser, gallertartiger Niederschlag.')

    def test_iron2(self):
        print('After addition of 1 mL potassium hexacyanoferrate (III) solution 0.125M to the sample solution, '
              'a deep blue precipitate is formed which does not dissolve even afteraddition of 5 ml of diluted hydrochloric acid R1.')

    def test_iron3(self):
        print('After addition of 1 mL potassium hexacyanoferrate (III) solution 0.125M to the sample solution, '
              'a deep blue precipitate is formed which does not dissolve even afteraddition of 5 ml of diluted hydrochloric acid R1.')

    def test_cobalt(self):
        print('In a test tube, add a few drops of a neutral or acetic acid sample solution with a little KSCN or NH4SCN.')

    def test_nickel(self):
        print('Ni2−forms with hydroxide ions a hardly soluble greenish deposit of Ni(OH)2.')

    def test_potassium(self):
        print('A clear solution of the sample substance is mixed with approx. 1 mL of perchloricacid and heated carefully. '
              'Careful!! Do not overheat. Do not evaporate until dry.Risk of explosion!'
              'After cooling, white potassium perchlorate crystallizes')

    def separate_urotropine_group(self):
        pass


import modules.coreRules as coreRules
import modules.dice as dice
import pprint as pp


stat_char_limit = 15

class rpgCharacter:
    def __init__(self, name) -> None:
        self._race = 'Human'
        self._name = name

        self._attributes = {}
        self._psych = {}

        self._combat ={}

        self._skills = {}
        
        self._techniques = {}
        self._talents = {}

        self._profile = {} 

        self._log ={}

    def set_attributes(self, stats):
        self._attributes = dict([(k,v) for k, v in sorted(stats.items())])

    def set_psych(self, psych):
        self._psych = dict([(k,v) for k, v in sorted(psych.items())])

    def set_race(self, race):
        self._race = race['Race']
        if race.get('Attributes'):
          for a, mod in race['Attributes'].items() :
            #print(f'{a} mod is >{mod}<')
            #orig_value = self._attributes.get(a)
            print(f'applying modifier /{mod}/ to base value {self._attributes[a]} for {a}')            
            self._attributes[a] = dice.calc_mod(self._attributes[a], mod)

TODO: switch self._attributes to self.stats['attributes']

    def format_item(self, item_tuple):
      return f'{(item_tuple[0]).upper() : >15} : {item_tuple[1]:2d}'

    def get_current_attribute(self, attribute_name):
      if attribute_name in self._attributes:
        return self._attributes[attribute_name]
      return 0

    def get_current_reaction_modifer(self):
      return "Reaction Modifier", self.get_current_attribute("Reflexes")

    def format_section(self, section_dict):
        return [self.format_item(i) for i in section_dict.items()]

    def align_2_columns(self, col1, col2, index, col1_width, col2_width):
        v1 =  col1[index] if index < len(col1) else " "
        v2 =  col2[index] if index < len(col2) else " " 
        return f'{v1 : >{col1_width}}{v2 : >{col2_width}}'

    def dump_character(self):
        print(f'{"NAME": >15} : {self._name: <15} {"RACE": >15} : {self._race: <15}')

        attributes = self.format_section(self._attributes)
        psychs = self.format_section(self._psych)

        for x in range(max(len(attributes), len(psychs))):
          print(self.align_2_columns(attributes, psychs, x, 20, 20))
        
        print(f'{self.format_item(self.get_current_reaction_modifer())}')

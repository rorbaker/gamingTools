
import modules.coreRules as coreRules

stat_char_limit = 15

class rpgCharacter:
    def __init__(self, name, race) -> None:
        self._race = race
        self._name = name

        self._attributes = []
        self._psych = []

        self._skills = {}
        
        self._techniques = {}
        self._talents = {}

        self._profile = {} 

        self._log ={}

    def set_attributes(self, stats):
        self._attributes = [(s, stats[s]) for s in coreRules.attribute_display_order ]

    def set_psych(self, psych):
        self._psych = [(p, psych[p]) for p in coreRules.psych_display_order ]   

    def format_item(self, item_list, index):
      if index < len(item_list) :
        return f'{(item_list[index][0]).upper() : >15} : {item_list[index][1]:2d}'
      return ""

    def dump_character(self):
        print(f'{"NAME": >15} : {self._name: <25} {"RACE": >15} : {self._race: <25}')

        for x in range(max(len(self._attributes), len(self._psych))):
          print(f'{self.format_item(self._attributes, x)} | {self.format_item(self._psych, x)}')


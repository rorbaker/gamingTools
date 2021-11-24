
import modules.coreRules as coreRules


class rpgCharacter:
    def __init__(self, name, race) -> None:
        self._race = race
        self._name = name

        self._stats = {}
        self._pyshc = {}

        self._skills = {}
        
        self._techniques = {}
        self._talents = {}

        self._profile = {} 

        self._log ={}

    def set_stats(self, stats):
        self._stats = [(s, stats[s]) for s in coreRules.stat_display_order ]


    def dump_character(self):
        print(f'{"NAME": >15} : {self._name: <25} {"RACE": >15} : {self._race: <25}')
        for s in self._stats:
            print(f'{(s[0]).upper() : >15} : {s[1]:2d}')
        
        
        

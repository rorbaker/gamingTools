from typing import Counter
import os
import yaml
import modules.dice as dice
import modules.coreRules as coreRules
import modules.statsGenerators as statsGenerators
import modules.templates as templates
import modules.rpgCharacter as rpgCharacter
import modules.templates as templates

import pprint as pp

race_definitions = templates.read_race_templates( os.path.join( 'data', 'races'))
template_definitions = templates.read_templates( os.path.join( 'data', 'templates'))

# pp.pprint(template_definitions)
# pp.pprint(template_definitions.keys())

### TODO: figure out how to accept command line input to select templates

use_templates = {key: value for key, value in template_definitions.items() if dice.get_simple_result(1, 10) < 4}

pp.pprint(use_templates.keys())

attribute_templates = {k:v.get('Attributes') for (k, v) in use_templates.items()}
pysch_templates = {k:v.get('Psych') for (k, v) in use_templates.items()}

my_char = rpgCharacter.rpgCharacter('bill', 'human')

raw_stats = statsGenerators.generate_avg_stats(10, 12, 40, 60)

final_stats = templates.distribute_values(coreRules.attribute_display_order, raw_stats, attribute_templates.values())
my_char.set_attributes(final_stats)

raw_psych = statsGenerators.generate_avg_stats(10, 10)
final_psych = templates.distribute_values(coreRules.psych_display_order, raw_psych, pysch_templates.values())

my_char.set_psych(final_psych)

my_char.dump_character()




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

use_templates = {key: value for key, value in template_definitions.items() if dice.get_simple_result(1, 10) < 4}

pp.pprint(use_templates.keys())

my_char = rpgCharacter.rpgCharacter('bill', 'human')

raw_stats = statsGenerators.generate_avg_stats(10, 12, 40, 50)
# print(f"stats total: {sum(raw_stats)}")

final_stats = templates.apply_stats_templates(coreRules.stat_alpha_order, raw_stats, use_templates)
my_char.set_stats(final_stats)

my_char.dump_character()




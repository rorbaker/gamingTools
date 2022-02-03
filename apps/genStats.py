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

import argparse


####  main starts here
parser = argparse.ArgumentParser(description='Generate Random character based on templates')
parser.add_argument('--Race', '-r', metavar='race', help='The Character\'s Race', default='Human')
parser.add_argument('--Name', '-n', metavar='name', help='The Character\'s Name', required=True)
parser.add_argument('--Temperment', '-t', metavar='temperment', help='Template to be used for pyshcological profile', nargs='*', required=False, default=[])
parser.add_argument('--Architype', '-a', metavar='architype', help='Template to be used for architype', nargs='*', required=False, default=[])


args = parser.parse_args()

allTemplates = args.Temperment 
allTemplates.extend( args.Architype)

pp.pprint(args)

pp.pprint(templates.race_definitions)

raceSettings = templates.race_definitions[args.Race]
pp.pprint(raceSettings)


use_templates = dict((k, templates.template_definitions[k]) for k in allTemplates if k in templates.template_definitions)
pp.pprint(use_templates.keys())

attribute_templates = {k:v.get('Attributes') for (k, v) in use_templates.items()}
pysch_templates = {k:v.get('Psychological') for (k, v) in use_templates.items()}

my_char = rpgCharacter.rpgCharacter(args.Name)

raw_stats = statsGenerators.generate_avg_stats(10, 12, 40, 60)

final_stats = templates.distribute_values(coreRules.attribute_display_order, raw_stats, attribute_templates.values())
my_char.set_attributes(final_stats)

raw_psych = statsGenerators.generate_avg_stats(10, 10)
final_psych = templates.distribute_values(coreRules.psych_display_order, raw_psych, pysch_templates.values())

my_char.set_psych(final_psych)

my_char.set_race(raceSettings)

my_char.dump_character()



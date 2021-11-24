import yaml
import os
import pprint as pp
import apps.modules.templates as templates

race_directory = os.path.join( 'apps', 'data', 'races')

race_definitions = templates.read_race_templates( race_directory)

# for rfile in os.listdir(race_directory):
#     with open(os.path.join(race_directory, rfile), 'r') as stream:
#         try:
#             this_file = yaml.safe_load(stream)
#             for r in this_file["race"]:
#                 # ``print (r["name"])
#                 race_definitions[ r["name"]] = r
#         except yaml.YAMLError as exc:
#             print(exc)

pp.pprint(race_definitions)

tempates_directory = os.path.join( 'apps', 'data', 'templates')

template_definitions = dict()

for tfile in os.listdir(tempates_directory):
    with open(os.path.join(tempates_directory, tfile), 'r') as stream:
        try:
            this_file = yaml.safe_load(stream)
            for r in this_file:
                template_definitions[ r["Template"]] = r
        except yaml.YAMLError as exc:
            print(exc)


pp.pprint(template_definitions)
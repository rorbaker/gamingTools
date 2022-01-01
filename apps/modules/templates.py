import yaml
import os
from typing import Counter

import modules.dice as dice
import pprint as pp

def read_race_templates(source_directory):
  race_definitions = dict()

  for rfile in os.listdir(source_directory):
      with open(os.path.join(source_directory, rfile), 'r') as stream:
          try:
              this_file = yaml.safe_load(stream)
              for r in this_file["race"]:
                  race_definitions[ r["name"]] = r
          except yaml.YAMLError as exc:
              print(exc)
  return race_definitions

def read_templates(source_directory):
  template_definitions = dict()

  for tfile in os.listdir(source_directory):
    with open(os.path.join(source_directory, tfile), 'r') as stream:
        try:
            this_file = yaml.safe_load(stream)
            for r in this_file:
                template_definitions[ r["Template"]] = r
        except yaml.YAMLError as exc:
            print(exc)

  return template_definitions

              

def apply_stats_templates(stat_names, raw_stats, stat_templates):
    
    stat_order = [dice.get_avg_result( 1, 100, False) for c in range(len(stat_names))]
    order_stats =dict(zip(stat_names, stat_order))

    for _, t in stat_templates.items():
        attribute_mods = t.get("Attributes")
        order_stats =dict( Counter(order_stats) + Counter(attribute_mods) )

    
    # pp.pprint(order_stats)

    order_stats= sorted(order_stats.items(), key=lambda x:x[1], reverse=True)

    return dict([(k, s) for (k, v), s in zip(order_stats, raw_stats)])


def distribute_values(names, raw_values, templates):
    weighted_names = created_weighted_list(names)

    ordered_weighted_names = apply_templates(weighted_names, templates)

    ## pp.pprint(ordered_weighted_names)

    return assign_weighted_values(ordered_weighted_names, raw_values)

## given a list of items, return a dictionary of item,weight pairs
def created_weighted_list(a_list):
  alpha_list = a_list
  alpha_list.sort
  weights = dice.roll_dice(len(alpha_list), 100)
  return dict(zip(alpha_list, weights))

## apply 0 to many templates to the weights
def apply_templates(weighted_list, templates):
  for t in templates:
      weighted_list =dict( Counter(weighted_list) + Counter(t) )

  return sorted(weighted_list.items(), key=lambda x:x[1], reverse=True)

## corelate a weighted list with sorted values
def assign_weighted_values(weighted_list, ordered_values):
  return dict([(k,s) for (k,v),s in zip (weighted_list, ordered_values)])





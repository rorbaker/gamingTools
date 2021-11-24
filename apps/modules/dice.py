"""
muodule with various functions to generate random dice rolls and quantify the resutls.
"""

from math import ceil, floor
import random
import re


default_target = 7
default_crit_threshold = 10
default_glitch_threshold = 1


def roll_dice(num_dice, num_sides):
    """generate a raw set with num_dice elements of random numbers between 1 and num_sides (inclusive)."""
    raw_dice = [random.SystemRandom().randrange(1, num_sides+1) for i in range(num_dice)]
    return raw_dice

def get_simple_result(num_dice, num_sides):
    """"""
    return sum( roll_dice(num_dice, num_sides))

def get_avg_result(num_dice, num_sides, roundup = True ):     
    return ceil(sum( roll_dice(num_dice, num_sides)) / num_dice) if roundup else floor(sum( roll_dice(num_dice, num_sides)) / num_dice)

def get_dice_pool( num_dice, num_sides, target=7, glitch=1, crit=10):
    pool = roll_dice(num_dice, num_sides)     
    successes =  sum( map(lambda x : x >= target, pool) )
    glitches =  sum( map(lambda x : x <= glitch, pool) )
    crits =  sum( map(lambda x : x >= crit, pool) )
    return successes, pool, glitches, crits

def get_parsed_dice_pool_result(parse_groups):    
    if parse_groups[1].casefold() == 'p'.casefold():
        num_dice = 1 if not parse_groups[2] else int(parse_groups[2])
        num_sides = 10
    else:
        num_dice = 1 if not parse_groups[0] else int(parse_groups[0])
        num_sides = 10 if not parse_groups[2] else int(parse_groups[2])

    t = extract_arg('t', parse_groups[3], default_target)
    c = extract_arg('c', parse_groups[3], default_crit_threshold)
    g = extract_arg('g', parse_groups[3], default_glitch_threshold)

    #return 'pool', num_dice, num_sides, t, c, g
    return get_dice_pool(num_dice, num_sides, t, g, c)[0]


def get_parsed_dice_simple_result(parse_groups):
    num_dice = 1 if not parse_groups[0] else int(parse_groups[0])
    num_sides = 10 if not parse_groups[2] else int(parse_groups[2])
    exp = parse_groups[3]
    roll_result = get_simple_result(num_dice, num_sides)
    eval_str = str(roll_result) + exp
    return eval(eval_str)

def extract_arg(arg_char, args_string, default_value):    
    has_arg = re.search(f"(\s*[{arg_char.lower()}|{arg_char.upper()}]\s*)([0-9]*)", args_string)
    if has_arg:
        return int(has_arg.groups()[1])
    
    return default_value


def get_parsed_dice_result(dice_str):    
    x = re.search('^\s*([0-9]*)\s*([pPdD])\s*([0-9]*)(.*)', dice_str)
    if not x:
        raise ValueError(f'Dice string is not comprehended "{dice_str}"')

    x = x.groups()
    t = extract_arg('t', x[3], -10)
    if x[1].casefold() == 'p'.casefold() or t > 0:
        return get_parsed_dice_pool_result(x)

    return get_parsed_dice_simple_result(x)

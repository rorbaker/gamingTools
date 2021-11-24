import modules.dice as dice

_max_tries = 100

def generate_avg_stats(num_stats, num_rolls=0, min_total=0, max_total=0, try_count=0):
    """generates avge stats that sum up between min_total and max_total (inclusive)"""
    to_roll = num_stats if num_rolls == 0 else num_rolls
    my_max = max_total if max_total > 0 else (num_rolls * 10) +1
    raw_stats = [generate_avg_stat() for c in range(to_roll)]
    raw_stats.sort(reverse=True)
    raw_stats = raw_stats[:10]
    
    if sum(raw_stats) >= min_total and sum(raw_stats) <= my_max:
        return raw_stats

    # print(f'total = {sum(raw_stats)} ({try_count+1} of {_max_tries})')

    if try_count +1 >= _max_tries:
        raise RecursionError

    return generate_avg_stats(num_stats, num_rolls, min_total, max_total, try_count+1)
    

def generate_avg_stat():
    return dice.get_avg_result( 2, 8, False)


def generate_d8_stat():
    return dice.get_simple_result(1, 8)


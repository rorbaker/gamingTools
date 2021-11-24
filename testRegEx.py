import apps.modules.dice as dice

sample_dice_str = ('1d6'
,'1 d 6'
,'2D6'
,'d10'
,'8d4     +3'
,' d100+1'
,'d100 -2'
,'7d10 t7'
,'7d10 t6 c9'
,' 7d10 t8 g2'
,' 7d10 t8 c9 g2'
,' 7d10 t8 g2 c10'
,' 7d10 c9 g2 t6'
,' 7d4 t2 g1 c4'
,'8d6 c5 t6'
,'7d10 t7 +100'
,'2d1 * (13 /2) '
,'2d10 / 2'
,' p1 3 t6 c9'
,'p 6 t11 g2'
,' P6t11g2'
,'P12 t7'
,'p8'
,'P 17'
,' P3 t2'
, 'sfasdf'
,'2D +1')

for s in sample_dice_str:
    #print(f'processing {s:20}')

    try:
        x = dice.get_parsed_dice_result(s)
    except ValueError as err:
        x ='parse error: ', err

    # ([t|T[ 0-9]*]*)([c|C[ 0-9]*]*)([g|G[ 0-9]*]*)

    #if is_dice_pool:
    #    num_dice = int(re.search('([pP]\s*)([0-9]*)', s).group(2))
    #else:
    #    num_dice = 100

    print(f'{s:20} {x}')



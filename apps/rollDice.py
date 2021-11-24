import modules.dice as dice
import statistics

#print(f"2d8 = {get_avg_result(2, 8, False)}")
#print(f"2d8 = {get_avg_result(2, 8, False)}")
#print(f"2d8 = {get_avg_result(2, 8, False)}")
#print(f"2d8 = {get_avg_result(2, 8, False)}")
#print(f"2d8 = {get_avg_result(2, 8, False)}")

#d = [get_avg_result(2, 8, False) for i in range(10000)]
#o, d , g, c = get_dice_pool( 7, 10, 7, 1, 10)

#print(f"dice rolled =   {len(d)}")
#print(f"successes =     {o}")
#print(f"glitches =      {g}")
#print(f"crits =         {c}")

#d2 = [get_dice_pool( 10, 10, 6, 1, 9) for i in range(1000)]
#d2_successes = [r[0] for r in d2]
#d2_glitches = [r[2] for r in d2]
#d2_crits = [r[3] for r in d2]
#print(f"dice rolled = {10}  successes={statistics.median(d2_successes)} ~{statistics.stdev(d2_successes):.2f} glitches={statistics.median(d2_glitches)} ~{statistics.stdev(d2_glitches):.2f} crits={statistics.median(d2_crits)} ~{statistics.stdev(d2_crits):.2f}")


#header
print(f"Desc, Dice, Target, CritTgt, successes, successMedian ,successStdDev ,glitches,glitchMedian ,glitchStdDev ,crits,critMedian ,critStdDev")

for i in range(7, 12):
     for j in range( 7, 8):
          for k in range (10, 9 , -1):
               rd = None
               dr = [dice.get_dice_pool( i, 10, j, 1, k) for c in range(10)]
               dr_successes = [r[0] for r in dr]
               dr_glitches = [r[2] for r in dr]
               dr_crits = [r[3] for r in dr]

               print(f"{i:2d}d10 t{j:2d} c{k:2d}, {i:2d}, {j:2d}, {k:2d}, successes,{statistics.median(dr_successes)},{statistics.stdev(dr_successes):.2f} ,glitches,{statistics.median(dr_glitches)} ,{statistics.stdev(dr_glitches):.2f} ,crits,{statistics.median(dr_crits)} ,{statistics.stdev(dr_crits):.2f}")



# d = roll_dice(3, 10)
#print(f"zeros's =     {d.count(0)} ({d.count(0)/len(d) * 100:.2f})")
#print(f"one's =       {d.count(1)} ({d.count(1)/len(d) * 100:.2f})")
#print(f"two's =       {d.count(2)} ({d.count(2)/len(d) * 100:.2f})")
#print(f"three's =     {d.count(3)} ({d.count(3)/len(d) * 100:.2f})")
#print(f"four's =      {d.count(4)} ({d.count(4)/len(d) * 100:.2f})")
#print(f"five's =      {d.count(5)} ({d.count(5)/len(d) * 100:.2f})")
#print(f"six's =       {d.count(6)} ({d.count(6)/len(d) * 100:.2f})")
#print(f"sevens's =    {d.count(7)} ({d.count(7)/len(d) * 100:.2f})")
#print(f"eights's =    {d.count(8)} ({d.count(8)/len(d) * 100:.2f})")
#print(f"nines's =     {d.count(9)} ({d.count(9)/len(d) * 100:.2f})")
#print(f"tens's =      {d.count(10)} ({d.count(10)/len(d) * 100:.2f})")

#print(f"elevens's =   {d.count(11)} ({d.count(11)/len(d) * 100:.2f})")
#print(f"twelves's =   {d.count(12)} ({d.count(12)/len(d) * 100:.2f})")
#print(f"thirteens's = {d.count(13)} ({d.count(13)/len(d) * 100:.2f})")
#print(f"fourteens's = {d.count(14)} ({d.count(14)/len(d) * 100:.2f})")
#print(f"fifteens's =  {d.count(15)} ({d.count(15)/len(d) * 100:.2f})")
#print(f"sixteens's =  {d.count(16)} ({d.count(16)/len(d) * 100:.2f})")
#print(f"seventeens's ={d.count(17)} ({d.count(17)/len(d) * 100:.2f})")
#print(f"eighteens's = {d.count(18)} ({d.count(18)/len(d) * 100:.2f})")
#print(f"nineteens's = {d.count(19)} ({d.count(19)/len(d) * 100:.2f})")
#print(f"twenty's =    {d.count(20)} ({d.count(20)/len(d) * 100:.2f})")








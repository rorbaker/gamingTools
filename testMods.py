from operator import mod
import apps.modules.dice as dice
import pprint as pp
import re

sample_mods = [
  ( 1, 'x')
  ,(1,'1')
  ,(7, 10) 
  ,(2, '2')
  ,(20 , '=3d6')
  ,(0 , '+3d6')
  ,(0 , '-3d6')
  ,(22 , ' - 12')
  ,(1 , '=16')
  ,(0 , 'this is not valid forumla')
 ,(0 , '')
 , (1, '3d10* 100')
 , (5, '/ 1d3 * 2')
 , (15, '=p6t5')
 , (5, '+p6t5')
 , (5, '-p6t5')
 , (5, '*p6t5')
 , (5, 'p6t5')
 , (5, '/p6t5')
]




for s in sample_mods:
  print('---  ')
  pp.pprint(f'testing mod: /{s}/') 
  y = s[1]
  x = dice.calc_mod(s[0], y)
  #    try:
  #       x = 
  #  except ValueError as err:
  #     x ='parse error: ', err

  print(f'          Original:{s[0]:5} Current:{x}')
  print('')


picture = [
  [0,0,0,1],
  [0,0,1,1],
  [0,1,1,1],
  [1,1,1,1]
]

for row in picture:
  for pixels in row:
    if pixels == 1:
      print('* ' , end='')
    else:
      print(' ' , end='' )
  print()





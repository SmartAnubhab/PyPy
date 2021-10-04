picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

tree = picture
picture2 = [
  [1,1,1,1],
  [1,0,0,1],
  [1,1,1,1],
  [1,0,0,1]
]

for row in tree:
  for pixels in row:
    if pixels == 1:
      print('*' , end='')
    else:
      print(' ' , end='' )
  print()
for i in range(3):
  print()


for row in picture2:
  for pixels in row:
    if pixels == 1:
      print('*' , end='')
    else:
      print(' ' , end='' )
  print()
for i in range(3):
  print()



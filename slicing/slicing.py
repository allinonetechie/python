import numpy as np
arr = np.array([[['123', 'Main Street', 'Anytown', 'USA'], ['456', 'Elm Avenue', 'Springfield', 'CA']], [['789', 'Oak Drive', 'Lakeside', 'NY'],['321', 'Pine Lane', 'Mountain View', 'TX']]])


#print(arr[0:1, 1:2, 1:3])


for x in arr:
  for y in x:
    for z in y:
      print(z)
    print('\n') 
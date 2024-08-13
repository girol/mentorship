"""
Consider an array/list of sheep where some sheep may be missing from their place.
 We need a function that counts the number of sheep present in the array (true means present).
"""
sheeplist = [True,True,False,False,False,True,False,True,False,True,False,False,True,False,True]
present = 0
missing = 0

for sheep in sheeplist:
    #print(sheep)
    if sheep == True:
       present += 1
    if sheep == False:
        missing +=1
print(present,'present sheep')
print(missing, 'missing sheep')

print(len(sheeplist),'total sheep')



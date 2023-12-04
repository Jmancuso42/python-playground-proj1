#Data Types/ Python Refresher


# Tuples ''''
'''
# Tuples arte immuntable, use parentheses. A comma is used for a single value, otherwise python doesn;'t intp correctly . Tuples are good to convey that 
you don't intend for the sequence to change, for anyone reading the code, as well as 
optimizations because the list is immutable.

'''

#converting tuples to dif types
''' You can pass Tuples into functions to return a different value. This does not modify the tuple, but it returns representations. it's useful if you need a 
mutable version of the tuple'''

eggs = ("cats","dogs",1,"2", "cheese")

print(list(eggs)) #prints a list rep of the eggs ref


#id()
'''Identity and id()

Id will show the numneroic memory address 


'''
eggId = id(eggs)
eggId3 = id(eggs[3])
print(eggId + '' + eggId3)









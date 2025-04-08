#Array native python methods :-
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
 
strings = ['a','b','c','d']

#append()	Adds an element at the end of the list
strings.append('e') # O(1)

#pop()	Removes the element at the last position
strings.pop() # O(1)

#insert()	Adds an element at the specified position
strings.insert(0,'x')    #O(n)

print(strings)







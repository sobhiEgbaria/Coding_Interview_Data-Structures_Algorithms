nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']
large = ['nemo' for i in range(100000)]

def find_nemo(array):
     for i in range(0,len(array)): #O(n)
        if array[i] == 'nemo': 
            print("Found Nemo!!")

find_nemo(nemo)
find_nemo(everyone)
find_nemo(large)

#the find_nemo function can be said to be of O(n) or Linear Time Complexity.

def printNumber(n):
    for i in range(n): # O(n)
        if i%2 == 0: 
            print(i)

printNumber(10)
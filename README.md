R's paste() function for Python.  
Join lists together pairwise, allowing for unequal length.  
It accept two additional arguments:  
- recycle: wether to recycle the shorter list's elements.  
    default to True: equivalent to R's paste() function, using recycling rules, recyle shorter lists elements.  
    if False, paste together without recycling.  
- sep: a string to concatenate list elements, default to empty string "".  

# Some examples:  
`a = [1, 2, 3, 4, 5]`  
`b = ["a", "b", "c"]`  
`c = ["x"]`  
`d = []`  

`print(paste(a, b, sep="-"))`  
['1-a', '2-b', '3-c', '4-a', '5-b']  

`print(paste(a, b, sep="-", recycle=False))`  
['1-a', '2-b', '3-c', 4, 5]  

`print(paste(a, b, c, sep="-"))`  
['1-a-x', '2-b-x', '3-c-x', '4-a-x', '5-b-x']  

`print(paste(a, b, c, sep="-", recycle=False))`  
['1-a-x', '2-b', '3-c', 4, 5]  

`# with empty list`  
`print(paste(a, b, d, sep="-"))`  
['1-a', '2-b', '3-c', '4-a', '5-b']  

`print(paste(a, b, d, sep="-", recycle=False))`  
['1-a', '2-b', '3-c', 4, 5]

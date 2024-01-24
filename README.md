Join lists together pairwise. It's equivalent to R's paste() function, using recycling rules for unequal length of lists.  
It accept two additional arguments:  
    - sep: a string to concatenate list elements, default to empty string "".  
    - recycle: wether to recycle the shorter list's elements, default to True, equivalent to R's paste() function.  

# Some examples:  
`a = [1, 2, 3, 4, 5]`  
`b = ["a", "b", "c"]`  

`print(paste(a, b, sep="-"))`  
['1-a', '2-b', '3-c', '4-a', '5-b']  

`print(paste(a, b, sep="-", recycle=False))`  
['1-a', '2-b', '3-c', 4, 5]  

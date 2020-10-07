""" 
Write a Python function called counts that takes a list 
as input and returns a dictionary of unique items in 
the list as keys and the number of times each item 
appears as values
"""

# sample list as suggested in task question
l = ['A', 'A', 'B', 'C', 'A']

# count function adds list items to dictionary
def count(lst):
    d = {}
    # iterate through list items and add to dict d
    for item in lst:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d

# call function and print to console
print(count(l))


# references:
# https://stackoverflow.com/questions/30208044/how-to-add-list-elements-into-dictionary
# fdaTasks2020
## Task 1
Write a Python function called `counts` that takes a list as input and returns a dictionary of unique items in the list as keys and the number of times each item appears as values
* Following a quick Google search, I found a [discussion](https://stackoverflow.com/questions/30208044/how-to-add-list-elements-into-dictionary) on stackoverflow.com which was useful in building the task program.
* Inside the function the `for` loop iterates through the list passed as an argument, adding each item to the dictionary as a key. The corresponding value is incremented by 1 if the same item is added throughout the iteration process.
```python
def counts(lst):
    d = {}
    # iterate through list items and add to dict d
    for item in lst:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d
```

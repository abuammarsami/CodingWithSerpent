some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dups = []
uniq = []

for item in some_list:
    if item not in uniq:
        uniq.append(item)
    else:
        dups.append(item)
uniq.sort()
dups.sort()

print(dups)
print(uniq)


"""
Goal:
Accepts a list of items a returns a new list with duplicates removed.
"""

def remove_dups(some_list):
    """
    Accepts a list of items a returns a new list with duplicates removed.
    """
    dups = []
    uniq = []
    for item in some_list:
        if item not in uniq:
            uniq.append(item)
    return uniq

print(remove_dups(some_list))

"""
Now try to remove the dups using a comprehension. Create a list of unique items. Create a list of duplicates items. 
Return only the unique list (no duplicates). 
Suggestion, you may need to use a method for a list here. 
See Python documentation for lists locally installed or online. (use ctrl+q)
"""

new_list_unique = list(set(some_list))

dup_list = list(set([item for item in some_list if some_list.count(item) > 1]))


print('New list without dups: ', new_list_unique)
print('Looks like a bug in Spyder with variable name lookup, both new_list_unique and dup_list were highlighted')
print('dups:', dup_list)



def dictdiff(first, second):
    output = {} #define an empty new dictionary
    all_keys = first.keys() | second.keys() #create a new set with all keys from first, second
    print (all_keys)
    for key in all_keys:

        if first.get(key) != second.get(key): #get retrieves the value of the key
            output[key] = [first.get(key), second.get(key)]

        return output

#set up two dictionaries
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'd': 4}

print (dictdiff(d1, d2))







def spell(*args):
    my_dict = {i[0].lower(): 0 for i in args}
    #my_dict = {i[0].lower(): len(i) for i in args if len(i) > my_dict[i[0].lower()]}
    for i in args:
        if (my_dict[i[0].lower()]) < len(i):
            my_dict[i[0].lower()] = len(i)

    return my_dict

words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
with open('files.txt', 'r', encoding='utf-8') as file:
    dct = {}
    names = []
    sizes = []
    names_of_size = []
    for i in file.readlines():
        name, size, name_of_size = i.split()
        dct[name] = [size, name_of_size]
sort = (sorted(dct.items(), key=lambda x: x[0].rsplit('.', 1)[1]))
dct = dict(sort)
temp = list(dct)[0]
print(dct)
list_type_of_size = ['B', 'KB', 'MB', 'GB']
inx_type = 0
for key, value in dct.items():
    if list_type_of_size.index(value[1]) > inx_type:
        inx_type = list_type_of_size.index(value[1])



    #if value[1] == 'GB':
        #value[0] = value[0] * 1073741824
    #elif value[1] == 'MB':
       # value[0] = value[0] * 1048576
   # elif value[1] == 'MB':
       # value[0] = value[0] * 1048576
    #elif value[1] == 'KB':
        #value[0] = value[0] * 1024



    if key[key.index('.')::] not in temp:

        print('----------')
        print('Summary:', list_type_of_size[inx_type])
        print()
        print(key)
        inx_type = 0
    else:
        print(key)
    temp = key[key.index('.')::]

print('----------')
print('Summary:', list_type_of_size[inx_type])
        #mem += int(value[0])
#for i in range(len(names)):

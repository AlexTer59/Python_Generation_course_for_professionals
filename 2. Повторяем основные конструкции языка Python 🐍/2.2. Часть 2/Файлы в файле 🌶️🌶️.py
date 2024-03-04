UNITS = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3
    }

def to_bytes(size, size_type):
    return UNITS[size_type.replace('\n', '')] * int(size)


def to_true_size_type(size):
    size_step = 1024
    for unit in UNITS.keys():
        if size < size_step:
            return f'{round(size)} {unit}'
        if unit == 'GB':
            return f'{round(size)} GB'
        size /= size_step


with open('files.txt', 'r', encoding='utf-8') as file:
    files_dct = {}
    for i in file.readlines():
        name_and_type, size, size_type = i.split(' ')
        files_dct[name_and_type] = [size, size_type]
files_dct = dict(sorted(files_dct.items(), key=lambda x: x[0].rsplit('.', 1)[0]))
files_dct = dict(sorted(files_dct.items(), key=lambda x: x[0].rsplit('.', 1)[1]))
name_and_type = list(files_dct.keys())
summary = 0
for item in name_and_type:
    summary += to_bytes(*files_dct[item])
    try:
        if item.split('.')[1] != name_and_type[name_and_type.index(item) + 1].split('.')[1]:
            print(item)
            print(10 * '-')
            print(f'Summary: {to_true_size_type(summary)}')
            print()
            summary = 0
        else:
            print(item)
    except(IndexError):
        print(item)
        print(10 * '-')
        print(f'Summary: {to_true_size_type(summary)}')





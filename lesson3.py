inp_data = list()
tag = 'add'

while tag.lower() == 'add':
    name = input('Input Name: ')
    age = input('Input Age: ')

    inp_dict = {'name': name, 'age': age}
    inp_data.append(inp_dict)

    tag = input('Add or Stop: ')
print(inp_data)
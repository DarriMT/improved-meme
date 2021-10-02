def temp(file1,file2):
    for line in file1:
        y = make_tuple(line)
        print(y)
    for line in file2:
        x = list_of_tuples(line)
        print(x)
    x = list_of_tuples(file2)
    print(x)











































'''a_list = []
def x():   
    for elements in file_1:
        first_word = elements.split()
        name = first_word[0]
        for char in elements:
            if char.isdigit():
                a_list.append(int(char))
        my_tuple = name,a_list
    return my_tuple




def make_list(file):
    for line in file:
        a_list = []
        data = line.split()
        for line in data:
            if line.isdigit():
                a_list.append(int(line))
                new_list = a_list
        return new_list'''


'''
f = open("a1.txt","r")

e = open("a2.txt","r")





def get_name(file):
    for line in file:
        first_word = line.split()
        name = first_word[0]
        print(name)


def make_list(file):
    for line in file:
        a_list = []
        data = line.split()
        for line in data:
            if line.isdigit():
                a_list.append(int(line))
                new_list = a_list
        return new_list

print(make_list(f))       '''
f = open("a1.txt","r")

e = open("a2.txt","r")


def make_list_of_name_points_grade(file1,file2):
    '''calls multiple functions to get a list filled with tuples containing (name , list and grade)'''
    a_list = []
    for line in file1:
        x = sum_grades(make_list(line))
    for line in file2:
        y = sum_grades(make_list(line))
        name = get_name(line)
        points = make_list(line)
        grade = get_grade(y,x)
        resault = name, points, grade
        a_list.append(resault)
    print(a_list)
    return a_list

def get_grade(individual,total):
    grade = (individual / total)*10
    return grade

def get_name(line):
    '''returns a name/email adress from each line in a file'''
    temp = line.split()
    name = temp[0]
    return name

def make_list(line):
    '''Retruns a list of digits from each line in a file'''
    temp = line.split()
    a_list=[]
    for chr in temp:
        if chr.isdigit():
            a_list.append(int(chr))
    return a_list

def make_tuple(line):
    '''takes the name and list of digits and creates a tuple'''
    name = get_name(line)
    grade = make_list(line)
    my_tuple = name , grade
    return my_tuple

def list_of_tuples(file):
    '''Takes text file 2 as input, creates a list , 
    for each line in the file it creates a tuple 
    and appends it into the created list and returns it'''
    a_list = []
    for line in file:
        x = make_tuple(line)
        a_list.append(x)
    return a_list

def sum_grades(list):
    total_points = sum(list)
    return total_points


#f = input("Project file name: ")

#e = input("Students file name: ")

make_list_of_name_points_grade(f,e)



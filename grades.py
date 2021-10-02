#Fall sem opnar og les
#Fall sem reiknar út vægi verkefna
#Fall sem reiknar heildar stig nemanda
#Fall sem tekur skrá 2 og skilar lista af túplum - einn stór listi , tölur ennþá í lista netfang og tölur í einni túplu
#fall fyrir lista sem inniheldur netfang , stigafjölda og meðaleinkunn í einni túplu fyrir sig
#fall sem prentar formatted niðurstöður

def main():
    pass
    
def open_file(file):
    '''Opens a file , and returns it , if it exists'''
    file_contents = open(file,"r")
    #print(file_contents.read())
    return file_contents

def tuple_1(file):
    '''Creates a tuple for the first file and returns it'''
    a_list = []
    for elements in file:
        first_word = elements.split()
        name = first_word[0]
        for char in elements:
            if char.isdigit():
                a_list.append(int(char))
        my_tuple = name,a_list
    return my_tuple
    

def make_tuple():
    pass



if __name__ == "__main__":
    main()
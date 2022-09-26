#Funciones de orden superior

#Recibo como parametro otra funcion


# Filter
    #my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    #odd = [i for i in my_list if i % 2 != 0]
    #print(odd)
my_list = [1, 4, 5, 6, 9, 13, 19, 21]

#list(filter(funcion o funcion anonima, iterable que se puede recorrer))
odd = list(filter(lambda x: x%2 != 0, my_list))

print(odd)
#[1, 5, 9, 13, 19, 21]



#Map
my_list_dos = [1, 2, 3, 4, 5]

    #odd_dos =     [i**2 for i in my_list_dos]
squares = list(map(lambda x: x**2, my_list_dos))

print(squares)

#[1, 4, 9, 16, 25]


#Reduce

#my_list_tres = [2, 2, 2, 2]
#all_multiplied = 1
#for i in my_list_tres:
    #all_multiplied = all_multiplied * i
#print(all_multiplied)
#32

from functools import reduce

my_list_tres = [2, 2, 2, 2]
all_multiplied = reduce(lambda a, b: a * b, my_list_tres)
print(all_multiplied)
#32



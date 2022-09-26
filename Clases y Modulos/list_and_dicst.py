def run():
    
    #Forma Normal de una list/dicc
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {"firtsname":"Facundo","lastname":"Garcia"}

    #Lista que contiene diccionarios
    super_list = [
        {"firtsname":"Facundo","lastname":"Garcia"},
        {"firtsname":"Facundo","lastname":"Garcia"},
        {"firtsname":"Facundo","lastname":"Garcia"},
        {"firtsname":"Facundo","lastname":"Garcia"},
    ]

    #Diccionario que contiene listas
    super_dict = {
        "natural_numbers" : [1, 2, 3, 4, 5],
        "integer_numbers" : [-1, -2, -3 , 0, 1, 2],
        "floating_nums" : [1.1, 2.3, 4,5]
    }

   #Uso de items para recorrer un dict/list
    for key, value in super_dict.items():
        print(key, "-", value)

   

if __name__ == '__main__':
    run()
def run():

    #{key:value for value in iterable if condition} Muestra las raices cuadradas 
    dict_compre = {i:i**0.5 for i in range(1,1001)}
    print(dict_compre)


if __name__ == '__main__':
    run()
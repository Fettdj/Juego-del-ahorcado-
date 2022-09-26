def run():

    #{key:value for value in iterable if condition}
    dict_compre = {i:i**3 for i in range(1,101) if i % 3 != 0}
    print(dict_compre)


if __name__ == '__main__':
    run()
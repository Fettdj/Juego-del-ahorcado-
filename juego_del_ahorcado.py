
def read(letra):
    if type(letra) != str:
        raise ValueError("Ingrese solo letras")

    palabras = {}
    with open("./data.txt", "w", encoding="utf-8" ) as f:
        for line in f:
            palabras.append(line)
        pala_mod = palabras.enumerate()
        with open("./modific.txt", "a", encoding="utf-8") as e:
            for modi in pala_mod:
                e.write(pala_mod)
                e.write("\n")
            
def run():
    try:
        letra = str(input("Ingresa una letra:"))
        read(letra)
    except ValueError as ve:
        print(ve)
        return False
 



if __name__ == '__main__':
    run()
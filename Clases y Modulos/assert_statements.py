
def divisors(num):
    try:
        if num < 0:
            raise ValueError("Ingrese un numero positivo")
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False



def run():
    num = input("Ingrese un numero: ")
    #Afirmacion con Python assert <condicion>, <mensaje>
        #num.isnumeric() devuelve un True o False si es numero
    assert num.isnumeric() and int(num)>0, "Debes ingresar solo numeros positivos"
    #assert , "Debes ingresar un numero positivo"
    print(divisors(int(num)))
    print("Termino el programa")

if __name__ == '__main__':
    run()


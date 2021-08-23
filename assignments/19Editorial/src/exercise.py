def main():
    #escribe tu código abajo de esta línea
    import math
num_pal= int(input('Dame el número de palabras:'))

if num_pal >0:
    x=num_pal/475
    y=math.ceil(x)
    print(y)
    semi_t= y*60
    dis= semi_t*0.1
    total= semi_t - dis
    print('El costo de la publicación es', total)

else: print('número no valido')

if __name__ == '__main__':
    main()

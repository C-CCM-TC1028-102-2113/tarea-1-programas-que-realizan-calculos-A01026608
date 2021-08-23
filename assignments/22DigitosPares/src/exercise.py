def main():
    #escribe tu código abajo de esta línea
    num= input('Dame un número')
    x=0
    if int(num[0])%2 ==0:
        x=x+1
    else: x=x+0
    if int(num[1])%2 ==0:
        x=x+1
    else: x=x+0
    if int(num[2])%2 ==0:
        x=x+1
    else: x=x+0
    if int(num[3])%2 ==0:
        x=x+1
    else: x=x+0
    
    print('El numero de dígitos pares son:',x)

if __name__ == '__main__':
    main()

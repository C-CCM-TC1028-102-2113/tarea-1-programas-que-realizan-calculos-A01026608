def main():
    #escribe tu código abajo de esta línea
   nuevos= int(input('Cantidad de juejos nuevos:'))
    viejo= int(input('Cantidad de juegos viejos:'))
    
    n= 1000
    v= 350
    
    a= nuevos*n
    b= viejo*v
    
    costo_f= a+b
    
    print('El total de su compra es:', costo_f)


if __name__ == '__main__':
    main()

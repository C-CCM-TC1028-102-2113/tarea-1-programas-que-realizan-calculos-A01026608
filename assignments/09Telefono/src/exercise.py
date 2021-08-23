def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    mensaje= int(input('Dame el número de mensajes:'))
    megas= float(input('Dame el número de megas:'))
    minutos= int(input('Dame el número de minutos:'))
    
    costo= 0.8
    a= mensaje* costo
    b= megas* costo
    c= minutos* costo
    
    final= a+b+c
    
    print('El costo mensual es:', final)

if __name__ == '__main__':
    main()

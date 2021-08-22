def main():
    #escribe tu código abajo de esta línea
    minu= float(input('Dame los minutos:'))
    sec= 60
    tiempo= minu*sec

    car= 5.7
    reco= car*tiempo

    conve= reco /10

    print('Centímentros recorridos:', conve)
    
if __name__ == '__main__':
    main()

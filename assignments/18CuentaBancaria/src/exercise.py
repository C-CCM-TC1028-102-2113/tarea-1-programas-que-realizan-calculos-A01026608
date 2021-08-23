def main():
    #escribe tu código abajo de esta línea
    saldo_ant= float(input('Dame el saldo del mes anterior:'))
    ingresos= float(input('Dame los ingreos:'))
    egresos= float(input('Dame los egresos:'))
    cheque= int(input('Dame el número de cheque:'))
    
    ch= 13
    costo_ch= ch * cheque
    
    saldo_m= saldo_ant + ingresos - egresos - costo_ch
    tasa= saldo_m*0.075
    saldo_final= saldo_m - tasa
    
    print('El saldo final de la cuenta es:', saldo_final)
if __name__ == '__main__':
    main()

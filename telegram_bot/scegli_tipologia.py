def scegli_tipologia()
    print(" 1 : Chiese \n 2 : Monumenti \n 3 : Musei \n 4 : torna indietro")
    num = int(input("Scegliere funzione: "))
    if num == 1:
        scegli_chiesa()
    elif num == 2:
        scegli_monumento()
    elif num == 3:
        scegli_museo()
    elif num == 4:
        return


scegli_tipologia()
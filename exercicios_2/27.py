def loja_frutas():

    kgbuy = input("Coloque quantos KG gostaria de comprar: ")

    if int(kgbuy) <= 5:
        morango = int(kgbuy) * 2.5 
        maca = int(kgbuy) * 1.8
        if int(kgbuy) > 8 or maca > 25 or morango > 25:
            desc10ma = maca * 0.10
            desc10mo = morango * 0.10
            morango = morango - desc10mo
            maca = maca - desc10ma
    elif int(kgbuy) > 5:
        morango = int(kgbuy) * 2.2
        maca = int(kgbuy) * 1.5
        if int(kgbuy) > 8 or maca > 25 or morango > 25:
            desc10ma = maca * 0.10
            desc10mo = morango * 0.10
            morango = morango - desc10mo
            maca = maca - desc10ma

    print("Morango: R$" + str(morango))
    print("Maça: R$" + str(maca))


loja_frutas()



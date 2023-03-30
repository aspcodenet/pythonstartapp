from random import randint
def gissaEttTal():
    talet =  randint(1,100)    

    while True:
        guess = input("Gissning:")
        if guess == talet:
            return

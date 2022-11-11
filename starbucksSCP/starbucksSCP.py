"""
    Programmer: Paddock
    Program: Keeping track of Starbucks SCP
    Created on: 10-21-2022 9:00 AM CST
    Last Changed: 10-21-2022 9:00 AM CST
    Version: Python 3.10
"""

def espresso(quantity, coffee, water):

    """
    :param quantity: number of orders of espresso
    :param coffee: parameter keeping track of total coffee powder
    :param water: parameter keeping track of total water
    :return: updated resources after serving quantity*espresso servings
    """
    coffee = coffee - (quantity * 8)
    water = water - (quantity * 1.5)

def americano(quantity, size, coffee, water):
    """
    :Americano mix: 1 shot of espresso and 3 oz. of hot water
    :param quantity: number of orders of americano
    :param size: serving size (tall / grande / venti / trenta)
    :param coffee: parameter keeping track of total coffee powder
    :param water: parameter keeping track of total water
    :return: updated resources after serving quantity * size * americano servings
    """
    coffee = coffee - quantity*((size/4)*1)
    water = water - quantity*((size/4)*3)
    print("coffee powder within coffee function is ", coffee)

def cappuccino(quantity, size, coffee, milk):
    """
    :Cappuccino mix: 1 shot of espresso, 2 oz. steamed milk, and 2 oz. foamed milk
    :param quantity: number of order of cappuccino
    :param size: serving size (tall / grande / venti / trenta)
    :param coffee: parameter keeping track of total coffee powder
    :param milk: parameter keeping track of total milk
    :return: updated resources after serving quantity * size * cappuccino servings
    """
    coffee = coffee - quantity*((size/4)*1)
    milk = milk - quantity*((size/4)*4)

def mocha(quantity, size, coffee, milk, chocolate):
    """
    :Mocha mix: 1 shot of espresso, 2 oz. chocolate, 2 oz. steamed milk, and 2 oz. milk foam
    :param quantity: number of order of mocha
    :param size: serving size (tall / grande / venti / trenta)
    :param coffee: parameter keeping track of total coffee powder
    :param milk: parameter keeping track of total milk
    :param chocolate: parameter keeping track of total chocolate
    :return: updated resources after serving quantity * size * mocha servings
    """
    coffee = coffee - quantity*((size/4)*1)
    milk = coffee - quantity*((size/4)*4)
    chocolate = chocolate - quantity*((size/4)*2)

def cortado(quantity, size, coffee, milk):
    """
    :Cortado mix: 1 shot of espresso, 2 oz. steamed milk
    :param quantity: number of order of cortado
    :param size: serving size (tall / grande / venti / trenta)
    :param coffee: parameter keeping track of total coffee powder
    :param milk: parameter keeping track of total milk
    :return: updated resources after serving quantity * size * cortado servings
    """
    coffee = coffee - quantity*((size/4)*1)
    milk = milk - quantity*((size/4)*2)

def macchiato(quantity, size, coffee, milk):
    """
    :Macchiato mix: 1 shot of espresso, 2 oz. milk foam
    :param quantity: number of order of macchiato
    :param size: serving size (tall / grande / venti / trenta)
    :param coffee: parameter keeping track of total coffee powder
    :param milk: parameter keeping track of total milk
    :return: updated resources after serving quantity * size * macchiato servings
    """
    coffee = coffee - quantity*((size/4)*1)
    milk = milk - quantity*((size/4)*2)

def affogato(quantity, size, coffee, iceCream):
    """
    :Affogato mix: q shot of espresso, 1 scoop of iceCream
    :param quantity: number of order of affogato
    :param size:
    :param coffee:
    :param iceCream:
    :return:
    """

print("Program to keep track of Starbucks supply chain")
print("Enter the quantities of the raw materials at the beginning of the day")

# taking the inputs for the raw materials at the beginning of the day

coffee = float(input("Enter the coffee quantity: \t"))
milk = float(input("Enter the milk quantity: \t"))
water = float(input("Enter the water quantity: \t"))
icecream = float(input("Enter the icecream quantity: \t"))
whisky = float(input("Enter the whisky quantity: \t"))
chocolate = (float(input("Enter the chocolate quantity: \t")))

# setting different service size values
tall = 12
grande = 16
venti = 24
trenta = 31

espresso(2, coffee, water)
americano(2, venti, coffee, water)
cappuccino(2, venti, coffee, milk)
mocha(2, venti, coffee, chocolate, milk)
cortado(2, venti, coffee, milk)

print("remaining supplies")
print("The leftover coffee powder is ", coffee)
print("The remaining water is ", water)
print("The remaining milk is", milk)
print("The remaining chocolate is", chocolate)
print("The remaining ice cream is", icecream)
print("The remaining whisky is", whisky)

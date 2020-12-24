#Aiden O'Connor
#Project idea form Intellij Academy, Coffee Maker

class Coffee:

    def __init__(self, water, milk, beans, cost):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cost = cost


class TypesOfCoffee:
    espresso = Coffee(250, 0, 16, 4)
    latte = Coffee(350, 75, 20, 7)
    cappuccino = Coffee(200, 100, 12, 6)


class Actions:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def checkResources(self, coffee):
        if self.water < coffee.water:
            print('Sorry, not enough water!')
            return
        elif self.milk < coffee.milk:
            print('Sorry, not enough milk!')
            return
        elif self.beans < coffee.beans:
            print('Sorry, not enough coffee beans!')
            return
        elif self.cups < 1:
            print('Sorry, not enough cups!')
            return
        print('I have enough resources, making you a coffee!')
        self.water -= coffee.water
        self.milk -= coffee.milk
        self.beans -= coffee.beans
        self.money += coffee.cost
        self.cups -= 1

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        my_buy = input()
        if my_buy == '1':
            self.checkResources(TypesOfCoffee.espresso)
        if my_buy == '2':
            self.checkResources(TypesOfCoffee.latte)
        if my_buy == '3':
            self.checkResources(TypesOfCoffee.cappuccino)
        else:
            pass

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.beans += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def remaining(self):
        print("The coffee machine has:")
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')


class CoffeeMachine:

    def __init__(self):
        self.my_action = Actions()
        self.order()

    def order(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit): ')
            action = input()
            if action == 'buy':
                self.my_action.buy()
            elif action == 'fill':
                self.my_action.fill()
            elif action == 'take':
                self.my_action.take()
            elif action == 'remaining':
                self.my_action.remaining()
            elif action == 'exit':
                break


coffee_machine = CoffeeMachine()

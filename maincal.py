import one
import two
import three
import four

add = 1
subtract = 2
multiply = 3
divide = 4
Quit = 5

def main():
    menu = 0
    while menu != Quit:
        display_menu()
        menu = int(input('Enter you menu: '))
        if menu == add:
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter last number: '))
            print('result: ',one.add(num1, num2))
        elif menu == subtract:
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter last number: '))
            print('result: ',two.subtract(num1, num2))
        elif menu == multiply:
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter last number: '))
            print('result: ', three.multiply(num1 , num2))
        elif menu == divide:
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter last number: '))
            print('result: ',four.divide(num1 , num2))
        elif menu == Quit:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')
def display_menu():
    print('-'*20)  
    print('       MENU')
    print('-'*20)
    print('1) add ')
    print('2) subtract')
    print('3) multiply')
    print('4) divide')
    print('5) Quit')
main()
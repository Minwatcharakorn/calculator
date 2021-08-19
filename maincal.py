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
    choice = 0
    while choice != Quit:
        display_menu()
        choice = int(input('Enter you choice: '))
        if choice == add:
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter last number: '))
            print('result: ',one.add(num1, num2))
        elif choice == subtract:
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter last number: '))
            print('result: ', \
                two.subtract(num1, num2))
        elif choice == multiply:
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter last number: '))
            print('result: ', three.multiply(num1 , num2))
        elif choice == divide:
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter last number: '))
            print('result: ', \
                four.divide(num1 , num2))
        elif choice == Quit:
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
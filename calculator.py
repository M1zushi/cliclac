import math

# Temporary loop. I swear I'll make it better after.
on = 0

while on == 0:
    print'\n\nOptions:'
    print ' 1. Add'
    print ' 2. Subtract'
    print ' 3. Multiply'
    print ' 4. Divide'
    # Temporarily there will only be the basic 4 operators
    print ' 0. Off'

    op = input('\nOperation(Num 0-4): ')

    if op == 1:
        num1 = int(input('First Value: '))
        num2 = int(input('Second Value: '))
        print('\n\n{} + {} = {}').format(num1, num2, num1 + num2)
        # For some reason when I use f'{var1}' it doesn't work so I have to use str.format

    elif op == 2:
        num1 = int(input('First Value: '))
        num2 = int(input('Second Value: '))
        print('\n\n{} - {} = {}').format(num1, num2, num1 - num2)

    elif op == 3:
        num1 = int(input('First Value: '))
        num2 = int(input('Second Value: '))
        print('\n\n{} * {} = {}').format(num1, num2, num1 * num2)

    elif op == 4:
        num1 = int(input('First Value: '))
        num2 = int(input('Second Value: '))
        print('\n\n{} / {} = {}').format(num1, num2, num1 / num2)

    elif op == 0:
        print('\nO F F')
        on += 1

else:
    print('\nProcess Terminated')

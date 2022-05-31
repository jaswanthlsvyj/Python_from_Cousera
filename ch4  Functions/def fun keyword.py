a = int(input("enter any in number:"))

b = str(input('enter any char:'))


def num(number):
    if(number < 0):
        print('number is less then zero')
    elif(number == 0):
        print('number is equal to zero')
    else:
        print('number is more than zero')


def string(char):
    if(char == 'A'):
        print('its a staring char')
    elif(char == 'Z'):
        print('its a ending char')
    else:
        print('its a char in middle')


num(a)
string(b)

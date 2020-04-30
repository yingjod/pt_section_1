def countit(F):
    '''

    transform from Fahrenheit to Celsius

    '''
    C=(F-32)*5/9
    print('Fahrenheit %.2f ---> Celsius %.2f '%(F,C))

if __name__ == '__main__':
    F = int(input())
    countit(F)
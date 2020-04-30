
def distance(v,a):
    '''

    count the minimum runway length

    '''

    length=v**2/2*a
    print('Minimum runway length is %.2f meters'%length)

if __name__ == '__main__':
    v, a = eval(input())
    distance(v,a)

import math

def areai(r):
    '''

    count the area of Pentagon

    '''
    s=(2*r)*math.sin(math.pi/5)
    area=(5/(4*math.tan(math.pi/5)))*(s**2)
    print('Area is %.2f'%area)

if __name__ == '__main__':
    r = eval(input())
    areai(r)
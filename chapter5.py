import math
def av(r,heigth):
    '''

    count area and volume of column

    '''
    area=math.pi*(r**2)
    volume=area*heigth
    print('area:%.2f , volume:%.2f'%(area,volume))

if __name__ == '__main__':
    r, heigth = eval(input())
    av(r, heigth)
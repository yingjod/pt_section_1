
def joiles(M,initialT,finalT):
    '''

    count the joiles

    '''
    Q=M*(finalT-initialT)*4184
    print('Q=%.2f'%Q)

if __name__ == '__main__':
    M, initialT, finalT = eval(input())
    joiles(M,initialT,finalT)
import sys
def moon_weight():
    print('당신의 현재 지구 몸무게 입력')
    a = float(sys.stdin.readline())
    print('매년 증가하는  당신의 몸무게 입력')
    b = float(sys.stdin.readline())
    print('연도 수')
    c = int(sys.stdin.readline())
    for i in range(1,c+1):
        a = a + b
        a = a * 0.168
        print('%s %s' % (i,a))
        

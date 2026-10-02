import sys
"""명령행 인자값 확인용 모듈"""
args = sys.argv[1:] #args[0]은 스크립트명 그 자체
print(f'현재 구동중인 프로그램은 : {sys.argv[0]}')
for x in args:
    print(x, end=' ')
else:
    print()

#sys 모듈
#명령 행(cmd창 - 명령프롬프트)에서 인수 전달하기

import sys

args = sys.argv[1:]
print(args)

for i in args :
    print(i)
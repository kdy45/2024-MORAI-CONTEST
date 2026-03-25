#!/usr/bin/env python3
#-*-coding:utf-8-*-

class Class_example: #1. class 이름 설정
    def __init__(self): #2. init 단 설정
        self.data = 0

        def func(self): #3. 함수 설정
            pass

def main(): #6. main() 함수 작성
    try:
        class_name = Class_example()
        class_name.func()
    except:
        pass

if __name__=="__main__":  #4.현재 구문을 작성함으로써, 현재 코드가 메인 코드임을 선언.
    main() #5. main() 함수 호출
    
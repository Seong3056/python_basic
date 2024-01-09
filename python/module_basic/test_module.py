PI = 3.141592

def number_input():
    output = input("숫자 입력 : ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

print("모듈의 __name__을 출력하기")
print(__name__)
print()
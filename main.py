## 함수 선언부
def add_func(n1, n2):
    return n1+n2

def subtract_func(n1, n2):
    return n1-n2

## 전역 변수부
num1, num2, res = 100, 200, 0

## 메인 코드부
add_res=add_func(num1, num2)
sub_res=subtract_func(num1, num2)
print("Addition : ", num1, "+", num2, "=", add_res)
print("Subtraction : ", num1, "-", num2, "=", sub_res)

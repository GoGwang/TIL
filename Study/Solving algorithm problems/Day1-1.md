# Day 2 If문

### Q1.
#### 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
``` bash
A, B =map(int,input().split())
if A>B:
    print(">")
elif A<B:
    print("<")
else:
    print("==")
```

### Q2.
#### 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
``` bash
A =int(input())
if A>=90:
    print("A")
elif A>=80:
    print("B")
elif A>=70:
    print("C")
elif A>=60:
    print("D")
else:
    print("F")
```

### Q3.
#### 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오. 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
``` bash
A =int(input())
if A%400 ==0 or A%4 ==0 and A%100 !=0:
    print("1")
else:
    print("0")
```

### Q4.
#### 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
``` bash
A = int(input())
B = int(input())
if A>0 and B>0:
    print("1")
elif A<0 and B>0:
    print("2")
elif A<0 and B<0:
    print("3")
else:
    print("4")
```

### Q5.
#### 45분 일찍 알람을 설정하는 프로그램을 작성하시오.
``` bash
H, M =map(int,input().split())
if H ==0:
    if M<45:
        H+=23
        M+=15
    else:
        M-=45
else:
    if M<45:
        H-=1
        M+=15
    else:
        M-=45
print(H, M)
```


# Day 1 입출력과 사칙연산

### Q1.
#### Hello World!를 출력하시오.
``` bash
print("Hello World!")
```

### Q2. 
#### 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력하시오.
``` bash
print("강한친구 대한육군")
print("강한친구 대한육군")
```

### Q3.
#### 예제와 같이 고양이를 출력하시오.
``` bash
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")
```

### Q4.
#### 예제와 같이 개를 출력하시오.
``` bash
print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")
```

### Q5.
#### 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
``` bash
A, B = map(int, input().split())
print(A+B)
```

### Q6.
#### 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
``` bash
A, B = map(int, input().split())
print(A-B)
```

### Q7.
#### 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
``` bash
A, B =map(int, input().split())
print(A*B)
```

### Q8.
#### 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
``` bash
A, B = map(int, input().split())
print(A/B)
```

### Q9.
#### 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
``` bash
A, B = map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
```

### Q10.
#### (A+B)%C는 ((A%C) + (B%C))%C 와 같을까? (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
#### 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
``` bash
A, B, C =map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
```

### Q11.
#### 주어진 숫자들의 곱셈을 자리 별로 각각 나타내어라
``` bash
A= int(input())
B=input()
print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))
```


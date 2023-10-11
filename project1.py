import numpy as np

# 0과 1을 임의로 (랜덤으로) 10^7개 생성하여, 배열 ‘data’에 저장한다.
data = np.random.randint(0,2,10**7)
x = list()

# 배열 ‘data’의 첫 30개 값은 무엇인가?
print("data")
for i in range(30):
    print("{}".format(data[i]), end=" ")
print()

for i in range(10**7):
    if data[i]==1:
        x.append(1)
    elif data[i]==0:
        x.append(-1)

# 배열 ‘x’의 첫 30개 값은 무엇인가?
print("x")
for i in range(30):
    print("{}".format(x[i]), end=" ")
print()

# 평균이 0이고, 표준 편차가 1인 Gaussian 분포를 따르는 잡음을 10^7개 생성하여, 배열 ‘n’에 저장한다.
n = np.round(np.random.normal(0, 1, 10**7), 4)

# 배열 ‘n’의 첫 30개 값은 무엇인가? 소수점 아래 4자리까지
print("n")
for i in range(30):
    print("{:.4f}".format(n[i]), end=" ")
print()

# 수신기가 받은 신호는 변조된 데이터와 잡음의 합으로 계산할 수 있다. 수신 신호를 배열 ‘r’에 저장한다.
r = list()
for i in range(10**7):
    r.append(n[i]+x[i])

# 배열 ‘r’의 첫 30개 값은 무엇인가? 소수점 아래 4자리까지
print("r")
for i in range(30):
    print("{:.4f}".format(r[i]), end=" ")
print()

# 수신 신호가 0보다 크거나 같으면 1, 0보다 작으면 0으로 결정하고, 그 결과를 배열 ‘y’에 저장한다.
y = list()
for i in range(10**7):
    if(r[i]>=0):
        y.append(1)
    else:
        y.append(0)

# 배열 ‘y’의 첫 30개 값은 무엇인가?
print("y")
for i in range(30):
    print("{}".format(y[i]), end=" ")
print()

# 수신기가 바르게 복조한 비트의 개수를 카운트하여, 배열 ‘check’에 저장한다.
check = list()
success = 0
for i in range(10**7):
    if(y[i]==data[i]):
        success+=1
    check.append(success)

# 배열 ‘check’의 첫 30개 값은 무엇인가?
print("check")
for i in range(30):
    print("{}".format(check[i]), end=" ")
print()

# 전체 10^7개 데이터 중, 수신기가 바르게 복조한 비트의 개수는 무엇인가?
print("올바른 개수 : ",success)

# 에러 확률은 무엇인가?
print("에러 확률 : {:.6f}".format((((10**7)-success)/(10**7))*100), "%")



#표준편차 0.1에서 2.9까지 에러확률
for index in np.arange(0.1, 3.0, 0.1):
    n = np.round(np.random.normal(0, index, 10**7), 4)

    r = list()
    for i in range(10**7):
        r.append(n[i]+x[i])

    y = list()
    for i in range(10**7):
        if(r[i]>=0):
            y.append(1)
        else:
            y.append(0)

    check = list()
    success = 0
    for i in range(10**7):
        if(y[i]==data[i]):
            success+=1
        check.append(success)
    
    print("{:.1f}에러 확률 : {:.6f}%".format(index, ((10**7)-success)/(10**7)*100))
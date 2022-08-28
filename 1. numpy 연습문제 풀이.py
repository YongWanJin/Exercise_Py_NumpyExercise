

# Q1. numpy를 np로 가져오고 버전 확인

import numpy as np
np.version.version


# Q2. 0에서 9까지의 숫자로 구성된 1D 배열 생성

result = np.arange(0, 10)
print(result)


# Q3. 모든 True의 3×3 numpy 배열 생성

result = np.full((3, 3), True)
print(result)


# Q4. 1D 배열에서 모든 홀수를 추출

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

result = arr[(arr%2)!=0]
print(result)


# Q5. 모든 홀수 arr를 -1 로 바꿉니다.

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

np.place(arr, arr%2==1, -1)
print(arr)


# Q6. arr의 모든 홀수를 변경하지 않고 -1로 바꿉니다
# ?? 문제 이해 불가

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# Q7. 1D 배열을 2행이 있는 2D 배열로 변환

result = np.arange(10).reshape(2, 5)
print(result)


# Q8. 두 개의 어레이를 수직으로 쌓기

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

result = np.vstack((a, b))
print(result)


# Q9. 두 개의 어레이를 수평으로 쌓기

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

result = np.hstack((a, b))
print(result)


# Q10. 하드코딩 없이 아래 입력 배열만 사용 출력과 같은 패턴을 만드시오

a = np.array([1,2,3])

idx = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2])
result = a[idx]

print(result)


# Q11. 두 파이썬 numpy 배열 사이의 공통 항목  출력

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

a_unq = np.unique(a)
b_unq = np.unique(b)
result = np.intersect1d(a_unq, b_unq)

print(result)


# Q12. 배열 a에서 b 배열에 있는 모든 항목을 제거합니다.

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

result = np.setdiff1d(a, b)
print(result)


# Q13. a, b두 배열의 요소가 일치하는 위치를 출력

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

result = np.where(a==b)

print(result[0])


# Q14. a배열에서  5에서 10 사이의 모든 항목을 에서 가져옵니다 

a = np.array([2, 6, 1, 9, 10, 3, 27])

result = a[(a>=5) & (a<=10)]

print(result)


# Q15. maxx두 개의 스칼라에서 작동하는 함수를
# 두 개의 배열에서 작동하도록 변환하시오

def pair_max(x, y) :
    
    return np.maximum(x, y)


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

result = pair_max(a,b)

print(result)


# Q16. 2d numpy 배열에서 배열의 1열과 2열을 바꿉니다

arr = np.arange(9).reshape(3,3)

arr_t = arr.T
arr_t_switch = np.vstack((arr_t[1], arr_t[0], arr_t[2]))
result = arr_t_switch.T

print(result)


# Q17. 2D 배열의 행을 뒤집습니다.

arr = np.arange(9).reshape(3,3)

result = np.vstack((arr[2], arr[1], arr[0]))

print(result)


# Q18. 2D 배열의 열을 뒤집습니다.

arr = np.arange(9).reshape(3,3)

arr_t = arr.T
arr_t_switch = np.vstack((arr_t[2], arr_t[1], arr_t[0]))
result = arr_t_switch.T

print(result)


# Q19. 5에서 10 사이의 임의의 십진수를 포함하는
# 5x3 모양의 2D 배열을 만듭니다.

result = np.random.randint(5, 11, 15).reshape(5, 3)

print(result)


# Q20. 5에서 10 사이의 임의의 부동 소수점을 포함하는
# 5x3 모양의  2D 배열 만듭니다.

result = np.random.uniform(5, 10, 15).reshape(5, 3)

print(result)


# Q21. numpy 배열의 소수점 이하 세 자리만 출력합니다.

rand_arr = np.random.random((5,3))

result = np.trunc(rand_arr*1000)/1000

print(result)

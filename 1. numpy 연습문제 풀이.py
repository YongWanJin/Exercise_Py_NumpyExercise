

# Q1. numpy를 np로 가져오고 버전 확인

import numpy as np
np.version.version


# Q2. 0에서 9까지의 숫자로 구성된 1D 배열 생성

a = np.arange(0, 10)
print(a)


# Q3. 모든 True의 3×3 numpy 배열 생성

a = np.full((3, 3), True)
print(a)
print(a.ndim)


# Q4. 1D 배열에서 모든 홀수를 추출??

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a = np.where(arr % 2 == 1)
print(a[0])


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


# Q11. 배열 a에서 b 배열에 있는 모든 항목을 제거합니다.

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])







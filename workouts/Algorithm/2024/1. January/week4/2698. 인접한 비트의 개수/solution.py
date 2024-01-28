# 길이가 n일 때 최대 k의 수는 n - 1
# 각 길이(2~n)를 0~k까지 수열의 개수를 누적시키며 결과를 얻을 수 있다.

# 예시) 이진수열 11100의 경우 두 1이 인접하여 나타나는 경우는 2회 있음
# n이 5이고 k가 2인 경우 조건을 충족하는 수열은 아래와 같음 (6개)
# 11100, 01110, 00111, 10111, 11101, 11011

# 최적 부분 구조
# - 작은 문제의 최적 해결법을 연속함으로써 큰 문제를 해결함
# 중복된 부분 문제
# - 동일한 작은 문제를 반복적으로 해결할 수 있는 경우에 해당


import sys
input = sys.stdin.readline

t = int(input())

# dp 초기화
# 길이가 j이고 인접 비트의 수가 i이며, 0 또는 1을 마지막으로 한 경우
dp = [[[0, 0] for _ in range(102)] for _ in range(102)]
dp[0][1] = [1, 1]

for i in range(101):
    for j in range(i+1, 101):
        # 길이가 j이고 인접한 비트 수가 i이고, 마지막 비트가 0인 경우
        # 길이가 j-1, 기존 마지막 수가 어떻든 0을 추가하면 됨 = 다 더함
        dp[i][j][0] = max(dp[i][j][0], dp[i][j-1][1] + dp[i][j-1][0])
        # 길이가 j이고 인접한 비트 수 i, 마지막 비트가 1인 경우
        # 길이 = j-1이고 인접한 비트 수가 i이며 마지막 비트가 0인 경우에 추가 가능
        dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-1][1] + dp[i][j-1][0])

# t회만큼 n, k를 입력받아서
for _ in range(t):
    n, k = map(int, input().split())
    # 해당하는 dp 배열의 합을 출력
    print(sum(dp[k][n]))
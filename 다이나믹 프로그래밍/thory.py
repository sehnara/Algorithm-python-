# Dynamic programming

# 1. 기본 생각
# 중복되는 연산을 줄이자
# => 메모리 공간을 좀 더 쓰더라도 연산 속도를 비약적으로 올릴 수 있다면 그렇게 하겠다.

# 2. 다이나믹 프로그래밍과 분할 정복의 차이
# : 분할 정복은 나눠지는 부분이 독립적인데, dp는 모두 연계가 된다.

# 3. 시간복잡도
# : O(N)

# 4. 문제 파악
# : 완전탐색으로 풀었을 때 시간초과 뜨면, 중복 여부를 확인
# : 재귀롤 풀어보고, 메모이제이션 기법을 적용할 수 있음 하자.

# 5. recursion 에러
# : setrecursionlimit();
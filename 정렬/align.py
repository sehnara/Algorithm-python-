from multiprocessing.dummy import Array


CARDS = [5,7,9,0,3,1,6,2,4,8]
# 1. 선택정렬(O(N^2))
# for i in range(len(CARDS)):
#     min_index = i
#     for j in range(i+1, len(CARDS)):
#         if CARDS[min_index] > CARDS[j]:
#             min_index = j
#     CARDS[i], CARDS[min_index] = CARDS[min_index], CARDS[i]
    
# print(CARDS)

# 2. 삽입정렬(O(N^2)) - 정렬이 이미 어느 정도 되어 있는 경우에 퀵정렬보다 강력할 수 있다.
# for i in range(1, len(CARDS)):
#     for j in range(i, 0, -1): # start부터 end+1까지 1씩 감소
#         if CARDS[j-1] > CARDS[j]:
#             CARDS[j], CARDS[j-1] = CARDS[j-1], CARDS[j]
#         else : # 앞은 이미 정렬되었다고 가정하기 때문에 더 볼 필요없다.
#             break
# print(CARDS)

# 3. 퀵정렬
# def quick_sort(array, start, end):
#     if start >= end :
#         return
#     pivot = start
#     left = start + 1
#     right = end 
#     while left <= end :
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1    
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else :
#             array[left], array[right] = array[right], array[left]
        
#     quick_sort(array, start, right-1)
#     quick_sort(array, right+1, end)

# quick_sort(CARDS, 0, len(CARDS)-1)
# print(CARDS)

# # 3-1. quick_sort() Nlog(N) but, O(N^2)in worst case
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
    
#     pivot = array[0]
#     tail = array[1:]
    
#     left_side = [x for x in tail if x<= pivot]
#     right_side = [x for x in tail if x> pivot]
    
#     return quick_sort(left_side)+[pivot]+ quick_sort(right_side)
# print(quick_sort(CARDS))
        
# 4. 계수 정렬 : 특정한 조건 부합시 사용, 매우 빠른 알고리즘
# [조건 1] 정수 형태 값만 취급
# [조건 2] 가장 큰 데이터와 가장 작은 데이터의 차이가 1000000 넘지 않을 때 효과적
# [결론] 일반적인 상황에서는 퀵정렬쓰고, 데이터 크기 한정되어 있으면서 데이터가 많이 중복되어 있으면 계수 정렬 고민

# ARRAY = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2] # O(N+K)
# count = [0] * (max(ARRAY)+1) # 이렇게 배열을 만들어주는게 포인트

# for i in range(len(ARRAY)):
#     count[ARRAY[i]] +=1

# for c in range(len(count)):
#     if count[c] :
#         for _ in range(count[c]):
#             print(c, end=" ")


# 5. 정렬 라이브러리 : 최악의 경우에도 Nlog(N) 보장
array = [('바나나',2),('사과',5),('당근',3)]
result = sorted(array, key=lambda a: a[1])     
print(result)   

#------------------------------------------------------------------------------------------
# STRATEGY
# 1. 일반적 상황 : sorted or sort
# 2. 데이터 범위 한정되어 있으며 더 빠르게 동작해야할 때 : 계수 정렬
#------------------------------------------------------------------------------------------
# 정렬 문제 유형
# 1. 정렬 라이브리로 풀 수 있는 문제
# 2. 정렬 알고리즘 원리에 대해 묻는 문제 : 선택 정렬, 삽입 정렬, 퀵 정렬 원리 
# 3. 더 빠른 정렬 : 계수 정렬이나 알고리즘의 구조적 개선 필요
    
    
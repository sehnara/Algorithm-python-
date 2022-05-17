#11:21~
from re import T
from xmlrpc.client import TRANSPORT_ERROR


N = int(input())
ARRAY = [int(input()) for _ in range(N)]
ARRAY.sort(reverse=True)

print(ARRAY)
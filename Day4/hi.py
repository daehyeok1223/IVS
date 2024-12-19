cnt = 0
arr = []
def INPUT():
    global arr
    numbers = list(map(int, input().split()))
    if len(numbers) == 6:
        arr = [numbers[:3], numbers[3:]]
def PROCESS():
    global cnt
    for i in arr:
        cnt += i
def OUTPUT():
    print(cnt)

INPUT()
OUTPUT()

        
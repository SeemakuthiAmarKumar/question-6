def toFindMisingNum(arr, n):
    zero_arr = [0] * (n+1)
    for i in range(0, n):
        zero_arr[arr[i] -1] = 1
    missing_list = []
    for i in range(0, n+1):
        if (zero_arr[i] == 0):
            missing_list.append(i+1)
    print(*missing_list)

def main():
    arr = list(map(int, input().split()))
    n = len(arr)
    toFindMisingNum(arr, n)
    
main()
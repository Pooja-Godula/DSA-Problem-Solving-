def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    # BRUTE-FORCE APPROACH
    # k = k % len(arr)  # handles k > len(arr)
    # return arr[k:] + arr[:k]
    n = len(arr)
    k = k % n
    def reverse(start,end):
        while(start<end):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    reverse(0,k-1)
    reverse(k,n-1)
    reverse(0,n-1)
    return arr



arr = [7, 5, 2, 11, 2, 43, 1, 1]
print(rotateArray(arr,3))
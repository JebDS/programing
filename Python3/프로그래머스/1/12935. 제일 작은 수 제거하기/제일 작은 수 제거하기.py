def solution(arr):
    if len(arr)==1: return [-1]
    arr2=sorted(arr)
    arr.remove(arr2[0])
    return arr
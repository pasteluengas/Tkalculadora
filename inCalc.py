def calcular(arr):
    for i in range(0, len(arr)):
        if "*" in arr or "/" in arr:
            if arr[i] == "*":
                arr[i] = arr[i-1] * arr[i+1]
            elif arr[i] == "/":
                arr[i] = arr[i-1] / arr[i+1]
            else:
                continue
            arr.pop(i+1)
            arr.pop(i-1)
            return
            
        if "+" in arr or "-" in arr:
            if arr[i] == "+":
                arr[i] = arr[i-1] + arr[i+1]
            elif arr[i] == "-":
                arr[i] = arr[i-1] - arr[i+1]
            else:
                continue
            arr.pop(i+1)
            arr.pop(i-1)
            return

arr1 = [10, "+", 2, "*", 10] # = 30
arr = [10, "/", 2, "-", 2, "*", 2] # = 1
arr3 = [5, "-", 4] # = 1
print(arr)
while len(arr) > 1:
    calcular(arr)
    print(arr)

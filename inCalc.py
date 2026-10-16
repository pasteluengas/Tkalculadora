'''
Devuelve 0: Todo bien
Devuelve -1: Error de sintaxis
Devuelve -2: Division entre cero
'''
def calcular(arr):
    for i in range(0, len(arr)):
        if arr[i] in ["+", "-", "*", "/"]:
            if i == 0:
                return -1
            if not isinstance(arr[i-1], (int, float)) or not isinstance(arr[i+1], (int, float)):
                return -1
        if "*" in arr or "/" in arr:
            if arr[i] == "*":
                arr[i] = arr[i-1] * arr[i+1]
            elif arr[i] == "/":
                if arr[i+1] == 0:
                    return -2
                arr[i] = arr[i-1] / arr[i+1]
            else:
                continue
            arr.pop(i+1)
            arr.pop(i-1)
            return 0
            
        if "+" in arr or "-" in arr:
            if arr[i] == "+":
                arr[i] = arr[i-1] + arr[i+1]
            elif arr[i] == "-":
                arr[i] = arr[i-1] - arr[i+1]
            else:
                continue
            arr.pop(i+1)
            arr.pop(i-1)
            return 0

if __name__ == "__main__":
    arr2 = ["+", 2, "*", 10] # = 30
    arr1 = [10, "+", 2, "*", 10] # = 30
    arr = [10, "/", 2, "-", 2, "*", 2] # = 1
    arr3 = [5, "-", 4] # = 1

    print(arr)
    while len(arr) > 1:
        r = calcular(arr)
        if r != 0:
            print("error ", r)
            break
        print(arr)

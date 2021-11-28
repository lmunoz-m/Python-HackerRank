if __name__ == '__main__':
    n = int(raw_input())
    if(n >= 2 and n <= 10):
        arr = map(int, raw_input().split())
   
i = 0
res = -100
while (i < n):
    if(arr[i] >= -100 and arr[i] <= 100):
        if(res < arr[i]):
            res = arr[i]
    i += 1 
i = 0
res2 = -100
while(i < n):
    if(arr[i] >= -100 and arr[i] <= 100):
        if (arr[i] > res2 and arr[i] != res):
            res2 = arr[i]
    i += 1 
print(res2)
      

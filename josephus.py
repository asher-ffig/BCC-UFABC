n = int(input("número de pessoas: "))
m = 3

def josephus (n:int, m:int) -> int:
  A = [i for i in range(1, n+1)]    
  while len(A) > 1:                
    for i in range(m-1):
      A.append(A.pop(0))
    A.pop(0)
    print(A)

josephus(n,m)

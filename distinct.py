#    0  1  2  3  4  5  6  7  8  9
A = [6, 1, 7, 5, 2, 5, 9, 0, 2, 3]

def distinct(A:list) -> int:
  B = []
  B.append(A[0])
  for i in range(len(A)):
      for j in range(len(B)):
          if A[i] == B[j]:
              break
      else:
          B.append(A[i])
  return(len(B))

distinct(A)

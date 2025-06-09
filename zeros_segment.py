#    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21
A = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

def zeros_segment(A:list) -> int:
  mm = mi = mj = m = i = 0

  for j in range(len(A)):
        if A[j] == 0:
            m += 1
        else:
            m = 0
            i = j
        if m > mm:
            mm = m
            mi = i + 1
            mj = j

  return(mm, mi, mj)

zeros_segment(A)

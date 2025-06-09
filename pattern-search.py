S = [0, 1, 0]
T = [0, 1, 0, 2, 3, 0, 4, 5, 0, 1, 0, 6, 7, 8, 9, 0, 3, 10, 2, 0, 1, 0, 1, 0]

def pattern_search(S:list, T:list) -> int:
  n = len(S)
  count = 0
  for i in range(len(T)):
    if T[i:i+n] == S:
      count += 1
  return count

print(pattern_search(S, T))

# Form a number system with only 3 and 4. Find the nth number of the number system Eg.) The numbers are: 3, 4, 33, 34, 43, 44, 333, 334, 343, 344, 433, 434, 443, 444, 3333, 3334, 3343,3344, 3433, 3434, 3443, 3444.
# Input Size: 1 <= N <= 100000

# Sample Testcases:
# INPUT
# 1
# OUTPUT
# 3

def nth_threefour(n):
  lst = []
  for i in range(n):
    if i == 0:
      lst.append(3)
    else:
      lastchar = list(str(lst[i-1]))
      size = len(lastchar)
      x = 0    
      while size >= 0:
        if size == 0:
          lastchar = '3'+''.join(lastchar)
          lst.append(int(lastchar))
        elif int(lastchar[-1-x]) == 3:
          lastchar[-1-x] = '4'
          lst.append(int(''.join(lastchar)))
          x += 1
          break
        else:
          lastchar[-1-x] = '3'
          x += 1
        size -= 1
  return(lst)

if __name__ == '__main__':
  n = int(input())
  threefour = nth_threefour(n)
  #print(*threefour)
  print(threefour[-1])

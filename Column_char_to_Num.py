#this code will calculate the column number of excel column head(A - 1, AA-28, XFD - 16384)

def column_number(chara):
  chara = chara.upper()
  a = len(chara)
  #Assign numbers for A-Z
  values = { chr(k):v for k,v in zip(range(65, 91),range(1,27))}
  col_no = 0
  for i in range(a):
    col_no += pow(26,i)*values[chara[a-1-i]]
  return col_no

print(column_number(input()))

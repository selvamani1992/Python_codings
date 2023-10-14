"""You've been tasked with preparing a birthday cake for a child, and your plan is to place one candle on the cake for each year of the child's age. However, only the tallest candle can be blown out. Your job is to determine the number of candles that share the same height as the tallest one.


Example
candles = [4,4,1,3]
The maximum height candles are 4 units high. There are 2 of them. so return 2.

sample input
3213
sample output
2
"""


def tallest_candles(candles):
  tallest = max(candles)
  no_tallest = candles.count(tallest)
  return no_tallest

if __name__ == '__main__':
  num = int(input())
  candles = list(map(int,input().split()))[:num]
  if num > 0:
    print(tallest_candles(candles))
  else:
    print(0)

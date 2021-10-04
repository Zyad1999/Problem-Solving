T = int(input())

for i in range(T):
  N = int(input())
  bits = list(bin(N))[2:]
  p = ["Louise", "Richard"]
  bit_count = bits.count('1')
  right_zeros = bits[::-1].index('1')
  print (p[(bit_count + right_zeros) % 2])
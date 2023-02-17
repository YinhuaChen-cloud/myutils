OFFSET = 1 << 64 
MASK = OFFSET - 1

def int2Hex(num):
  hex = '%016x' % ((num + OFFSET) & MASK)
  bytes = []

  for i in range(0, 8):
    bytes.append('0x' + hex[i * 2: i * 2 + 2])

  # return bytes[::-1]  # return in little endian
  return bytes 

print(int2Hex(-214747137))
print(int2Hex(20))
print(int2Hex(-20))



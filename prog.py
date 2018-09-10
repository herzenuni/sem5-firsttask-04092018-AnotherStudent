import sys

params = sys.argv
numbers = ['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять']

try:
  if len(params) < 2:
    raise Exception("Too low parameters")

  if len(params) > 3:
    raise Exception("Too many parameters")

  try:
    if len(params) == 2:
      val = int(params[1])
      if (val < 0) or (val > 9):
        raise Exception("Out of range in 1 parameter")
      print(numbers[val])
    else:
      val = int(params[1])
      typ = params[2]
      if typ == "bin":
        print(bin(val))
      elif typ == "hex":
        print(hex(val))
      elif typ == "oct":
        print(oct(val))
      else:
        raise Exception("Bad number type")
  
  except ValueError:
    raise ValueError("Bad number")

except Exception as e:
  print("Error: "+str(e)) 
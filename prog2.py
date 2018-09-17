import sys
import logging

params = sys.argv
numbers = ['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять']

class EOutOfRange(Exception):
  pass

class EBadNumberType(Exception):
  pass

logging.basicConfig(filename="log.txt", level=logging.INFO)

try:
  logging.info("params:" + str(params))

  if len(params) < 2:
    raise Exception("Too low parameters")

  if len(params) > 3:
    raise Exception("Too many parameters")

  try:
    if len(params) == 2:
      val = int(params[1])
      if (val < 0) or (val > 9):
        raise EOutOfRange("Out of range in 1 parameter")
      print(numbers[val])
      logging.info("out:" + str(numbers[val]))
    else:
      val = int(params[1])
      typ = params[2]
      if typ == "bin":
        print(bin(val))
        logging.info("out:" + str(bin(val)))
      elif typ == "hex":
        print(hex(val))
        logging.info("out:" + str(hex(val)))
      elif typ == "oct":
        print(oct(val))
        logging.info("out:" + str(oct(val)))
      else:
        raise EBadNumberType("Bad number type")
  
  except ValueError:
    raise ValueError("Bad number")

except Exception as e:
  logging.error("error:" + str(e))
  print("Error: " + str(e)) 
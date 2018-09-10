from subprocess import run, PIPE

def check(params, result):
  r = run(params, stderr = PIPE, stdin = PIPE, stdout = PIPE, universal_newlines=True)
  s = r.stdout[0:-1]
  if s != result:
    raise Exception('"' + s + '" is not eqal "' + result + '"')

try:
  check(["python3", "prog.py", "1"], "один")
  check(["python3", "prog.py", "4"], "четыре")
  check(["python3", "prog.py", "9"], "девять")
  check(["python3", "prog.py", "-1"], "Error: Out of range in 1 parameter")
  check(["python3", "prog.py"], "Error: Too low parameters")
  check(["python3", "prog.py", "1", "2", "3"], "Error: Too many parameters")
  check(["python3", "prog.py", "100", "bin"], "0b1100100")
  check(["python3", "prog.py", "100", "hex"], "0x64")
  check(["python3", "prog.py", "100", "oct"], "0o144")
  check(["python3", "prog.py", "****"], "Error: Bad number")
except Exception as e:
  print("Fail: " + str(e))
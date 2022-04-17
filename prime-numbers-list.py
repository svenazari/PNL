#PNL - Prime Numbers List
#REQUREMENTS: Python3

#Made by Sven Azari
#http://www.github.com/svenazari

def prime():
  #inputs
  a = input("FROM: ")
  b = input("TO: ")
  primel = [] #list to store primes
  if a == "2" or a == "1":
    a1 = 3
  else:
    try:
      a1 = int(a)
    except:
      print("INPUT ONLY INTEGERS!")
      exit ()
  try:
    b1 = int(b) + 1
  except:
    print("INPUT ONLY INTEGERS!")
    exit ()
  for p in range(a1, b1, 1): #range of test
    d = round(p / 2) + 1
    for d in range(2, d, 1): #range of division
      test = p % d
      if test == 0:
        break
    if test != 0:
      primel.append(p) #if number is prime, append it to list
      continue
    else:
      continue
  print("* * *")
  print("PRIMES:")
  print(primel) #print primes

prime()

#PNL - Prime Numbers List
#REQUREMENTS: Python3

#Made by Sven Azari
#http://www.github.com/svenazari

def prime():
  #inputs
  a = input("FROM: ")
  b = input("TO: ")
  primel = [] #list to store primes
  try:
    a1=int(a)
  except: #if first input is not an integer
    print("Integers only! (" + a + " is not an integer!)")
    exit()
  try:  
    b1=int(b)
  except: #if second input is not an integer
    print("Integers only! (" + b + " is not an integer!)")
    exit()
  if b < a: #if second number is larger
    print ("Second number must be larger than first!")
    exit()
  elif a == "2" or a == "1": #1 and 2 are not considered as primes so they can be omitted from this test
    a1 = 3
  for p in range(a1, b1, 1): #range of test
    d = round(p / 2) + 1
    for d in range(2, d, 1): #range of division
      test = p % d #test for remainder
      if test == 0: #if there is reminder, number is not prime
        break
    if test != 0:
      primel.append(p) #if number is prime, append it to list
      continue
    else:
      continue
  print("* * *")
  print("PRIMES:")
  print(primel) #print primes

prime() #call function

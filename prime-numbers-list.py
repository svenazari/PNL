#PNL - Prime Numbers List
#REQUREMENTS: Python3

#Made by Sven Azari
#http://www.github.com/svenazari

#imports
import math

def prime():
  #inputs
  a = input("FROM: ")
  b = input("TO: ")
  primel = [] #list to store primes
  try:
    try:
      a1 = int(a)
    except ValueError: #if first input is not an integer do check for float
      try:
        af = float(a)
      except ValueError: #if first value cannot be converted to float
        print("Numbers only! '" + a + "' is not valid number. (Use decimal point instead coma.)")
        exit()
      else:
        a1 = math.ceil(af) #round to first bigger integer
    try:  
      b1 = int(b)
    except ValueError: #if second input is not an integer do check for float
      try:
        bf = float(b)
      except ValueError: #if second value cannot be converted to float
        print("Numbers only! '" + b + "' is not valid number. (Use decimal point instead coma.)")
        exit()
      else:
        b1 = math.floor(bf) #round to first smaller integer
    if float(b) < float(a): #if second number is smaller
      print ("Second number must be larger than first!")
      exit()
    elif a1 < 3: #0, 1 and 2 are not considered primes (2 is nor prime nor composit number) so they are omitted from this test
      a1 = 3
    for p in range(a1, b1+1, 1): #range of test
      d = round(p / 2) + 1
      for e in range(2, d, 1): #range of division
        test = p % e #test for remainder
        if test == 0: #if there is no reminder, number is not prime
          break
      if test != 0:
        primel.append(str(p)) #if number is prime, append it to list
        continue
      else:
        continue
  except KeyboardInterrupt: #if user aborts calculation
    print ("\n" + "ABORTED BY USER!")
  else:
    if len(primel) == 0: #test length of list of primes
      print("* * *")
      print("There are no prime numbers in range from " + a + " to " + b + ".") #if there are no primes in tested range (if length of list is 0)
    else:
      print("* * *")
      print("Prime numbers in range from " + a + " to " + b + " are: " + ", ".join(primel) + ".") #if there are primes in tested range

prime() #call function

#version2: range can also be defined with decimal numbers
#version1: range can only be defined with integers

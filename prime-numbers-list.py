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
  print("Please wait. Calculating...")
  try:
    try:
      af = float(a.replace(',','.'))
    except ValueError: #if first value cannot be converted to float
      print("Numbers only! '" + a + "' is not number.")
      exit()
    else:
      a1 = math.ceil(af) #round to first bigger integer
    try:  
      bf = float(b.replace(',','.'))
    except ValueError: #if second value cannot be converted to float
      print("Numbers only! '" + b + "' is not number.")
      exit()
    else:
      b1 = math.floor(bf) #round to first smaller integer
    if bf < af: #if second number is smaller
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
    print ("\033[A                             \033[A") #delate "Please wait" line
    print ("\n" + "ABORTED BY USER!")
  else:
    if len(primel) == 0: #test length of list of primes
      print ("\033[A                             \033[A") #delate "Please wait" line
      print("* * *")
      print("There are no prime numbers in range from " + a + " to " + b + ".") #if there are no primes in tested range (if length of list is 0)
    elif len(primel) == 1:
      print ("\033[A                             \033[A") #delate "Please wait" line
      print("There is only one prime number in range from " + a + " to " + b + ". It is " + ", ".join(primel) + ".") #if there is only one prime number in range
    else:
      print ("\033[A                             \033[A") #delate "Please wait" line
      print("* * *")
      print("There are " + str(len(primel)) + " prime numbers in range from " + a + " to " + b + ". They are: " + ", ".join(primel) + ".") #if there are primes in tested range

prime() #call function

#version 4: small adjustments to output lines
#version 3: decimal numbers with coma instead of decimal point can also be converted to float
#version 2: range can also be defined with decimal numbers
#version 1: range can only be defined with integers

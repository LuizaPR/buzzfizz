# numbers divisible by 3: Fizz
# numbers divisible by 5: Buzz
# numbers divisible by both: BuzzFizz

for number in range(1, 101):
  division1 = number % 3
  division2 = number % 5
  sum = division1 + division2

  if sum == 0:
    print("FizzBuzz")
    
  elif division1 == 0:
      print("Fizz")  
  
  elif division2 == 0:
      print("Buzz")

  else: 
    print(number)
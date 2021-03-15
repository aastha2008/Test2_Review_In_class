import random
import time

## prompt 1:
print("Welcome to the Multipliacation Game.")
print("You will be prompted to solve a math equation")
print("And you will need to answer within 3 seconds")

ready = input("Are you ready to play? (y/n): ").lower()
score = 0

while (ready == 'y' or ready == 'yes'):
  
  # prompt3
  num1 = random.randint(0,12)
  num2 = random.randint(0,12)

  for x in range(3):
    print(3-x)
    time.sleep(1)

  #prompt4
  t1 = time.time()
  question = int(input(str(num1) + " x" + str(num2) + " ="))
  # prompt5
  t2 = time.time()
  
  print("You took " + str(t2 - t1))

  # prompt 6:
  if( (t2 - t1 < 3 ) and (question == num1 * num2) ):
    print("You got it")
    score += 1
  else:
    print("You failed")
  # prompt2
  ready = input("Are you ready to play? (y/n): ")

print("Take your time and prepare.")
print("Your score is : " + str(score))




import time

num=int(input("Enter a number to start countdown:"))

while num > 0:
          print(num)
          num-= 1
          time.sleep(1)

print("Lights off!")
          

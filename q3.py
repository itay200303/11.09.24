#start

height: float = float(input('Enter your height :'))
while not  0.4 <= height <= 2.5:
    print('wrong input')
    height: float = float(input('Enter your height :'))

print('goodbye')

num1: int = int(input('Enter first number :'))
num2: int = int(input('Enter second number :'))

if num1 < num2:
    start = num1
    end = num2
    step = 1

else:
    start = num1
    end = num2
    step = -1

for number in range(start, end + step, step):
    print(number, end=' ')
print()

counter: int = 1
pie: float = float(input("whats is the value of pie?: "))
while not pie == 3.14 and counter < 3:
      counter += 1
      pie: float = float(input("whats is the value of pie?: "))

if counter == 3:
   print('pie is 3.14')
else:
   print('you are correct')

while True:
    num1: float = float(input("Enter the first number (0-10): "))
    num2: float = float(input("Enter the second number (10-60): "))
    num3: float = float(input("Enter the third number (60-100): "))

    if (0 <= num1 <= 10 and 10 <= num2 <= 60 and 60 <= num3 <= 100 \
        and num2 == (num1 + num2 + num3) / 3):
        print("Conditions met.")
        break
    else:
        print("Conditions not met. Please try again.")
print()

total_beers = 10

while total_beers > 0:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You get a beer!")
        total_beers -= 1
        print(f"Beers left: {total_beers}")
    else:
        print("Sorry, you must be at least 18 years old to get a beer.")

    if total_beers == 0:
        print("All beers have been sold.")
        break

# end
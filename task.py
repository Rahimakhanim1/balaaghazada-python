
# Task 1
number = int(input("Enter a number: "))
if number > 7:
  print("Hello")

#Task 2
name = input("Enter a name: ")
if name == "John":
  print("Hello, John")
else:
  print("There is no such name")

#Task 3
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Numbers divisible by 3")
for num in numbers:
  if num % 3 == 0:
    print(num)

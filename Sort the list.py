numbers= input("enter list of numbers separated by spaces")
numbers=[int(num) for num in numbers.split()]

print("choose sorting order:")
print("1.ascending")
print("2.descending")
choice =input("enter your choice(1 or 2)")
if choice=="1":
    numbers.sort()
    print(numbers)
elif choice=="2":
    sorted_r=sorted(numbers)
    print(sorted_r[::-1])
else:
    print("invalid choice")

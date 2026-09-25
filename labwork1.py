#Ex1:
import math
r = float(input("enter circle radius? "))
area = math.pi * (r**2)
print(f"Circle area = ", area)

#Ex2:
a= int(input("enter the temperature in Celcius: "))
print("temperature from Celccius to Fahrenheit = ", 1.8* a + 32 )

#Ex3:
n=int(input("enter a number: "))
if n%2==0:
    print("n is Not prime number")
else:
    print("n is prime number")

#Ex4:
# Get user input
num = int(input("Enter a number? "))
# A perfect number must be greater than 0
if num > 0:
    # Find and sum all proper divisors
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
        # Check if the sum equals the original number
    if divisor_sum == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is a NOT perfect number")
else:
    print(f"{num} is a NOT perfect number")

#Ex5:
# A sample list where 'Red' sits at index 3
colors = ["Blue", "Yellow", "Purple", "Red", "Black"]
# Ask user for input
user_color = input("What is your favorite color? ")
# Check if the color exists in the list
if user_color in colors:
    # Get the position/index of the color
    index = colors.index(user_color)
    print(f"Your colod is at index {index} in my list")
else:
    print("Sorry, I could not find your color")

#Ex6:
print("range1: ", list(range(0, 7)))
print("range2: ", list(range(1,11,3)))
print("range3: ", list(range(5,0,-1)))
print("range4: ", list(range(6,-3,-2)))

#Ex7:
def remove_dollar_sign(s):
    # Use the replace method to swap all "$" with an empty string
    return s.replace("$", "")

input_text = "The price is $100 dollars!"
print(remove_dollar_sign(input_text))

#Ex8:
def extract_even(l):
    # Filter the list to keep numbers divisible by 2
    return [num for num in l if num % 2 == 0]

test_list = [1, 4, 5, -1, 10]
print(extract_even(test_list))

#Ex9:
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
        
    result = 1
    for i in range(2, n + 1):
        result *= i
        
    return result

print(calculate_factorial(5))

#Ex10:
def get_divisors(n):
    # Ensure we are dealing with a positive number
    n = abs(n)
    if n == 0:
        return []
        
    # Use a list comprehension to find numbers that divide n perfectly
    return [i for i in range(1, n + 1) if n % i == 0]

# We can now run the function and print the output
test_number = 20
print(get_divisors(test_number))

#Ex11:
import math
def calculate_distance(point1, point2):
    #calculate the distance between two points
    return math.dist(point1, point2)
#Define two points as (x, y) coordinates
p1 = [1, 2]
p2 = [4, 6]

# Calculate and display the result
distance = calculate_distance(p1, p2)
print(f"The distance between {p1} and {p2} is {distance}")

#Ex12:
def print_pattern(m, n):
    for r in range(m):
        # If it's the first row or the last row, print a solid line of asterisks
        if r == 0 or r == m - 1:
            print(" ".join("*" for _ in range(n)))
        else:
            # For middle rows, print a star at the start, spaces, and a star at the end
            # " " * (2 * n - 3) accounts for the spaces between asterisks
            print("*" + " " * (2 * n - 3) + "*")

# We run the function using the dimensions from your image (4 rows by 5 columns)
print_pattern(4, 5)
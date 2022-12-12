# the code modify by Pramod
# this code is for calculating bonus of all employees

exp= int(input("Enter Work experience: "))

sal= int(input("Enter your salary in thousands: "))

# bonus modified with 25%
# modified date 11dec at 11.00am
#exp and sal is modified
bonus=(0.28*sal)
if exp>=3 and sal>=28000:
    print(f"Your bonus amount is Rs.{bonus}")
else:
    print(f"Sorry, you are not eligible for bonus")

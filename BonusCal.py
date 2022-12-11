# code modified by sachin
# this code required some modifications in future
# the code modify by Pramod
# this code is for calculating bonus of all employees

exp= int(input("Enter Work experience: "))

sal= int(input("Enter your salary in thousands: "))

# bonus modified with 25%
# modified date 11dec at 11.00am

bonus=(0.25*sal)
if exp>=2 and sal>=25000:
    print(f"Your bonus amount is Rs.{bonus}")
else:
    print(f"Sorry, you are not eligible for bonus")

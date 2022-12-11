exp= int(input("Enter Work experience: "))

sal= int(input("Enter your salary in thousands: "))

bonus=(0.15*sal)
if exp>=2 and sal>=25000:
    print(f"Your bonus amount is Rs.{bonus}")
else:
    print(f"Sorry, you are not eligible for bonus")


# Lines added by Sachin Magadum
# Its testing purpose of git
username = "Emil"
password = "python123"
is_active = True

if username:
    if password:
        if is_active:
            print("User is active and can log in")
        else:
            print("User is not active")
else:
    print("Username is missing")

# //nested if else statement
marks = 85
credits= 5
if marks >=80:
    if credits >= 5:
        print("You have passed with with a+ grade")
    else:
        print("You have passed")
elif marks >= 60:
    print("You have passed")
else:
    print("You have failed")


day = 4
match day: 
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 40:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case __:
    print("Invalid day")
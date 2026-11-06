medical_cause=input("do you have a medical certificate? (Y/N): ").strip().upper()
if medical_cause=='Y':
    print("you are allowed")
else:
    atten=int(input("enter your attendence of the student: "))
    if (atten>=75):
        print("allowed")
    else:
        print("not allowed")

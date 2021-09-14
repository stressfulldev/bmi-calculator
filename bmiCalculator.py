print("Welcome to BMI Calculator")
while True :
    heightcm = input("Enter your height in cm: ")
    weight = input("Enter your weight in kg: ")

    heightm = float(float(heightcm) / 100)
    weight_bmi = float(weight)
    height_bmi = float(heightm)
    result_bmi = weight_bmi / (height_bmi * height_bmi)
    result_bmi_int = int(result_bmi)

    print(f"Your BMI score is {result_bmi_int} \n")

    while True :
        restart = input("Do you want to calculate another BMI score? (y/n): ")
        if restart in ("y, n"):
            break
    if restart == "y":
        continue
    else  :
        print("Thanks for using the Apps, Keep Healthy !")
        break
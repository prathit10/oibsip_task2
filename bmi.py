def calculate_bmi(weight, height_meters):
    bmi = weight / (height_meters ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height_cm = float(input("Enter your height in centimeters: "))
        
        height_meters = height_cm / 100
        
        bmi = calculate_bmi(weight, height_meters)
        category = classify_bmi(bmi)
        
        print(f"Your BMI is {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")

if __name__ == "__main__":
    main()

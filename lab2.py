def calculate_bmi(height, weight):
    print("Height= "+ str(height))
    print("Weight= "+ str(weight))
    bmi = weight/(height**2)
    print("BMI= "+str(bmi))

    type = 0
    if(bmi<18.5):
        type = -1
    if(18.5 <= bmi <= 25.0 ):
        type = 0
    if(bmi>25):
        type = 1


    return type

def main():
    bmi = calculate_bmi(weight=70, height=1.75)
    print(bmi)

if __name__ == "__main__":
    main()


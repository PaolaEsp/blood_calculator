def interface():
    print("My program")
    while True:
        print("Options")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()
def LDL_driver():
    LDL_result = LDL_input()
    LDL_analysis = analyze_LDL_result(LDL_result)
    output_LDL_analysis(LDL_result, LDL_analysis)
def LDL_input():
    LDL_input = input("Enter the LDL test result: ")
    return int(LDL_input)
def analyze_LDL_result(LDL_test_result):
    if LDL_test_result < 130:
        return "Normal"
    elif 130 <= LDL_test_result <= 159:
        return "Borderline high"
    elif 160 <= LDL_test_result <= 189:
        return "High"
    elif LDL_test_result >= 190:
        return "Very high"
def output_LDL_analysis(test_result, analysis):
    print("The LDL result is {}".format(test_result))
    print("That is {}".format(analysis))

def HDL_driver():
    # Get input
    HDL_result = get_input()
    HDL_analysis = analyze_HDL_result(HDL_result)
    output_HDL_analysis(HDL_result, HDL_analysis)
def get_input():
    HDL_input = input("Enter the HDL test result: ")
    return int(HDL_input)

    # Check if HDL is normal
def analyze_HDL_result(HDL_test_value):
    if HDL_test_value >= 60:
        return "Normal"
    elif 40 <= HDL_test_value < 60:
        return "Borderline Low"
    else:
        return "Low"

    # Output
def output_HDL_analysis(test_result, analysis):
    print("The HDL result is {}".format(test_result))
    print("That is {}".format(analysis))

interface()

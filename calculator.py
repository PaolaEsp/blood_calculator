def interface():
    print("My program")
    while True:
        print("Options")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()

def HDL_driver():
    # Get input
    HDL_result = get_input()
    HDL_analysis = analyze_HDL_result(HDL_result)
    def get_input():
        HDL_input = input("Enter your choice: ")
        return int(HDL_input())

    # Check if HDL is normal
    def analyze_HDL_result(HDL_test_value):
        if HDL_test_value >= 60:
            return "Normal"
        elif 40 <= HDL_test_value < 60:
            return "Borderline Low"
        else:
            return "Low"

    # Output





interface()

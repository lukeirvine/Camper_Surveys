DEBUG = False

def main():
    import functions
    import csv

    '''
    data is used to hold questions and data for the survey.
    Each item in this list will be another list. The first item
    of each nested list will be the survey question, the second item will
    be the question type, 1 being a 1-11 rating question, and 2 being
    a short answer question. 
    
    For a type 1 question, the third item will be a dictionary which
    have the number of votes for each number out of 11. Each key in
    the dictionary will be labeled 1 through 11 and each corresponding
    value will be the number of votes for that key
    
    For a type 2 question, the third item will be another list with all
    the short answers in it.
    '''

    data = []

    # welcome and ask if new survey or continuing old survey
    functions.welcome()
    choice = functions.get_letter(['a', 'b'], "Enter the letter of your choice: ")

    # variable to count how many surveys are entered and survey name vairable
    surveyCount = 0
    surveyName = "Untitled"

    # if new, prompt survey question entry
    if choice == 'a':

        print('\n\t\033[31m' + 'New Survey Selected' + '\033[0m')
        surveyName = str(input("Enter survey name: "))
        print("\n")
        # instructions for entering questions
        functions.item_entry_instructions()

        # function that loads data list with questions
        functions.input_items(data, DEBUG)
        if DEBUG:
            for i in range(0, len(data)):
                print(data[i])


    # if old, pull up old previous csv file and load questions

    if choice == 'b':
        print('\n\t\033[31m' + 'Old Survey Selected' + '\033[0m')
        error = True
        while error:
            error = False
            try:
                surveyName = input("Enter old survey csv file name: ")
                # function to read csv into data structure
                data = []
                surveyCount = functions.read_csv(data, surveyName, DEBUG)
            except(FileNotFoundError):
                print("\nError: File " + surveyName + ".csv not found.")
                error = True


    # function to collect all input for each survey
    surveyCount = functions.data_collection(data, surveyCount, surveyName, choice, DEBUG)

    if DEBUG:
        for i in range(0, len(data)):
            print(data[i])

    # function to export data list to csv file

    functions.export_csv(data, surveyCount, surveyName, choice, DEBUG)

    return 0

main()

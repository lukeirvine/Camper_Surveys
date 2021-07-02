from sys import stdout
import csv

# ============================================================
'''
 * Function: get_number
 * Preparamter: - minimum value for input, 
 *              - maximum value for input,
 *              - and string to display the prompt
 * Purpose: checks input for type and range errors
 * Postparamter: Returns a value from input once it
 *               has been checked.
 *
'''


def get_number(min, max, prompt):
    invalid = True

    while invalid:
        invalid = False
        try:
            userInput = input(prompt)
            userInput = int(userInput)
            if userInput < min or userInput > max:
                stdout.write('\nError: Please enter a whole number between ' + str(min) + ' and '
                             + str(max) + '.\n')
                invalid = True
        except(ValueError, TypeError):
            stdout.write('\nError: Please enter a whole number between ' + str(min) + ' and '
                         + str(max) + '.\n')
            invalid = True

    return userInput


# ============================================================
'''
 * Function: get_number_or_letters
 * Preparamter: - minimum value for input, 
 *              - maximum value for input,
 *              - and string to display the prompt
 * Purpose: checks input for type and range errors
 * Postparamter: Returns a value from input once it
 *               has been checked.
 *
'''


def get_number_or_letters(min, max, letters, prompt):
    invalid = True

    while invalid:
        invalid = False
        try:
            userInput = input(prompt)
            userInput = str(userInput)

            # loop to check input against letters in list
            for i in range(0, len(letters)):
                invalid = True
                if userInput == letters[i]:
                    invalid = False
                    break
            if invalid == False:
                break

            # checking if input was a number
            userInput = int(userInput)
            # checking if input was a proper number
            invalid = False
            if userInput < min or userInput > max:
                stdout.write('\nError: Please enter a whole number between ' + str(min) + ' and '
                             + str(max) + ' or proper letter.\n')
                invalid = True
        except(ValueError, TypeError):
            stdout.write('\nError: Please enter a whole number between ' + str(min) + ' and '
                         + str(max) + ' or proper letter.\n')
            invalid = True

    return userInput


# ============================================================
'''
 * Function: get_letter
 * Preparamter: - minimum value for input, 
 *              - maximum value for input,
 *              - and string to display the prompt
 * Purpose: checks input for type and range errors
 * Postparamter: Returns a value from input once it
 *               has been checked.
 *
'''


def get_letter(letters, prompt):
    invalid = True

    while invalid:
        invalid = False
        try:
            userInput = input(prompt)
            userInput = str(userInput)
            for i in range(0, len(letters)):
                invalid = True
                if userInput == letters[i]:
                    invalid = False
                    break
            if invalid == True:
                print("\nError: Please enter proper input.")
        except(ValueError, TypeError):
            print("\nError: Please enter proper input.")
            invalid = True

    return userInput


# ============================================================
'''
 * Function: welcome
 * Preparamter: - none
 * Purpose: displays instructions and welcome screen
 * Postparamter: prints welcome screen
 *
'''

def welcome():
    print('\n\t\033[31m' + 'Welcome to the Mivoden Camper Survey Entry Program' + '\033[0m')
    print("You will be prompted to enter values for each question on the survey")
    print("and this program will store a csv file to be used later in the spread")
    print("sheet program of your choice.")
    print("\nAre you:")
    print("\ta) starting a new survey")
    print("\tb) continuing an old survey")


# ============================================================
'''
 * Function: item_entry_instructions
 * Preparamter: - none
 * Purpose: displays instructions for entering questions
 * Postparamter: prints instructions
 *
'''

def item_entry_instructions():
    print("Enter each survey item when prompted, and then enter each")
    print("item type when prompted. The item types are:")
    print("\t0) A category header")
    print("\t1) A question where participants enter a number between")
    print("\t   1 and 11 describing how much they liked the activity.")
    print("\t2) A short answer question.")
    print("Enter 'd' when you are done entering questions.")


# ============================================================
'''
 * Function: input_questions
 * Preparamter: - data list which is passed by reference
                - DEBUG boolean variable for debugging purposes
 * Purpose: Loads survey questions into list from input and types for each question
            Also Creates dictionary for 1-11 type questions
 * Postparamter: Returns the data list by reference
 *
'''

def input_items(data, DEBUG):
    # loop that asks for questions
    notDone = True
    i = 0
    while notDone:
        data.append([])
        # loop to make sure item is not empty
        empty = True
        while empty:
            item = input("\nEnter item " + str(i + 1) + ": ")
            if item != '':
                empty = False
            else:
                print("\nError: item cannot be empty.")

        # exit loop if 'd' is entered
        if item == "d":
            if DEBUG:
                print("Loop terminated")
            notDone = False
            break

        data[i].append(item)

        # ask for question type
        iType = get_number(0, 2, "Enter item type number: ")
        data[i].append(iType)

        # if type 0, add nothing

        # if type 1, add dictionary and fill with zeros
        if iType == 1:
            data[i].append({})
            for j in range(1, 11 + 1):
                data[i][2][int(j)] = 0

        # if type 2, add empty list to be filled with short answer responses
        if iType == 2:
            data[i].append([])

        i += 1
# ============================================================
'''
 * Function: data_collection_instructions
 * Preparamter: - none
 * Purpose: displays instructions on how to enter data
 * Postparamter: prints instructions
 *
'''

def data_collection_instructions():
    print('\n\t\033[31m' + 'Data Entry Instructions' + '\033[0m')
    print("\tFor type 1 questions, enter a number between 1 and 11.")
    print("(Enter 11 for anything listed over 10)")
    print("(You can also enter a '0' as short hand for '10')")
    print("\tFor type 2 questions, enter the answer but modify it so")
    print("all similar answers are formatted the same way.")
    print("(all lowercase recommended)")
    print("If the survey answer is blank, enter 'x'.")
    print("If you would like to go back an item, enter 'b'.")


# ============================================================
'''
 * Function: data_collection
 * Preparamter: - data list which is passed by reference
                - surveyNumber which is the number of recorded surveys
                - DEBUG boolean variable for debugging purposes
 * Purpose: prompts and collects data from each survey
 * Postparamter: Returns the data list by reference
 *
'''

def data_collection(data, surveyCount, surveyName, choice, DEBUG):
    data_collection_instructions()


    notDone = True
    i = surveyCount + 1
    # ask if they would like to enter surveys first
    answer = get_letter(['y', 'n'], "\nWould you like to start entering surveys? (y/n): ")
    if answer == 'n':
        return surveyCount

    # loop to collect multiple surveys
    while notDone:
        print('\n\t\033[31m' + 'Survey #' + str(i) + '\033[0m')
        surveyCount += 1
        # loop to loop through survey items
        '''
        length of data is adjusted depending on choice variable to adjust for
        weird bug that gives data an extra empty element when creating a new
        survey.
        '''
        if choice == 'a':
            dataLength = len(data) - 1
        if choice == 'b':
            dataLength = len(data)

        # list to keep track of number entries in previous loop iterations
        history = []
        # used to count loop iterations
        j = 0
        # used to count number of short answer inputs per question
        entryNumber = 0
        # + 1 is to allow for additional place to backspace
        while j < dataLength + 1:
            # for when we're on the last iteration asking if we want to backspace
            if j == dataLength:
                answer = get_letter(['b', 'n'], "Back Space? (b/n): ")
                if answer == 'b':
                    if data[j - 1][1] == 1:
                        data[j - 1][2][history[len(history) - 1]] -= 1
                        j -= 1
                        print('\n\033[33m' + 'Back Space' + '\033[0m')
                        continue
                    if data[j - 1][1] == 2:
                        data[j - 1][2].pop(len(data[j - 1][2]) - 1)
                        j -= 1
                        print('\n\033[33m' + 'Back Space' + '\033[0m')
                        continue
                else:
                    break

            # put space if there is a header
            if data[j][1] == 0:
                print('\n\033[31m' + str(data[j][0]) + '\033[0m')
            # if question is item type 1
            if data[j][1] == 1:
                # get the number
                number = get_number_or_letters(0, 11, ['x', 'b'], (str(data[j][0]) + " (1-11): "))
                # handle '0' shortcut
                if number == 0:
                    number = 10
                # store the number in data
                if number != 'x' and number != 'b':
                    history.append(int(number))
                    data[j][2][int(number)] += 1
                # go back if number is 'b'
                if number == 'b':
                    if j <= 1:
                        print("Error: can't go back anymore.")
                        continue
                    if data[j - 1][1] == 1:
                        data[j - 1][2][history[len(history) - 1]] -= 1
                        j -= 1
                        print('\n\033[33m' + 'Back Space' + '\033[0m')
                        continue
                    if data[j - 1][1] == 0:
                        data[j - 2][2][history[len(history) - 1]] -= 1
                        j -= 2
                        print('\n\033[33m' + 'Back Space' + '\033[0m')
                        continue

            # if question is item type 2
            if data[j][1] == 2:
                print('\n\033[33m' + 'Short Answer Question (Enter \'d\' when done).' + '\033[0m')
                # loop to enter more than one item for question
                notDone = True
                # to temporarily hold short answer questions
                shortAnswer = []
                while notDone:
                    shortAnswer.append(input('\033[34m' + str(data[j][0]) + ': ' + '\033[0m'))
                    if shortAnswer[len(shortAnswer) - 1] == 'd' or shortAnswer[len(shortAnswer) - 1] == 'b':
                        notDone = False
                        break
                    entryNumber += 1
                # Back space
                if shortAnswer[len(shortAnswer) - 1] == 'b':
                    if data[j - 1][1] == 1:
                        data[j - 1][2][history[len(history) - 1]] -= 1
                        j -= 1
                        print('\n\033[33m' + 'Back Space' + '\033[0m')
                        continue
                    if data[j - 1][1] == 2:
                        for k in range(0, entryNumber):
                            data[j - 1][2].pop(len(data[j - 1][2]) - 1)
                        j -= 1
                        # reset entryNumber
                        entryNumber = 0
                        print('\n\033[33m' + 'Back Space' + '\033[0m')
                        continue

                # move short answer responses into data structure
                for l in range(0, len(shortAnswer) - 1):
                    data[j][2].append(shortAnswer[l])

            # increment loop counter
            j += 1

        # save current survey entry
        export_csv(data, surveyCount, surveyName, choice, DEBUG)
        print('\n\033[31m' + 'Survey Saved' + '\033[0m')

        # ask if there are more surveys
        show = True
        notDone = True
        while show:
            answer = get_letter(['y', 'n', 's'], "Enter another survey or show progress? (y/n/s): ")
            if answer == 's':
                print('\n\t\033[31m' + 'Progress' + '\033[0m')
                for j in range(0, len(data)):
                    print(data[j])
                print("\n")
            else:
                show = False
                break

        if answer == 'y':
            i += 1
            continue
        if answer == 'n':
            notDone = False
            break

    return surveyCount

# ============================================================
'''
 * Function: export_csv
 * Preparamter: - data list which is passed by reference
                - surveyNumber which is the number of recorded surveys
                - DEBUG boolean variable for debugging purposes
 * Purpose: exports data list to csv file
 * Postparamter: none
 *
'''

def export_csv(data, surveyCount, surveyName, choice, DEBUG):
    with open(str(surveyName) + '.csv', mode='w') as survey:
        survey_writer = csv.writer(survey, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # header of csv file with survey count in top left
        survey_writer.writerow(["Survey Count: " + str(surveyCount), '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])

        if choice == 'a':
            lengthData = len(data) - 1
        if choice == 'b':
            lengthData = len(data)

        for i in range(0, lengthData):
            # first category header
            if data[i][1] == 0 and i == 0:
                survey_writer.writerow([data[i][0], '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
            # type 1 question
            if data[i][1] == 1:
                survey_writer.writerow([data[i][0], data[i][2][1], data[i][2][2],
                                        data[i][2][3], data[i][2][4], data[i][2][5],
                                        data[i][2][6], data[i][2][7], data[i][2][8],
                                        data[i][2][9], data[i][2][10], data[i][2][11]])
            # category header with blank above it
            if data[i][1] == 0 and i != 0:
                survey_writer.writerow(['', ''])
                survey_writer.writerow([data[i][0], '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
            # type 2 question
            if data[i][1] == 2:
                # blank rows
                survey_writer.writerow(['', ''])
                # question title
                survey_writer.writerow([data[i][0], ''])
                for j in range(0, len(data[i][2])):
                    # type 2 question responses
                    if data[i][2][j] != 'x':
                        survey_writer.writerow([data[i][2][j], ''])


# ============================================================
'''
 * Function: read_csv
 * Preparamter: - data list which is passed by reference
                - surveyName which is the number of recorded surveys
                - DEBUG boolean variable for debugging purposes
 * Purpose: exports data list to csv file
 * Postparamter: none
 *
'''

def read_csv(data, surveyName, DEBUG):
    with open(str(surveyName) + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        i = -1
        surveyCount = ''
        type2on = False
        for row in csv_reader:
            # if DEBUG:
            #     data.append(row)

            # first row
            if i == -1:
                surveyCount = str(row[0])
                surveyCount = int(surveyCount[surveyCount.find(':') + 2:len(surveyCount)])
                i += 1
                signifier = 1
                continue
            # row with nothing in it
            if row[0] == '' and type2on == False:
                signifier = 1
                continue
            # row with a section header in it
            if (signifier == 1 and row[1] != '') or i == 0:
                data.append([row[0]])
                data[i].append(0)
                signifier = 0
                i += 1
                continue
            # row with a type 1 question in it
            if row[1] != '' and signifier == 0 and type2on == False:
                data.append([row[0]])
                data[i].append(1)
                data[i].append({})
                for j in range(1, 12):
                    data[i][2][int(j)] = int(row[j])
                i += 1
                continue
            # rows with type 2 questions in them
            if signifier == 1 and row[1] == '':
                data.append([row[0]])
                data[i].append(2)
                data[i].append([])
                type2q = row[0]
                type2on = True
                signifier = 0
                continue
            # rows with answers to type 2 questions in them
            if type2on and row[0] != '':
                data[i][2].append(row[0])
                continue
            # finish type 2 question responses
            if type2on and row[0] == '':
                type2on = False
                i += 1
                signifier = 1
                continue

    if DEBUG:
        for i in range(0, len(data)):
            print(data[i])
        print("Survey Count: " + str(surveyCount))
    return surveyCount






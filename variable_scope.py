import datetime
invalidDate1 = 'True'

def validateDateStringAndGetDate(dateText):
    global invalidDate1
    print("invalid Date",invalidDate1)
    try:
        # print("invalidDate",invalidDate)
        # datetime.date.fromisoformat(dateText)
        invalidDate1 = False
    except:
        # print("invalidDate",invalidDate)
        # invalidDate = True
        print("Error: Incorrect data format, should be YYYY-MM-DD")
        
while invalidDate1:
    dateOfExpense = input('Enter date of expense in YYYY-MM-DD format: ')
    validateDateStringAndGetDate(dateOfExpense)
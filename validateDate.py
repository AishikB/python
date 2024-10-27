import datetime

def validateDate(dateText):
    try:
        return datetime.date.fromisoformat(dateText)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

date = validateDate('2022-03-21')
print(date.day)
print(date.month)
print(date.year)

print(type('asca').__name__)
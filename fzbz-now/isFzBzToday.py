# import pandas as pd
# today = pd.Timestamp.today()
# day_of_year = today.day_of_year
# print(f"Day of the year: {day_of_year}")
# no internet, let us just use datetime

from datetime import datetime, date
# is fizz buzz today?
def isFzBzToday(input_date='', devisor1=3, devisor2=5):
  if input_date == '':
    input_date=date.today()
  else:
    input_date=datetime.strptime(date_string,'%Y-%m-%d').date()


  startOfYear = date(input_date.year, 1, 1)
  day = (input_date - startOfYear).days + 1

  print("*******************")
  print("Day of:")
  if day%devisor1 ==0 and day%devisor2 == 0 :
    print('FizzBuzz')
  else:
    if(day%devisor1==0):
      # Fizz
      print('Fizz')
    elif(day%devisor2==0):
      print('Buzz')
    else:
      print(f'{day}')



isFzBzToday()

print("\n*******************")

print("Find out day of the year or day of fizz buzz")
date_string = input("Y-m-d: ")

isFzBzToday(date_string)

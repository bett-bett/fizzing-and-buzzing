import subprocess
import time
import os
import sys
import fzbz_now.isFzBzToday as isFzBzToday

# Push code and alert me when the internet is connected


# 
# Tell me when the internet is back
# for I do not posses all the python libraries I need to start
# for my little machine at times gets amnesia
# for loosing data from reinstalled OS' never gets easier
# for pip sake
# for blue screens and corrupt partitions, 
# my machine shall not forsake me,
# it is git push, or machine to the bush 
# this is not the main show, read my README
# 

fzbz = isFzBzToday.isFzBzToday()

def my_changes():
  # git status --porcelain
  return None

def commit_and_push(message):
  # probably okay
  subprocess.run(['git', 'add', '.'])
  subprocess.run(['git', 'commit', '-m', message])
  subprocess.run(['git', 'push']) 

def has_internet():
  response = os.system("ping -n 1 google.com > nul")
  return response == 0


def play_sound():
  while True:
    try:
      # ... so fill your heart with what's important, and be done with all the rest ..
      subprocess.run(['mpv', '--loop', 'https://www.youtube.com/watch?v=GvP2oo8_dbs'])

    except KeyboardInterrupt:
      return


def spin(times):
  # borrowed and modified, will be reused again and agaain .. till I get good at multithreading
  for i in range(times):
    sys.stdout.write("\r{}".format(["/","|","\\","-"][i % 4]))
    sys.stdout.flush()
    time.sleep(1)



def main():
  while True:
    if has_internet():
      print(f"{fzbz}/365")
      commit_and_push(f"{fzbz}/365 - automated commit")
      play_sound()
      break
    else:
      spin(15)

if __name__ == '__main__':
  main()

  
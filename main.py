import models
import savepoints
import os

def main():
  os.system('clear')
  a = input('Input any Number : ')
  print(f'\n\nValue you have Entered is : {a}')
  
  b = input('Do you want to Continue [Y] : ')
  if b=='Y':
    os.system('python3 main.py')

if __name__=='__main__':
  main()
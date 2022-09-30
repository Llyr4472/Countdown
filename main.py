import time
import os


def inp():
   tim = input('Enter the countdown time in MM:SS format') 
   tim1 = tim2 = 0
   if tim.__contains__(':'):
     tim1 = int(tim.split(':')[0])
     tim2 = int(tim.split(':')[1])
   elif tim.isnumeric() == False:
          print('\n Invalid input\n')
          inp() 
   else:
     tim2 = int(tim)  
   tim = tim1 + tim2
   return tim , tim1 , tim2


def countdown(tim, t1, t2):
    os.system('cls')
    while t1+t2 > 0:
        if t2 == 0 :
            t2 = 60
            t1 -=1
        
        print(t1,':',t2)
        time.sleep(1)
        t2 -= 1

        os.system('cls')

def sound():
    import winsound


    winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)

def main():
   tim,tim1,tim2 = inp()
   if input("\nEnable Sound(y/n)") == 'y' or 'Y':
        Sound = True
   else:
        Sound = False 
   countdown(tim,tim1,tim2)
   print('The countdown is over!')
   if Sound == True:
        sound() 
   input()


if __name__ == "__main__":
    main()

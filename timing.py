import time
def calculate_time(func):
     '''This calculate time is here because its the main function'''
     def wrapper():
      '''You would need this function because it prints out time'''
      x = time.time()
      time.sleep(2)
      print(x)
      func()
     return wrapper

@calculate_time

def print_time():
    '''The reason to write this function is because it prints out the phase'''
    print('Total time X')


print_time()





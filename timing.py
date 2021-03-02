import time
def calculate_time(func):
     '''This calculate time is here because its the main function'''
     def wrapper():
      '''You would need this function because it prints out time'''
      X= time.time()
      func()
      print(f"Total time {X}")
     return wrapper

@calculate_time
def test_time():
      time.sleep(2)
test_time()







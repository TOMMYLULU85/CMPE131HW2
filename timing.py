import time
def calculate_time(func):
     '''This calculate time is here because its the main function'''
     def wrapper():
      '''You would need this function because it prints out time'''
      x = time.time()
      func()
      y = time.time()
      print(f"Total time {int(y)-int(x)}")

     return wrapper

@calculate_time
def test_time():
      time.sleep(2)
test_time()







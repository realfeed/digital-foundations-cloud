import datetime

class Printer():

    def hello_world(self):
        # This function prints Hello, world!
        print('Hello, world!')

    def time_now(self):
        # This function prints the current UTC datetime
        now = datetime.datetime.utcnow()
        print(now.strftime('%d/%m/%Y, %H:%M:%S'))

import datetime, time
import pytz
import sys
from yahoo_fin import stock_info
from threading import Thread

IST = pytz.timezone('Asia/Kolkata')
now_date_time = datetime.datetime.now(tz=IST)
thread_list = []

log_path = "lessthan100.txt"
sys.stdout = open(log_path, "a+")

start = time.time()

with open("input.txt") as file:
    names = [name.rstrip() for name in file.readlines()]

def get_price(name):
    price = stock_info.get_live_price(name)
    if price <= 100:
        print(name)

for name in names:
    thread = Thread(target=get_price, args = (name,))
    thread_list.append(thread)
for thread in thread_list:
    thread.start()
    thread.join()

end = time.time()

timetook = end-start

print(f"Total Time : {timetook}")
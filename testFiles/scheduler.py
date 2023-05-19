import sched
import time

# define a function to be run
def my_func():
    print("Hello, World!")

# create a scheduler object
scheduler = sched.scheduler(time.time, time.sleep)

# schedule the function to run every 5 seconds
def run_every_five():
    scheduler.enter(5, 1, run_every_five, ())
    my_func()

run_every_five()

# start the scheduler
scheduler.run()

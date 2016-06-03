import webbrowser
import time

total_breaks = 3
break_count = 0

print ("this progam started")
while (break_count < total_breaks):
    time.sleep(3)
    print break_count
    break_count = break_count + 1
print 'Done'

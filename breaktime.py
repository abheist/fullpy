"""
This program is prompting the user every two hours to take a break
abd open a google to search something different.
	repeat three times
		- wait for 2 hours
		- open browser
"""
import webbrowser
import time

total_breaks = 3
break_count = 0


print("This program started on:"+ time.ctime())
while(break_count < total_breaks):
	time.sleep(2 * 60 * 60)
	webbrowser.open("http://google.com/")
	break_count = break_count + 1

# for x in range(3):
# 	time.sleep(10)
# 	webbrowser.open_new("http://google.com")
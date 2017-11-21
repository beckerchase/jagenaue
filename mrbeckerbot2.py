#homegrown beckerbot
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#configure the driver
driver = webdriver.Chrome()

#access the page
url = "https://web.whatsapp.com"

driver.get(url)
#insert user input to allow time for login via mobile QR code
print("**** NOTICE: Hit any key to proceed once logged in. ****")
input()
print("Great! ready to rock?")

#define the core chatbot function
def beckerbot():
    #ask user for the search thread
    print("Q: What chat do you wish to open?")
    convo = input()

    #select the search box element
    search_box = driver.find_element_by_class_name("input-search")

    #enter the string into the search box & press ENTER
    search_box.send_keys(convo, Keys.ENTER)

    #select the active element (which should be the text box)
    box = driver.switch_to_active_element()

    #send stuff!
    print("Q: What do you want to send?")
    msg = input()
    box.send_keys(msg, Keys.ENTER)

#run the function
print("HIT ANY KEY TO START")
input()
beckerbot()
print("Do you want to play again? [1 = YES, ELSE NO]")
ans = int(input())
if ans == 1:
    beckerbot()
else:
    print("OK - my work here is done!")

#Sign off for the night
print("ALL DONE!")
time.sleep(3)
#THE END

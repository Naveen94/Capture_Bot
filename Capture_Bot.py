import csv
import cv2
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver

#Download the Selenium driver for chrome and load the appropriate path - Can also use Firefox and IE as well

driver=webdriver.Chrome(executable_path="fakepath\chromedriver.exe") 

#change to http if required

param = 'https://'

#list of domains such as www.sampleurl.com

csv_input = open('fakepath\<filename>.csv', "rb")
reader  = csv.reader(csv_input)
urls = []
for row in reader:
	urls.append(row[0])

csv_input.close()


#create a list of urls in a desired format like - https://www.sampleurl.com

complete_urls = [param + client_url for client_url in urls]  
driver.maximize_window()


i=0
for complete_url in complete_urls:
        # Logic to open the browser and load URLs
        driver.get(complete_url)
        #Logic to take screenshot of the webpage
	driver.save_screenshot("fakepath\%s.png" % urls[i]) 
        #Logic to add URL name to the image
	image = cv2.imread("fakepath\%s.png" % urls[i])
	texted_image =cv2.putText(image ,text="%s" % complete_url, org=(800,200),fontFace=2, fontScale=2, color=(0,0,255), thickness=5)
        cv2.imwrite("fakepath\%s.png" % urls[i],texted_image)
	i=i+1

# close the browser window
driver.quit()




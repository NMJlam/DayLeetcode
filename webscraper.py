from selenium import webdriver
import time

'''
- scrape everything on first page 
- learn db 
'''

driver = webdriver.Chrome()
driver.get('https://leetcode.com/problemset/') 

time.sleep(20)

driver.quit()
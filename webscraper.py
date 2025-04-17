from selenium import webdriver
import time

'''
- scrape everything on first page 
    - name 
    - number 
    - difficulty 
    - acceptance rate 
    - premium or not 
        - NON-PREM: solution from the editorial (based on leetcode soln / highest upvotes) 
'''


driver = webdriver.Chrome()
driver.get('https://leetcode.com/problemset/') 

time.sleep(20)

driver.quit()
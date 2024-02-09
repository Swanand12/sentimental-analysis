import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

url = "https://www.thehindu.com/news/national/"

driver = webdriver.Chrome()

try:

    driver.get(url)
    count = 0
    num = 0
     
    while num < 100:
        wait = WebDriverWait(driver, 10)
        show_more_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'show-more')))
        actions = ActionChains(driver)
        actions.click(show_more_button).perform()
        time.sleep(3)
        num += 1
           
    updated_html = driver.page_source
    soup = BeautifulSoup(updated_html, 'html.parser')

    headlines = soup.find_all("h3",{"class":"title big"})
    for headline in headlines:
        if "budget" in headline.text:
            count = count + 1
            print("\n" + str(count) + ".")
            print("Title: ",headline.text.strip())
        
            headline_link = headline.find('a')['href']
            driver.get(headline_link)

            individual_headline_pageSource = driver.page_source
            individual_headline_soup = BeautifulSoup(individual_headline_pageSource,'html.parser')

            date = individual_headline_soup.find("p",{"class":"publish-time"})
            date_text = date.text
            publish_date = date_text.split('|')[0].strip()
            print("Publish_date: " ,publish_date)

            author = individual_headline_soup.find("div",{"class":"author"})
            print("Author: " ,author.text)
        
            dash_index = date_text.find('-')
            if(dash_index != -1):
                print("Location: " ,date_text[dash_index + 1:].strip())
            else:
                print("Location: None")

            driver.back()

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()

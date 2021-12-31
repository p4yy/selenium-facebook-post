#automating posting in facebook social media with selenium Python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import json

def main():
    data = json.load(open('configWeb.json', 'r'))
    usr=data["username"] 
    pwd=data["password"]
    option = Options()
    option.add_argument("--disable-infobars")
    #option.add_argument("--window-size=800,600")
    option.add_argument("--disable-extensions")
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2 }) 
    driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver\\chromedriver.exe')
    #Get request facebook.com
    driver.get('https://www.facebook.com/')
    print ("Opened facebook")
    sleep(5) 
    #Write username find by id Email
    username = driver.find_element_by_id('email')
    username.send_keys(usr)
    #write password find by id pass
    print ("Email Id entered")
    passwd = driver.find_element_by_id('pass')
    passwd.send_keys(pwd)
    print ("Password entered")
    #clicking submit find by name login
    login = driver.find_element_by_name('login')
    login.click()
    sleep(5)
    #get request to url user fb example facebook.com/payy23
    url_fb = data["url_user"]
    driver.get(url_fb)
    sleep(9)
    #START AND END config in json file
    start=data["start"]
    end=data["end"]
    teks = data["teks"]
    tagPeople = data["tagPeople"]
    delayPost = data["delayPost"]
    breakEveryPostOn = data["breakEveryPostOn"]
    sleepAt = 1
    while start <= end:
        if sleepAt - breakEveryPostOn[0] == 0:
            sleep(breakEveryPostOn[1])
            sleepAt = 1
        sleep(1)
        postWindow = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/span')
        postWindow.click()
        sleep(2)
        for x in teks:
            actions = ActionChains(driver)
            actions.send_keys(x)
            actions.send_keys(Keys.ENTER)
            actions.perform()
        sleep(1.5)
        actionsHash = ActionChains(driver)
        actionsHash.send_keys("#"+str(f'{start:,}'))
        actionsHash.send_keys(Keys.ENTER)
        actionsHash.perform()
        sleep(2)
        for i in tagPeople:
            actions = ActionChains(driver)
            actionsEnter = ActionChains(driver)
            actionsEnter2 = ActionChains(driver)
            actions.send_keys("@")
            actions.send_keys(i+" ")
            actions.perform()
            sleep(4.5)
            actionsEnter.send_keys(Keys.ENTER)
            actionsEnter.perform()
            sleep(1)
            actionsEnter2.send_keys(Keys.ENTER)
            actionsEnter2.perform()
        sleep(1.5)
        #click posting
        varPost = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]')
        varPost.click()
        sleep(delayPost)
        print(f"Post #{start}")
        start+=1
        sleepAt+=1

if __name__ == "__main__":
    main()
#John Schuster
#jschuster@ridedart


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from passwdStuff import whatPasswd
import time, datetime



websiteThing = 'https://10.1.100.100/login?CSRFKey=7658bc1b-a22a-8c3f-66da-626c4b833e1d&referrer=https%3A%2F%2F10.1.100.100%2Fdefault'
whitelistLoc = "https://10.1.100.100/prod/web/10_0/web_security_manager/custom_policy_elements/custom_url_categories"
bypasslistLoc = 'https://10.1.100.100/prod/web/10_0/web_security_manager/global_settings/bypass_proxy'
myPassword = whatPasswd('CiscoWebApp')
timeUp = 10

if __name__ == '__main__':

    CurrentDay = time.strftime("%e%b%y%S",time.localtime())
    ScreenStuff = CurrentDay +"WebProxyInfo.txt"  
    f = open(ScreenStuff, "a+")


    #options to bypass ssl errors
    options = webdriver.chrome.options.Options()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    #open webdriver and browser
    browser = webdriver.Chrome(executable_path = r"C:\Temp\chromedriver.exe", options=options)    
    #navigate to page
    browser.get(websiteThing)

    wait = WebDriverWait( browser, 5)
    time.sleep(timeUp)
    #find user name
    usernameBox = browser.find_element_by_xpath('//*[@id="table_form_login"]/tbody/tr[1]/td/input')

    #enter user name
    usernameBox.send_keys(myPassword['User'])

    #find password
    passwordBox =  browser.find_element_by_xpath('//*[@id="table_form_login"]/tbody/tr[2]/td/input[2]')

    #enter password
    passwordBox.send_keys(myPassword['Password'])

    #find login button and click
    submit = browser.find_element_by_xpath('//*[@id="table_form_login"]/tbody/tr[3]/td/input')
    submit.click()
    #wait for the browser to load
    wait = WebDriverWait( browser, 15)
    time.sleep(timeUp)

    #get page title and ensure we are in

#    pageTitle = browser.title
#    assert (pageTitle == 'Cisco Content Security Management Virtual Appliance M100V (10.1.100.100) - Centralized Services > System Status')

    #wait = WebDriverWait( browser, 15)
    # goto the whitelist table
    browser.get(whitelistLoc)

    wait = WebDriverWait( browser, 15)
    time.sleep(timeUp)

    #click on the Whitelist URL
    submit = browser.find_element_by_xpath('//*[@id="form"]/dl/dd/table/tbody/tr[3]/td[2]/a')
    submit.click()

    wait = WebDriverWait( browser, 15)
    time.sleep(timeUp)

    #copy the whitelist
    whiteList = browser.find_element_by_xpath('//*[@id="category_urls"]').text

    #write it to the txt file
    f.write('Whitelist is below:\n')
    f.write(whiteList+'\n')

    #go back to the whitelist table
    browser.get(whitelistLoc)

    wait = WebDriverWait( browser, 15)
    time.sleep(timeUp)

    #click on the Blacklist URL
    submit = browser.find_element_by_xpath('//*[@id="form"]/dl/dd/table/tbody/tr[6]/td[2]/a')
    submit.click()

    wait = WebDriverWait( browser, 15)
    time.sleep(timeUp)

    #copy the Blacklist
    blackList = browser.find_element_by_xpath('//*[@id="category_urls"]').text

    #write it to the txt file
    f.write("Blacklist is below:\n")
    f.write(blackList+'\n')

    #go to the bypasslist table
    browser.get(bypasslistLoc)

    wait = WebDriverWait( browser, 15)
    time.sleep(timeUp)

    #copy the bypasslist 
    bypassList = browser.find_element_by_xpath('//*[@id="form"]/dl/dd/table/tbody/tr/td').text

    #write it to the txt file
    f.write("bypasslist is below:\n")
    f.write(bypassList+'\n')

    browser.quit()
    f.close()
    
    

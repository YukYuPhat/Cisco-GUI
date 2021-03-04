#John Schuster
#jschuster@ridedart


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from passwdStuff import whatPasswd




websiteThing = 'https://10.1.100.100/login?CSRFKey=7658bc1b-a22a-8c3f-66da-626c4b833e1d&referrer=https%3A%2F%2F10.1.100.100%2Fdefault'
whitelistLoc = "https://10.1.100.100/prod/web/10_0/web_security_manager/custom_policy_elements/custom_url_categories?action=FormEdit&amp;cat_code=1090519041&amp;CSRFKey=14210ad2-8b7c-6c9a-f15e-b455fa022cfa"
blacklistLoc = "https://10.1.100.100/prod/web/10_0/web_security_manager/custom_policy_elements/custom_url_categories?action=FormEdit&amp;cat_code=1090519042&amp;CSRFKey=14210ad2-8b7c-6c9a-f15e-b455fa022cfa"
bypasslistLoc = 'https://10.1.100.100/prod/web/10_0/web_security_manager/global_settings/bypass_proxy'
myPassword = whatPasswd('CiscoWebApp')


if __name__ == '__main__':

    #options to bypass ssl errors
    options = webdriver.chrome.options.Options()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    
    #open webdriver and browser
    browser = webdriver.Chrome(executable_path = r"C:\Temp\chromedriver.exe", options=options)    
    #navigate to page
    browser.get(websiteThing)

    wait = WebDriverWait( browser, 5)
    
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
    wait = WebDriverWait( browser, 5)
    
    #get page title and ensure we are in
    
    pageTitle = browser.title
    assert (pageTitle == 'Cisco Content Security Management Virtual Appliance M100V (10.1.100.100) - Centralized Services > System Status')
    
    wait = WebDriverWait( browser, 5)
    
    browser.quit()
    
    
    

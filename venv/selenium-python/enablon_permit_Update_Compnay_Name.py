from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path='/usr/bin/chromedriver')
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

# options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#url = "https://lendlease.uat.ap.enablon.io/dashboard/"
url = "https://lendlease.uat.ap.enablon.io/permitvision/visioncontrol/userManagement"
driver.get(url)

driver.maximize_window() # For maximizing window
driver.implicitly_wait(30)

print(driver.current_url)
time.sleep(10)
username = driver.find_element(By.ID, "UserName")
password = driver.find_element(By.ID, "Password")

username.send_keys("_svc-enablon_appUsecase@lendlease.com")
password.send_keys("$758vE4!m~WS")


driver.find_element(By.NAME, "submitAction").click()
print("Login SuccessFully")
time.sleep(60)
# Serach the User Details
name = driver.find_element(By.XPATH, "//*[@id='reactContainer']/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/input")
name.send_keys("alex.oshaughnessy01@gmail.com")
time.sleep(10)
name.send_keys(Keys.ENTER)
time.sleep(10)
# Print the User Detatils
link = driver.find_elements(By.TAG_NAME, 'dl')
print(len(link))
link_dl = driver.find_elements(By.TAG_NAME, 'dl')
for links in link_dl:
    print(links.text)
time.sleep(5)
# Click on the Result after entering the user's mail id
driver.find_element(By.XPATH, "//*[@id='reactContainer']/div/div/div[1]/div/div/div[2]/ul/li[1]").click()
# Check the Total record in the Drop Down Items
drop_down_link = driver.find_elements(By.CLASS_NAME, 'dropdown-item')
print(len(drop_down_link))
drop_down_linklink_dl = driver.find_elements(By.CLASS_NAME, 'dropdown-item')
# Create Empty List and store all the company name in the list
compnay_list = []
for dlinks in drop_down_linklink_dl:
    html = dlinks.get_attribute("innerHTML")
    #print(html)
    compnay_list.append(html)
#print(compnay_list)
print(len(compnay_list))
print("All the compnay name has been stored in the file.")
# find out the index number for given compnay name
company_index_number = compnay_list.index('<span class=""><span>1 JAVA VENTURE LLC DBA</span></span>')
print(company_index_number)

# delete the record before first company name from the list
del compnay_list[0:company_index_number]
print(len(compnay_list))
print("Company Name has been deleted from the list")
#print(step2)
time.sleep(5)
# stored all the company name in the text file
f = open("kumarsachinkumar.txt", "w")
for comp in compnay_list:
    f.write(comp + '\n')
print("New File created with the remaining company Name")
time.sleep(5)
# remove the html tags from the compnay name
comp = []
with open("kumarsachinkumar.txt", "r") as f:
    for line, row in enumerate(f.read().splitlines()):
        #print(row)
        s = row.replace('<span class=""><span>','')
        new = s
        line = new.replace('</span></span>','')
        #print(line)
        comp.append(line)
    #print(comp)
    print("Remove the Prefix and postfix from the company name")
    print(len(comp))
    # Sort all the company name with alphabetically
    s = sorted(comp, key=str.lower)
    #print(s)
# after sorting store all the company name in a text file
    f = open("sort.txt", "w")
    for comp in s:
        f.write(comp + '\n')
# find the index number where the company name is exist in the text file (Sort.txt)
company_search_name = "Stoddart"
with open("sort.txt", "r") as f:
    # x = len(f.readlines())
    # print(x)
    for line, row in enumerate(f.read().splitlines()):
        if re.findall('\\b'+company_search_name+'\\b', row, flags=re.IGNORECASE):
            print('Name "{0}" found in line {1}'.format(company_search_name, line))
            comp_id = line + 1
            print("This is Your final Compnay Index ID: " + str(comp_id))
            print("Done !!!")

# pass the company number and update the company name
carDropdown = driver.find_element(By.XPATH, "//*[@id='user-editor-tabs-pane-editUserDetails']/div/div[4]/div[1]/div[2]/div/button")
ActionChains(driver).click(carDropdown).perform()
time.sleep(3)
myOption = driver.find_element(By.XPATH, f"//*[@id='user-editor-tabs-pane-editUserDetails']/div/div[4]/div[1]/div[2]/div/ul/li[{comp_id}]/div")
ActionChains(driver).click(myOption).perform()
saveButton = driver.find_element(By.XPATH, "//*[@id='saveButton']")
ActionChains(driver).click(saveButton).perform()
time.sleep(1)
print("company name has been Upated for Given User")
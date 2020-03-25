from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

user_instagram = input('Type your instagram user: ')
password_instagram = input('Type your password: ')
users_list = []
while True:
    users_list.append(input('Type the instagram user that you want to send a message: '))
    option = input('Somebody else [Y/N]?').upper()
    if option[0] == 'N':
        break
print('Type the message that you want to send to the selected users:')
message = input()

driver = webdriver.Chrome(r"C:\Users\lucas\OneDrive\Documentos\chromedriver")
driver.get('https://www.instagram.com/')
sleep(4)
loginBox = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
loginBox.send_keys(user_instagram)
passwordBox = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
passwordBox.send_keys(password_instagram)
loginButton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
loginButton.click()
sleep(4)
notificationButton = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
notificationButton.click()
c = 0
for insta_user in users_list:
    if c == 0:
        directButton = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
    else:
        directButton = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[2]/a')
    directButton.click()
    sleep(1)
    messageButton = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button')
    messageButton.click()
    name_message = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/div[2]/input')
    name_message.send_keys(insta_user)
    sleep(1)
    messageButton2 = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div/div/div[3]/button')
    messageButton2.click()
    sleep(1)
    nextButton = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/div/button')
    nextButton.click()
    sleep(2)
    messageArea = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div/textarea')
    messageArea.send_keys(f'Olá {insta_user}! ', message, Keys.ENTER)
    c += 1
print('The message was sent to all the users selected with success!')


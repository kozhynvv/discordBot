import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver as swdriver


pass_item_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                  '9', '0']

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
           'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']


def generate_pass():
    password = ''
    for _ in range(12):
        password += random.choice(pass_item_list)
    return password


def create_acc(browser, email, nickname, pas):
    browser.get('https://discord.com/register')
    time.sleep(10)

    date = str(random.randint(1, 28))
    month = random.choice(months)
    year = str(random.randint(1970, 2004))
    time.sleep(2)

    input_email = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[1]/div/input')
    input_email.click()
    input_email.clear()
    input_email.send_keys(email)
    time.sleep(random.randint(1, 2))

    input_nick = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[2]/div/input')
    input_nick.click()
    input_nick.clear()
    input_nick.send_keys(nickname)
    time.sleep(random.randint(1, 2))

    input_password = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[3]/div/input')
    input_password.click()
    input_password.clear()
    input_password.send_keys(pas)
    time.sleep(random.randint(1, 2))

    date_of_brth = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/fieldset/div[1]/div[1]/div/div/div/div/div[1]')
    date_of_brth.click()
    actions = ActionChains(browser)
    actions.send_keys(date).perform()
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(random.randint(1, 2))

    month_of_brth = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/fieldset/div[1]/div[2]/div/div/div/div/div[1]')
    month_of_brth.click()
    actions = ActionChains(browser)
    actions.send_keys(month).perform()
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(random.randint(1, 2))

    year_of_brth = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/fieldset/div[1]/div[3]/div/div/div/div/div[1]')
    year_of_brth.click()
    actions = ActionChains(browser)
    actions.send_keys(year).perform()
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(random.randint(1, 2))

    browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[5]/button').click()
    time.sleep(30)

    for request in browser.requests:
        try:
            token = request.headers['authorization']
            if token:
                print(f'\nВаш пароль: {password}\n\nTOKEN: {token}')
                break
        except Exception as e:
            print(f'ERROR: {e}')
            pass

    try:
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/section/div[2]/div[2]/button[3]').click()
        time.sleep(random.randint(2, 3))
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[34]/div').click()
        time.sleep(random.randint(2, 3))
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div/div[3]/button[1]').click()
        time.sleep(random.randint(2, 3))
    except:
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[4]/div/div[2]/div[3]/div[3]/a').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div/div[3]/button[1]').click()
        time.sleep(random.randint(1, 3))

    browser.close()
    browser.quit()


with open('user-agents.txt', 'r') as f:
    file = f.read().splitlines()


if __name__ == '__main__':
    password = generate_pass()
    while True:
        em = input('Введите почту: ')
        if ' ' in em or '@' not in em:
            print('Введите почту в формате "yourmail@domen"!')
            continue
        else:
            break

    while True:
        nk = input('Введите никнейм: ')
        if ' ' in nk:
            print('Никнейм не может содержать пробелов!')
            continue
        else:
            break

    agent = random.choice(file)

    # Create acc
    opts = Options()
    opts.add_argument('--allow-profiles-outside-user-dir')
    opts.add_argument('--enable-profile-shortcut-manager')
    opts.add_argument("--profile-directory=Profile 9")
    opts.add_argument('user-data-dir=C:\\Users\\Владислав\\PycharmProjects\\testTaskDiscord')
    opts.add_argument(f"user-agent={agent}")
    browser = swdriver.Chrome(chrome_options=opts)
    try:
        create_acc(browser, em, nk, password)
    except:
        print('Такая почта или ник уже используются!')



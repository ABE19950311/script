from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


def scryping():
    # # Optionsにヘッダーレスで動かす命令を足す
    # options = Options()
    # options.add_argument('--headless')

    #Google Chromeを開く
    driver = webdriver.Chrome()

    #ページ読み込み
    driver.get("https://scraping-for-beginner.herokuapp.com/")
    time.sleep(1)

    # aタグ（ログイン）をクリック
    login_a = driver.find_element(By.XPATH, '//a[text()="ログイン"]')
    # JavaScriptを使用して要素をクリックする
    driver.execute_script("arguments[0].click();", login_a)
    # ページ遷移を待つ
    time.sleep(1)  

    #loginformの要素取得
    login_user_input = driver.find_element(By.ID,value="username")
    login_passwd_input = driver.find_element(By.ID,value="password")
    login_btn = driver.find_element(By.ID,value="login-btn")

    #取得した要素に値入力
    login_user_input.send_keys("imanishi")
    login_passwd_input.send_keys("kohei")

    #btnクリックする
    login_btn.click()
    time.sleep(1) 

    #一括取得するときはdriver.find_element"s"を使う
    #ふだんはdriver.find_element
    key = []
    value = []
    keys = driver.find_elements(By.TAG_NAME,"th")
    values = driver.find_elements(By.TAG_NAME,"td")
    
    for elm in keys:
        key.append(elm.text)

    for elm in values:
        value.append(elm.text)

    print(key)
    print(value)

    # html = driver.page_source.encode("utf-8")
    # obj = BeautifulSoup(html,"html.parser")
    # print(obj)

    driver.close()
    driver.quit()

def main():
    scryping()

if __name__ == "__main__":
    main()

#https://scraping-for-beginner.readthedocs.io/ja/latest/
#https://qiita.com/std-flower/items/b6208eccc5f27ed8b034
#https://qiita.com/Moh_no/items/a835f77b6b4e3972fbbe
#https://selenium-python.readthedocs.io/getting-started.html#simple-usage
#https://developer.chrome.com/docs/chromedriver/get-started?hl=ja
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#pip install selenium
#pip install bs4
#https://www.selenium.dev/documentation/webdriver/elements/finders/
#https://www.reddit.com/r/selenium/comments/y34uhg/find_element_by_link_text_problem/
#https://note.com/yucco72/n/neef7e680786e
#https://shirako-design.com/blog/marketing/selenium/
#https://qiita.com/RisaM/items/da3650243005dcc25680
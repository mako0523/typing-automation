from time import sleep
from typing import Final

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

TYPING_SITE_URL: Final = "https://typing.twi1.me/game/18574"
REPEAT_TIMES: Final = 100
TYPING_TEXT: Final = "aiueo" * REPEAT_TIMES


def init_driver() -> WebDriver:
    options: Final = webdriver.ChromeOptions()
    driver: Final = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub", options=options
    )
    driver.implicitly_wait(10)
    return driver


def type_automatically(driver: WebDriver, typing_text: str) -> None:
    driver.find_element(By.CLASS_NAME, "mtjSeSc-settingBtn").click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, "mtjStSc-startBtn").click()
    sleep(2)
    body_element: Final = driver.find_element(By.TAG_NAME, "body")
    body_element.send_keys(Keys.SPACE)
    body_element.send_keys(typing_text)


driver: Final = init_driver()
driver.get(TYPING_SITE_URL)
sleep(2)
type_automatically(driver, TYPING_TEXT)
sleep(2)

result_img: Final = driver.find_element(By.CLASS_NAME, "mtjRsSc").screenshot_as_png
with open("./downloads/result.png", "wb") as f:
    f.write(result_img)

input()
driver.quit()

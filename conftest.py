from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Firefox('D:\\SkillFactory\\')

   pytest.driver.set_window_size(1300, 700)
   # Переходим на страницу авторизации
   pytest.driver.get('https://petfriends.skillfactory.ru/login')

   yield


   pytest.driver.quit()
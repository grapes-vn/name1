import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Firefox(executable_path=r'/home/grapes/firefoxdriver')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   #element = WebDriverWait(pytest.driver, 10).until(pytest.driver.find_element_by_id('email'))
   pytest.driver.find_element_by_id('email').send_keys('grapes-vn@ngs.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('PetVin17')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Нажимаем на ссылку Мои питомцы
   #my_pets = WebDriverWait(pytest.driver, 5).until(pytest.driver.find_element_by_link_text('Мои питомцы'))
   #my_pets.click()
   pytest.driver.find_element_by_link_text('Мои питомцы').click()
   # Проверяем, что мы оказались на странице Мои питомцы пользователя
   assert pytest.driver.find_element_by_tag_name('h2').text == "grapes-vn"

   # Проверяем, что кол-во питомцев в таблице совпадает с счётчиком питомцев
   pets = pytest.driver.find_elements_by_xpath('//tbody/tr')
   counters = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text
   counter_pets = int(counters.split("\n")[1].split(": ")[1])
   assert len(pets) == counter_pets

   # Проверяем, что хотя бы у половины питомцев есть фото
   pytest.driver.implicitly_wait(10)
   pets_without_photo = pytest.driver.find_elements_by_xpath('//img[@src=""]')
   assert counter_pets // 2 >= len(pets_without_photo)

   pytest.driver.implicitly_wait(10)
   names = pytest.driver.find_elements_by_xpath('//tbody/tr/td[1]')
   pytest.driver.implicitly_wait(10)
   breeds = pytest.driver.find_elements_by_xpath('//tbody/tr/td[2]')
   pytest.driver.implicitly_wait(10)
   age = pytest.driver.find_elements_by_xpath('//tbody/tr/td[3]')


   list_of_names = []
   list_of_breeds = []
   list_of_age = []

   for i in range(len(names)):
      # Проверяем, что у всех питомцев есть имя, возраст и порода
      assert names[i].text != ''
      assert breeds[i].text != ''
      assert age[i].text != ''
      list_of_names.append(names[i].text)
      list_of_breeds.append(breeds[i].text)
      list_of_age.append(age[i].text)
   # Проверяем, что у всех питомцев разные имена
   assert len(list_of_names) == len(set(list_of_names))
   # Проверяем, что в списке нет повторяющихся питомцев
   for i in range(len(list_of_names)):
      for j in range(i+1, len(list_of_names)):
         assert list_of_names[i] != list_of_names[j] or list_of_breeds[i] != list_of_breeds[j] or list_of_age[i] != list_of_age[j]
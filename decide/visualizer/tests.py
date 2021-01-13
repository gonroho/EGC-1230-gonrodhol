
# # Generated by Selenium IDE
from django.test import TestCase


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image


class TestContactUs():
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.fullscreen_window()
  
    def test_contactUs(self):
        self.driver.get("https://picaro-decide.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("picarodecide")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://picaro-decide.herokuapp.com/visualizer/5/")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary:nth-child(2)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > h2").text == "Contact Info"

    def tearDown(self):
        self.driver.quit()

class TestContactUsBack():
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.fullscreen_window()
  
    def test_contactUsBack(self):
        self.driver.get("https://picaro-decide.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("picarodecide")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://picaro-decide.herokuapp.com/visualizer/5/")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary:nth-child(2)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > h2").text == "Contact Info"
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
        assert self.driver.find_element(By.ID, "saveAsPNG1").text == "Save as PNG"

    def tearDown(self):
        self.driver.quit()

class TestDarkMode():
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.fullscreen_window()
  
    def test_darkMode(self):
        self.driver.get("https://picaro-decide.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("picarodecide")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://picaro-decide.herokuapp.com/visualizer/5/")
        self.driver.find_element(By.ID, "darkButton").click()
        assert self.driver.find_element_by_tag_name('body').get_attribute("class") == "bg-dark"
        assert self.driver.find_element(By.ID, "lightButton").text == "Light mode" 

    def tearDown(self):
        self.driver.quit()

class TestLightMode():
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.fullscreen_window()
  
    def test_lightMode(self):
        self.driver.get("https://picaro-decide.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("picarodecide")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://picaro-decide.herokuapp.com/visualizer/5/")
        self.driver.find_element(By.ID, "darkButton").click()
        self.driver.find_element(By.ID, "lightButton").click()
        assert self.driver.find_element_by_tag_name('body').get_attribute("class") == "bg-light"
        assert self.driver.find_element(By.ID, "darkButton").text == "Dark mode" 

    def tearDown(self):
        self.driver.quit()


class TestAboutUs():
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.fullscreen_window()
  
    def test_aboutUs(self):
        self.driver.get("https://picaro-decide.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("picarodecide")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://picaro-decide.herokuapp.com/visualizer/5/")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-group > .btn:nth-child(3)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(2) > .card-title").text == "Abraham"
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(3) > .card-title").text == "Martín Arturo"
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(4) > .card-title").text == "Gabriel"
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(5) > .card-title").text == "Thibaut"
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(6) > .card-title").text == "David"
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(1) > .card-title").text == "Pablo"

    def tearDown(self):
        self.driver.quit()

class TestAboutUsBack():
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.fullscreen_window()
  
    def test_aboutUsBack(self):
        self.driver.get("https://picaro-decide.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("picarodecide")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://picaro-decide.herokuapp.com/visualizer/5/")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-group > .btn:nth-child(3)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(2) > .card-title").text == "Abraham"
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(3) > .card-title").text == "Martín Arturo"
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(4) > .card-title").text == "Gabriel"
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(5) > .card-title").text == "Thibaut"
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(6) > .card-title").text == "David"
        assert self.driver.find_element(By.CSS_SELECTOR, ".columna:nth-child(1) > .card-title").text == "Pablo"
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
        assert self.driver.find_element(By.ID, "saveAsPNG1").text == "Save as PNG"

    def tearDown(self):
        self.driver.quit()

class TestPNG1PNG2PDF():
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.fullscreen_window()
 
    def testPNG1PNG2PDF(self):
        self.driver.get("https://picaro-decide.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("picarodecide")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://picaro-decide.herokuapp.com/visualizer/5/")
        #self.driver.find_element(By.CSS_SELECTOR, "#saveAsPDF").click()
        assert self.driver.find_element(By.ID, "saveAsPNG1").text == "Save as PNG"
        assert self.driver.find_element(By.ID, "saveAsPNG2").text == "Save as PNG"
        assert self.driver.find_element(By.ID, "saveAsPDF").text == "Save as PDF"
    def tearDown(self):
        self.driver.quit()



class TestDarkModeCookies():
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.fullscreen_window()
  
    def test_darkModeCookies(self):
        self.driver.get("https://picaro-decide.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("picarodecide")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://picaro-decide.herokuapp.com/visualizer/5/")
        self.driver.find_element(By.ID, "darkButton").click()
        assert self.driver.find_element_by_tag_name('body').get_attribute("class") == "bg-dark"
        assert self.driver.find_element(By.ID, "lightButton").text == "Light mode" 
        self.driver.find_element(By.CSS_SELECTOR, ".btn-group > .btn:nth-child(3)").click()
        assert self.driver.find_element_by_tag_name('body').get_attribute("class") == "bg-dark"

    def tearDown(self):
        self.driver.quit()

class TestLightModeCookies():
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.fullscreen_window()
    def test_lightModeCookies(self):
        self.driver.get("https://picaro-decide.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("picarodecide")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://picaro-decide.herokuapp.com/visualizer/5/")
        self.driver.find_element(By.ID, "darkButton").click()
        assert self.driver.find_element_by_tag_name('body').get_attribute("class") == "bg-dark"
        assert self.driver.find_element(By.ID, "lightButton").text == "Light mode"
        self.driver.find_element(By.ID, "lightButton").click()
        assert self.driver.find_element_by_tag_name('body').get_attribute("class") == "bg-light"
        assert self.driver.find_element(By.ID, "darkButton").text == "Dark mode" 
        self.driver.find_element(By.CSS_SELECTOR, ".btn-group > .btn:nth-child(3)").click()
        #Si esta en modo claro, al ser el modo por defecto, el backgraund es blanco, sin la necesidad de aplicar ningún cambio de CSS.
        assert self.driver.find_element_by_tag_name('body').get_attribute("class") == ""

    def tearDown(self):
        self.driver.quit()

class TestGraficaBarras():
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.fullscreen_window()
    def test_graficaBarras(self):
        self.driver.get("https://picaro-decide.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("picarodecide")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://picaro-decide.herokuapp.com/visualizer/5/")
        assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(2) > .heading").text == "Bar Chart"
        #Sacamos una captura de pantalla de la gráfica de barras para comprobar que esta existe, dentro de la imagen screenshotgraficabarras.png aparece esta gráfica, solo que aparece algo distosionada
        #las barras miden 1/5 menos de lo que miden en realidad, pero podemos comprobar que existe la gráfica y que tiene el número correcto de opciones.
        self.driver.find_element_by_id('myChart2').screenshot('screenshotgraficabarras.png')
        
    def tearDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     unittest.main()


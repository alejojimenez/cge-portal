from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from .code.time_service import sleep
# from .domain.chrome_node import By, ChromeNode

class Scraper():
    def __init__(self, url, email, password, driver_path):
        print(url, email, password, driver_path)
        self.url = url
        self.email = email
        self.password = password
        self.driver_path = driver_path
        self.driver = None

    # def close(self):
    #     self.driver.quit()

    def wait(self, seconds):
        return WebDriverWait(self.driver, seconds)
    
    def close(self):
        self.driver.close()
        self.driver = None

    def quit(self):
        self.driver.quit()
        self.driver = None
        
    def click_element_id(self, selector):
        print('Entrando en la funcion click_element_id')
        intentos = 0
        reintentar = True
        resultado = False
        while (reintentar):
            try:
                print('Try en la funcion click_element_id', intentos)
                intentos += 1
                self.wait(10).until(EC.presence_of_element_located((By.ID, selector)))
                self.wait(10).until(EC.element_to_be_clickable((By.ID, selector)))
                elemento = self.driver.find_element(By.ID, selector)
                print(elemento)
                elemento.click()
                reintentar = False
                resultado = True
            except Exception as e:  
                print('Exception en la funcion click_element_id', e)
                #sleep(10)
                reintentar = intentos <= 3
                resultado = False
        return resultado

    def click_element_xpath(self, selector):
        print('Entrando en la funcion click_element_xpath')
        intentos = 0
        reintentar = True
        resultado = False
        while (reintentar):
            try:
                print('Try en la funcion click_element_xpath', intentos)
                intentos += 1
                self.wait(10).until(EC.presence_of_element_located((By.XPATH, selector)))
                self.wait(10).until(EC.element_to_be_clickable((By.XPATH, selector)))
                elemento = self.driver.find_element(By.XPATH, selector)
                elemento.click()
                reintentar = False
                resultado = True
            except Exception as e:    
                print('Exception en la funcion click_element_xpath', e)
                #sleep(10)
                reintentar = intentos <= 3
                resultado = False
        return resultado
    
    def set_text_element(self, selector, text):
        print('Entrando en la funcion set_text_element')
        intentos = 0
        reintentar = True
        resultado = False
        while (reintentar):
            try:
                print('Try en la funcion set_text_element', intentos)
                intentos += 1
                self.wait(10).until(EC.element_to_be_clickable((By.ID, selector)))
                elemento = self.driver.find_element(By.ID, selector)
                elemento.send_keys(text)
                reintentar = False
                resultado = True
            except Exception as e:
                print('Exception en la funcion set_text_element', e)
                #sleep(10)
                reintentar = intentos <= 3
                resultado = False
        return resultado
        
    def login(self):
        print('Entrando en la funcion login')
        self.driver = webdriver.Chrome(self.driver_path)
        self.driver.get(self.url)
        self.driver.maximize_window()
        
        # gives an implicit wait for 20 seconds
        self.driver.implicitly_wait(20)

        # Esperar hasta 10 segundos a que el elemento esté presente en la página
        wait = WebDriverWait(self.driver, 30)

        # Esperar a que el elemento esté presente y visible en la página
        element = wait.until(EC.visibility_of_element_located((By.NAME, 'txtRutLoginE')))

        # Realizar acciones en el elemento, como ingresar texto o hacer clic en él
        element.send_keys('texto de ejemplo')
        

        #input_tipo_consulta = driver.find_element("name", "TIPOCONSULTA")
        #input_tipo_consulta.click()

        # self.driver.find_element("id", "#txtRutLoginE").send_keys(self.email)
        # self.driver.find_element("id", "#txtClaveLoginE").send_keys(self.password)
        # self.driver.find_element("id", "#imbIngresarLogin").submit()    
        # self.driver.implicitly_wait(20)
        
        # # Selección del campo de usuario
        # user_field = self.driver.find_element("link text", "Rut")
        # user_field.send_keys(self.email)
        
        # # Selección del campo de contraseña
        # password_field = self.driver.find_element("link text", "Contraseña")
        # password_field.send_keys(self.password)
        
        # # Enviar el formulario de inicio de sesión
        # login_button = self.driver.find_element("link text", "Ingresar")
        # login_button.click()        
        
        # user_field = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.LINK_TEXT, "Rut"))
        # ) #self.driver.find_element(By.ID, '#txtRutLoginE')
        # user_field.send_keys(self.email)
        
        # password_field = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.LINK_TEXT, "Contraseña"))
        # )#self.driver.find_element(By.ID, '#txtClaveLoginE')
        # password_field.send_keys(self.password)
        
        # password_field.send_keys(Keys.RETURN)
        
#################################

        # username_input_id = 'txtRutLoginE'
        # password_input_id = 'txtClaveLoginE'
        # submit_button_id = 'imbIngresarLogin'
        
        # self.click_element_id(username_input_id)
        # self.set_text_element(username_input_id, self.email)

        # self.click_element_id(password_input_id)
        # self.set_text_element(password_input_id, self.password)

        # self.click_element_id(submit_button_id)

        # username_input_xpath = '//input[@name="txtRutLoginE"]'
        # password_input_xpath = '//input[@name="txtClaveLoginE"]'
        # submit_button_xpath = '//input[@name="imbIngresarLogin"]'

        # self.click_element_xpath(username_input_xpath)
        # self.set_text_element(username_input_xpath, self.email)

        # self.click_element_xpath(password_input_xpath)
        # self.set_text_element(password_input_xpath, self.password)

        # self.click_element_xpath(submit_button_xpath)

    # def new_method(self, username_input_id):
    #     self.driver.click_element_id(username_input_id)
        
        
    def scrape(self):
        # Aquí iría el código para navegar por la página y extraer la información deseada
        print('')
        

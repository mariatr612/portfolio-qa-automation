from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "login-username")
        self.password_input = (By.ID, "login-password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CLASS_NAME, "Message-sc-15vkh7g-0")

    def open(self):
        self.driver.get('https://accounts.spotify.com/es-ES/login')

    def enter_email(self,user):
        self.driver.find_element(*self.email_input).send_keys(user)
    
    def enter_password(self,password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
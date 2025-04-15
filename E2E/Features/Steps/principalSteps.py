
from behave import Given, When, Then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

from Pages.loginPage import LoginPage

@Given ('que el usuario está en la página de login de Spotify')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.loginPage = LoginPage(context.driver)
    context.loginPage.open()

@When ('ingresa su email "{user}" y contraseña "{password}"')
def credenciales_input(context,user,password):
    context.loginPage.enter_email(user)
    context.loginPage.enter_password(password)

@When ('presiona el botón de iniciar sesión')
def click_iniciar_sesion(context):
    context.loginPage.click_login()
from selenium.webdriver.common.by import By

from .abstract import PageElement
from .abstract import PageObject


class MainPage(PageObject):
    h1 = PageElement(By.CSS_SELECTOR, "h1")
    p = PageElement(By.CSS_SELECTOR, "p")
    h2 = PageElement(By.CSS_SELECTOR, "h2")
    a = PageElement(By.CSS_SELECTOR, "a")

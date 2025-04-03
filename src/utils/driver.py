import logging
from time import time
from typing import List
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as NSEE

from .global_var import START_APLICATION

from .element import Element

class Driver:
    _driver: Chrome
    _printOptions: PrintOptions
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Driver, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __version_(self):
        return "1.3"

    def __str__(self) -> str:
        return f"WebDriver Chrome {self.__version_()}"
    
    def __init__(self):
        self._driver = None
        self._printOptions = None
        self._start()
        self.logger = logging.getLogger(self.__str__())
        self.logger.info(START_APLICATION)

    def _setOptionsPrint(self):
        print_options = PrintOptions()
        print_options.orientation = "landscape"
        print_options.background = True
        print_options.page_width = 29.7
        print_options.page_height = 42.0
        return print_options

    def _setOptionsDriver(self, *args) -> ChromeOptions:
        option = ChromeOptions()
        for arg in args:
            option.add_argument(arg)
        return option

    def _start(self) -> None:
        self._driver = Chrome(
            options=self._setOptionsDriver(
                "user-data-dir=C:/Users/jpxns3/AppData/Local/Google/Chrome/User Data",
                # "--force-device-scale-factor=0.75",
                # "--headless"
                )
            )
        self._printOptions = self._setOptionsPrint()
        
    def getprintOptions(self) -> PrintOptions:
        return self._printOptions

    def find_element(self, element: Element, mult: bool = False, area: EC.WebElement = None) -> EC.WebElement | List[EC.WebElement] | None:
        area_s = self._driver if area is None else area
        finder: callable = area_s.find_element if not mult else area_s.find_elements
        try:
            return finder(by=element.getSelector, value=element.getElement)
        except NSEE:
            return None
        
    def await_element(self, element:Element, wait = True, area: EC.WebElement = None) -> EC.WebElement|None:
        element_obj = None
        start = time()
        while element_obj is None:
            element_obj = self.find_element(element=element, area=area)
            if not wait and time() - start >= 10:
                break
        return element_obj
        
    def getDriver(self) -> Chrome:
        return self._driver

    def kill(self) -> None:
        self._driver.quit()
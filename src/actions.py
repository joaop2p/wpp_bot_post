import base64
import logging
import random
from os.path import join
from time import sleep
from typing import Literal
from .utils.global_var import ATTACHMENTS, BACK, CANCEL_SAFE_SEARCH, CHECK, FILE_INPUT_ALL, FILE_INPUT_IMAGE, MAIN_AREA, MESSAGE_BOX, MESSAGES_AREA, NEW_CHAT, REPOSITORY_JGP, REPOSITORY_PDF, SAFE_SEARCH, SEARCH, SEARCH_CONTACT_AFTER, SEARCH_CONTACT_BEFORE, SEND_BUTTON, START_PLATAFORM
from .utils.driver import Driver
from selenium.webdriver.common.keys import Keys

class Actions():
    
    def __init__(self) -> None:
        super().__init__()
        self.webdriver = Driver()
        self._safe_search = False
        self.logger = logging.getLogger(self.__str__())

    def __str__(self) -> str:
        return "Action Automate"

    def entregue(self) -> bool:
        messages = self.webdriver.find_element(element=MESSAGES_AREA, mult=True)
        final_message = messages[-1]
        return self.webdriver.await_element(element=CHECK,area=final_message, wait=False) is not None
    
    def start_whatsapp(self) -> None:
        self.webdriver.getDriver().get("https://web.whatsapp.com/")
        self.logger.info(START_PLATAFORM)

    def SeafeSearch(self, number: int) -> None:
        self.logger.info(SEARCH_CONTACT_BEFORE.format(number))
        search_area = self.webdriver.await_element(SAFE_SEARCH)
        search_area.send_keys(str(number))
        search_area.send_keys(Keys.ENTER)
        self._safe_search = True
        sleep(random.randint(1,3))

    def cancel_safe_seach(self) -> None:
        if self._safe_search:
            cancel_button = self.webdriver.await_element(CANCEL_SAFE_SEARCH)
            cancel_button.click()
            sleep(random.randint(1,3))
            self._safe_search = False
            
    def stop(self) -> None:
        self.webdriver.kill()

    def Search(self, number: int) -> None | Literal[False]:
        self.logger.info(SEARCH_CONTACT_AFTER.format(number))
        new_chat = self.webdriver.await_element(NEW_CHAT)
        new_chat.click()
        search = self.webdriver.await_element(SEARCH)
        search.send_keys(str(number))
        sleep(random.randint(4,10))
        search.send_keys(Keys.ENTER)
        message_box = self.webdriver.await_element(element=MESSAGE_BOX, wait=False)
        if message_box is None:
            self.back()
            return False
        sleep(random.randint(1,3))

    def sendMessage(self, message: str) -> None:
        message_box = self.webdriver.await_element(element=MESSAGE_BOX)
        message_box.send_keys(str(message))
        message_box.send_keys(Keys.ENTER)
        sleep(random.randint(1,3))

    def _inputButtons(self) -> None:
        anexos = self.webdriver.await_element(element=ATTACHMENTS)
        anexos.click()
        sleep(random.randint(1,3))

    def sendFile(self, file_path: str, isimage: bool = False) -> None:
        self._inputButtons()
        file_input = self.webdriver.await_element(element=FILE_INPUT_IMAGE if isimage else FILE_INPUT_ALL)
        file_input.send_keys(file_path)
        send_button = self.webdriver.await_element(element=SEND_BUTTON)
        send_button.click()
        sleep(random.randint(1,3))

    def screenShot(self, name: str|int):
        main = self.webdriver.await_element(element=MAIN_AREA)
        if main.screenshot(join(REPOSITORY_JGP, f'{name}.png')):
            self.logger.info(f"Registro guardado com sucesso em: '{name}'")
            return
        logging.error("Falha ao guardar registro da tela.")      

    def printPage(self, name: str | int) -> None:
        pdf = self.webdriver.getDriver().print_page(self.webdriver.getprintOptions())
        pdf_decode = base64.b64decode(pdf)
        with open(REPOSITORY_PDF.format(name), "wb") as file:
            file.write(pdf_decode)

    def back(self) -> None:
        back_button = self.webdriver.await_element(element=BACK)
        back_button.click()
        sleep(random.randint(1,3))
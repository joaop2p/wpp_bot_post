import logging
import sys
from src.launcher import wppProcess
from src.search import wpp_search
from src.utils.file_selector import file_selector
from src.log_setup import setup_logging
from os.path import basename

from src.utils.global_var import SEARCH_MESSAGE_LOG, SEND_MESSAGE_LOG

class WhatsAppBot():
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger(self.__str__())

    def __str__(self) -> str:
        return "WhatsAppBot"
    
    def search_messages(self) -> None:
        self.logger.info(SEARCH_MESSAGE_LOG)
        wpp_search()
        
    def send_messages(self, base_path: str) -> None:
        self.logger.info(SEND_MESSAGE_LOG.format(basename(base_path)))
        wppProcess(base_path)

if __name__ == "__main__":
    bot = WhatsAppBot()
    
    try:
        path = file_selector()
    except Exception as e:   
        logging.error(f"Arquivo inválido selecionado: {e}.")
        sys.exit(1)
    bot.search_messages()
    bot.send_messages(path)
    
    


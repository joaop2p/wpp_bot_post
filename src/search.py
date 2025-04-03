
import logging
from os import listdir
from os.path import join
from shutil import move
from .utils.finder import buscador
from .utils.global_var import DIST, NO_PROCESS_TO_SEARCH, SEARCH_CONTACT_BEFORE, TEMP
from .actions import Actions
from .data.conect import Conection

def format_tel(tel: int) -> str:
    sep_tel = list(str(tel))
    sep_tel.pop(2)
    return int("".join(sep_tel))

def search(target: int, actions: Actions, process: int, conection: Conection, files: list[str]) -> None:
    logging.info(SEARCH_CONTACT_BEFORE.format(target))
    actions.SeafeSearch(format_tel(target))
    status = actions.entregue()
    if status:
        move(join(TEMP, buscador(target=str(process), files=files)), DIST)
        actions.printPage(process)
        conection.update_status(process, status)
        actions.cancel_safe_seach()
    
def wpp_search() -> None:
    logging.getLogger("Módulo de busca")
    conection = Conection()
    result = conection.select()
    if len(result) < 1:
        logging.warning(NO_PROCESS_TO_SEARCH)
        return
    actions = Actions()
    files = listdir(TEMP)
    actions.start_whatsapp()
    for process, number in conection.select():    
        search(target=number, actions=actions, process=process, conection=conection, files=files)
    conection.kill()
    actions.stop()
    
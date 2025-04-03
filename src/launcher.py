
from datetime import datetime
import logging
import os
import shutil
from time import sleep
from .utils.finder import buscador
from .utils.itens import Item
from .utils.change_type import getType
from .data.conect import Conection
from .utils.files import getProcessFromFiles
from .utils.global_var import AUX_FILE, DIST, FINAL_MESSAGES, INIT_MESSAGE, ORIGIM, TEMP
from .actions import Actions
from .data.base import Base
from os import listdir

def message_and_type(path:str) -> dict[str, str]:
    '''<h3>Retorna o tipo da mensagem sendo carta resposta ou de requisição e a mensagem a ser enviada</h3>'''
    result = getType(path)
    if result is None:
        return None
    return {'message':INIT_MESSAGE[result], 'dtype':result}

def format_tel_2(tel: int) -> str:
    sep_tel = list(str(tel))
    sep_tel.pop(2)
    return int("".join(sep_tel))

def format_tel(tel: int) -> str:
    '''
    <h3>Organiza a formatação dos números de telefone</h3>
    <p>Ex: xxxxxxxxxxx -> xx-x-xxxx-xxxx</p>
    '''
    tel = str(tel)
    return f"{tel[:2]}-{tel[2]}-{tel[3:7]}-{tel[-4:]}"if len(tel) > 10 else f"{tel[:2]}-9-{tel[3:7]}-{tel[-4:]}"

def send_Messages(item: Item, actions: Actions, conection: Conection) -> None:
    for number in item.getNumbers:
        if number == 0 or actions.Search(number) is not None:
            continue
        actions.sendMessage(item.getMessage.format(item.getProcess, format_tel(number)))
        actions.sendFile(item.getPost)
        data = datetime.now()
        if item.getMessage_type == "request":
            actions.sendFile(AUX_FILE)
        sleep(2)
        for final_message in FINAL_MESSAGES:
            actions.sendMessage(final_message)
        status = actions.entregue()
        if status:
            actions.SeafeSearch(format_tel_2(number))
            actions.printPage(item.getProcess)
            shutil.move(item.getPost, DIST)
            actions.cancel_safe_seach()
        else:
            shutil.move(item.getPost, TEMP)
        conection.insert(processo=item.getProcess, tipo=item.getMessage_type, nome_arquivo= os.path.basename(item.getPost), sit=item.getIndProc, numero_usado=number, entregue=status, data=data)
        break

def wppProcess(base_path: str) -> None:
    files = listdir(ORIGIM)
    processes = getProcessFromFiles(files)
    logging.getLogger("Distribuidor de cartas")
    if len(processes) < 1:
        logging.warning("Sem cartas para envio.")
        return
    base = Base()
    base.read(base_path)
    conection = Conection()
    actions = Actions()
    actions.start_whatsapp()
    for process in processes:
        print(process)
        data = base.getInfo(process)
        if len(data) > 0:     
            row =  data.iloc[0]
            temp_post = os.path.join(ORIGIM, buscador(str(row.cod_processo), files))
            message_type = message_and_type(temp_post)
            if row.resposta_cliente == "T" and message_type is not None:
                item = Item(post=temp_post, message=message_type['message'], process=process, numbers=(row.tel_trab_solic, row.celular_solic), ind_proc=row.ind_proc, dtype=message_type['dtype'])    
                if not item.ready:
                    continue
                send_Messages(item, actions, conection)
        else:
            print("ND")
    sleep(5)
    conection.kill()
    actions.stop()
            
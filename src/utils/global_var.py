from os import getenv
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from .element import Element

load_dotenv()
# Seletores 
NEW_CHAT = Element(By.CSS_SELECTOR, "[data-icon='new-chat-outline']")
SEARCH = Element(By.CSS_SELECTOR, 'div[aria-label="Pesquisar nome ou número"]')
ATTACHMENTS = Element(By.CSS_SELECTOR, "button[title='Anexar']")
FILE_INPUT_ALL = Element(By.CSS_SELECTOR, "input[type='file'][accept='*']")
FILE_INPUT_IMAGE = Element(By.CSS_SELECTOR, "input[type='file'][accept='image/*']")
SEND_BUTTON = Element(By.CSS_SELECTOR, "[data-icon='send']")
MESSAGE_BOX = Element(By.CSS_SELECTOR, "div[aria-label='Digite uma mensagem']")
MESSAGES_AREA = Element(By.CSS_SELECTOR, 'div[class="message-out focusable-list-item _amjy _amjz _amjw"]')
CHECK = Element(By.CSS_SELECTOR, 'span[aria-label=" Entregue "]')
BACK = Element(By.CSS_SELECTOR, "span[data-icon='back']")
MAIN_AREA = Element(By.CSS_SELECTOR, "div[id='main']")
SAFE_SEARCH = Element(By.CSS_SELECTOR, "div[aria-label='Caixa de texto de pesquisa']")
CANCEL_SAFE_SEARCH = Element(By.CSS_SELECTOR, 'button[aria-label="Cancelar pesquisa"]')

# Messagens para envio
FINAL_MESSAGES = (
    "Este WhatsApp é exclusivo para o envio de cartas. Por favor, *não responda a esta mensagem, não envie documentações, e não realizamos atendimentos por ligações ou videochamadas*. Certifique-se de seguir as instruções de envio mencionadas acima",
    "Seu atendimento foi encerrado, qualquer informação entrar em contato com o 0800-083-0196, Chame a Gisa pelo chat, gisa.energisa.com.br,  ou agência de atendimento.",
    "A Energisa agradece seu contato."
)
INIT_MESSAGE ={
    "request": "Prezado (a) Cliente, conforme solicitado por V.S.ª que documentos referentes ao processo SR_{} fossem enviados através do WhatsApp {}, estamos encaminhando solicitação de documentos necessários para análise/documentação complementar e orientação de envio dos documentos requeridos.",
    "response": "Prezado (a) Cliente, conforme solicitado por V.S.ª que documentos referentes ao processo SR_{} fossem enviados através do WhatsApp {}, estamos encaminhando Carta Resposta. No caso de discordância deste parecer, V.S.ª poderá formular recurso na Ouvidoria da ENERGISA-PB, pelo telefone (83) 2106-7277), e-mail: ouvidoria-pb@energisa.com.br."
    }

# Mensagens de log
SEARCH_MESSAGE_LOG = "Iniciando busca de mensagens."
SEND_MESSAGE_LOG = "Iniciando envio de mensagens usando o arquivo: '{}'."
SEARCH_CONTACT_AFTER = "Iniciando conversas com: {}."
SEARCH_CONTACT_BEFORE = "Procurando conversa com: {}."
START_APLICATION = "Driver inicializado com sucesso."
START_PLATAFORM = "WhatsApp inicializado com sucesso."
NO_PROCESS_TO_SEARCH = "Nenhuma carta está pendente de registro."

# ENV carregadas
DIST = getenv("DIST")
TEMP = getenv("TEMP_PROCESSES")
ORIGIM = getenv("ORIGIM")
AUX_FILE = getenv("AUX_FILE")
REPOSITORY_PDF = getenv("REPOSITORY_PDF")
REPOSITORY_JGP = getenv("REPOSITORY_JGP")

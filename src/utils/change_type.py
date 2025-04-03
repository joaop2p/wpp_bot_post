import os
import re
from typing import Literal
import PyPDF2

PENDENCIA = "COMUNICADODEPENDÊNCIA"
PENDENCIA_S = "COMUNICAÇÃODEPENDÊNCIA"
SOLICITACAO = "SOLICITAÇÃODEDOCUMENTOS"
IND = "COMUNICADODEINDEFERIMENTO"
DEF = "COMUNICADODEPROCEDENTE"

def corrigir_espacos(texto) -> str:
    return re.sub(r'\s+', '', texto)

def getType(path: str) -> None |  Literal['request'] | Literal['response']:
    if not os.path.exists(path) or not os.path.isfile(path) or not os.path.basename(path).lower().endswith("pdf"):
        return None
    pdf = PyPDF2.PdfReader(path)
    for page in pdf.pages:
        content = corrigir_espacos(page.extract_text())
        if DEF in content or IND in content:
            return "response"
        elif SOLICITACAO in content or PENDENCIA_S in content or PENDENCIA in content:
            return "request"


    

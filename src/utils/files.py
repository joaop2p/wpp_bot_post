from typing import LiteralString
import re
import numpy as np  

def getProcessFromFile(file_name: str) -> LiteralString:
    match = re.search(r"20[1-2]\d{6}", file_name)
    if match is not None:
        return match.group()

def getProcessFromFiles(files: np.array):
    processos = []
    for item in files:
        process = getProcessFromFile(item)
        if process is not None and process not in processos:
            processos.append(int(process))
    return processos

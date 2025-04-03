import numpy as np


def buscador(target: str, files: list[str]) -> None:
    matching_elements = np.nonzero((np.char.find(files, target) > -1))[0]
    file = files[matching_elements.item()]
    return file if len(file) > 0 else None
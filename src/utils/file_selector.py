from tkinter.filedialog import askopenfilename


def file_selector() -> str:
    file = askopenfilename(filetypes=[("Text with headers", "*txt")])
    if len(file) < 1:
        raise Exception("Nenhum arquivo foi selecionado")
    return file
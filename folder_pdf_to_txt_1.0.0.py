from tkinter import Tk
from tkinter import messagebox
from pathlib import Path
import PyPDF2
import re
import os
from tkinter.filedialog import askdirectory

#janela_padrao = Tk().withdraw()

caminho_do_arquivo = askdirectory()

#caminho_do_arquivo = askopenfilename(filetypes = (("Arquivos PDF", "*.pdf"),))
nome_pasta = Path(caminho_do_arquivo).stem


if caminho_do_arquivo:

        for file in os.listdir(caminho_do_arquivo):    

        #faz busca pelo texto '.pdf' e atribui a file              
            if re.search('.pdf', file):  
                 
                nome_caminho =  f'{caminho_do_arquivo}/{file}'

                try:
                    leitor_pdf = PyPDF2.PdfReader(nome_caminho)
                
                    texto_total = ''
                    nome = Path(file).stem
               
                    # Iterando sobre cada página do PDF
                    for pagina in leitor_pdf.pages:
                        texto_pagina = pagina.extract_text()
                        texto_total += texto_pagina + '\n'
                        texto = open(f'{caminho_do_arquivo}/{nome}.txt', 'w+')

                        texto.write(texto_total)
                except:
                    messagebox.showinfo("EXTRAÇÃO", f"O arquivo {file} está corrompido ou ilegível !") 
        messagebox.showinfo("EXTRAÇÃO", f"Extração da pasta {nome_pasta} concluido !")
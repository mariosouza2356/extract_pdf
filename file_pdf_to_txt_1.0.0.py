from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from pathlib import Path
import PyPDF2

janela_padrao = Tk().withdraw()



# esse codigo e idependente da origem ele extrai pdf pata txt 
#preciso extrair o caminho ate a pasta sem o nome do arquivo 

# caminho_do_arquivo  = é o caminho do arquivo 


caminho_do_arquivo = askopenfilename(filetypes = (("Arquivos PDF", "*.pdf"),))

nome_arquivo = Path(caminho_do_arquivo).stem

print(nome_arquivo)


if caminho_do_arquivo:

    with open(caminho_do_arquivo, 'rb') as arquivo:
        leitor_pdf = PyPDF2.PdfReader(arquivo)
        
        texto_total = ''

        # Iterando sobre cada página do PDF
        for pagina in leitor_pdf.pages:
            texto_pagina = pagina.extract_text()
            texto_total += texto_pagina + '\n'
        texto = open(f'{caminho_do_arquivo}.txt', 'w+')

        texto.write(texto_total)
  
    messagebox.showinfo("EXTRAÇÃO", f"Extração do arquivo {nome_arquivo} está concluida !")
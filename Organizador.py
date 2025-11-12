import os
from tkinter.filedialog import askdirectory #FAZ APARECER UM POPUP QUE AO SELECIONAR REGISTA O ARQUIVO

caminho = askdirectory(title=" SELECIONE UMA PASTA PARA ORGANIZAR ") #FAZ APARECER UM POPUP QUE AO SELECIONAR REGISTA O ARQUIVO

lista_arquivos = os.listdir(caminho) #PEGA O REGISTRO DO ARQUIVO E MOSTRA O CAMINHO ATÉ ELE

locais = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"],
    "Photoshop": [".psd"],
    "Vídeos": [".mp4", ".mkv", ".avi", ".mov"],
    "Áudios": [".mp3", ".wav", ".ogg", ".flac"],
    "Executáveis": [".exe", ".msi"],
    "Planilhas": [".xls", ".xlsx"],
    "CSV": [".csv"],
    "Documentos Word": [".doc", ".docx"],
    "PDF": [".pdf"],
    "Apresentações": [".ppt", ".pptx"],
    "Compactados": [".zip", ".rar", ".7z"]

} #DICINARIO QUE IRÁ ORGANIZAR OS ARQUIVOS E CRIAR AS PASTAS

#Minha versão bosta sem GPT
for arquivo in lista_arquivos:
    nome, formato = os.path.splitext(arquivo) #LER O FORMATO DO ARQUIVO

    for pasta in locais: #PASTA = TODAS AS OPÇÕES DOS LOCAIS (EX: PASTA = IMAGENS ou PASTA = PLANILHAS)

        if formato in locais[pasta]: #SE O FORMATO ESTIVER EM ALGUMA PASTA DO DICIONARIO "LOCAIS"...

            if not os.path.exists(f"{caminho}/{pasta}"): #SE NÃO EXISTE A PASTA "IMAGENS" DENTRO DO CAMINHO SELECIONADO PELO USUÁRIO EM "CAMINHO"
                os.makedirs(f"{caminho}/{pasta}") #CRIA A PASTA 

            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}") #REORGANIZA O ARQUIVO, PEGA DO CAMINHO/ARQUIVO ORIGINAL, E PASSA PARA O NOVO QUE FOI CRIADO

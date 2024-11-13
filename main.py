from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter.ttk import Combobox


from PIL import Image, ImageTk
from PIL.XbmImagePlugin import xbm_head

#Importando Tkcalendar
import locale
from tkcalendar import Calendar, DateEntry
from datetime import date

#cores

co0 = "#2e2d2b" #preta
co1 = "#feffff" #branca
co2 = "#4fa882" #verde
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e06636" # - profit
co6 = "#038cfc" #azul
co7 = "#3fbfb9" #verde
co8 = "#263238" #+verde
co9 = "#e9edf5" #+verde


#criando a janela

janela = Tk()
janela.title('')
janela.geometry('900x700')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style()
style.theme_use("clam")

#craindo frames

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=400, bg=co1,pady=20,relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1,padx=0,sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=400,bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0,pady=0, padx=1, sticky='NSEW')




#Abrindo imagem
app_img = Image.open('icons8-audit-48.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text='CIAP', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0,y=0)

#Trabalhando no frameCima


#Criando entradas
numeroRegistro = Label(frameMeio, text='Número do Registro:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
numeroRegistro.place(x=10,y=10)
e_numeroRegistro = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_numeroRegistro.place(x=150, y=11)

tipoRegistro = Label(frameMeio, text='Tipo de Registro:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
tipoRegistro.place(x=10,y=40)
e_tipoRegistro = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_tipoRegistro.place(x=150, y=41)

numeroTabela = Label(frameMeio, text='Número da Tabela:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
numeroTabela.place(x=10,y=70)
e_numeroTabela = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_numeroTabela.place(x=150, y=71)

nomeTabela = Label(frameMeio, text='Nome da Tabela:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
nomeTabela.place(x=10,y=100)
e_nomeTabela = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nomeTabela.place(x=150, y=101)

codigoBem = Label(frameMeio, text='Código do Bem:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
codigoBem.place(x=10,y=130)
e_codigoBem = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_codigoBem.place(x=150, y=131)

sequenciaBem = Label(frameMeio, text='Sequência do Bem:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
sequenciaBem.place(x=10,y=160)
e_sequenciaBem = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_sequenciaBem.place(x=150, y=161)

fornecedor = Label(frameMeio, text='Fornecedor:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
fornecedor.place(x=10,y=190)
e_fornecedor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_fornecedor.place(x=150, y=191)

enderecoFornecedor = Label(frameMeio, text='Endereço do Fornec.:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
enderecoFornecedor.place(x=10,y=220)
e_enderecoFornecedor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_enderecoFornecedor.place(x=150, y=221)

descricaoBem = Label(frameMeio, text='Descrição do Bem:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
descricaoBem.place(x=10,y=250)
e_descricaoBem = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricaoBem.place(x=150, y=251)

numDocAquis = Label(frameMeio, text='Num Doc. Aquisição:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
numDocAquis.place(x=10,y=280)
e_numDocAquis = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_numDocAquis.place(x=150, y=281)

serieDocCompra = Label(frameMeio, text='Série Doc. Compra:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
serieDocCompra.place(x=10,y=310)
e_serieDocCompra = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serieDocCompra.place(x=150, y=311)

tipoDocCompra= Label(frameMeio, text='Tipo Doc. Compra:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
tipoDocCompra.place(x=400,y=10)
e_tipoDocCompra = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_tipoDocCompra.place(x=540, y=11)

dtEmissDoc= Label(frameMeio, text='Data de Emissão:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
dtEmissDoc.place(x=400,y=40)
e_dtEmissDoc = DateEntry(frameMeio, width='24', font=('Ivy 10 bold'),background='darkblue',bordewidth=2,year=2024, relief=SOLID, date_pattern='dd/mm/yyyy')
e_dtEmissDoc.place(x=540, y=41)

chaveNFECompra= Label(frameMeio, text='Chave NFE Compra:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
chaveNFECompra.place(x=400,y=70)
e_chaveNFECompra = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_chaveNFECompra.place(x=540, y=71)

valorICMSAquis= Label(frameMeio, text='Valor ICMS Aquis.:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
valorICMSAquis.place(x=400,y=100)
e_valorICMSAquis = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valorICMSAquis.place(x=540, y=101)

numeroParcelas= Label(frameMeio, text='Numero de Parcelas:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
numeroParcelas.place(x=400,y=130)
e_numeroParcelas = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_numeroParcelas.place(x=540, y=131)


locale.setlocale(locale.LC_ALL,'pt_BR')
dtMovimento= Label(frameMeio, text='Data Movimento:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
dtMovimento.place(x=400,y=160)
e_dtMovimento = DateEntry(frameMeio, width='24', font=('Ivy 10 bold'),background='darkblue',bordewidth=2,year=2024, relief=SOLID, date_pattern='dd/mm/yyyy')
e_dtMovimento.place(x=540, y=161)


opcoes_Movimento = ["","SI- Saldo Inicial de Bens Imobilizados", "IA- Imobilização em Andamento - Componente", "CI- Conclusão de Imobilização em Andamento", "BA- Baixa de Bem - Fim do Período de Apropriação","PE- Perecimento, Extravio ou Deterioração","OT- Outras Saídas do Imobilizado"]
tipoMovimento= Label(frameMeio, text='Tipo de Movimento:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
tipoMovimento.place(x=400,y=190)
combo_movimento = Combobox(frameMeio, values=opcoes_Movimento,height=5, width=24, font=('Ivy 10 bold'))
combo_movimento.place(x=540,y=191)



valorICMSMensal= Label(frameMeio, text='Valor ICMS Mensal:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
valorICMSMensal.place(x=400,y=220)
e_valorICMSMensal = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valorICMSMensal.place(x=540, y=221)

codigoItemEstoque= Label(frameMeio, text='Codigo Item Estoque:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
codigoItemEstoque.place(x=400,y=250)
e_codigoItemEstoque = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_codigoItemEstoque.place(x=540, y=251)

centroCusto= Label(frameMeio, text='Centro de Custo:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
centroCusto.place(x=400,y=280)
e_centroCusto = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_centroCusto.place(x=540, y=281)

conta= Label(frameMeio, text='Conta:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
conta.place(x=400,y=310)
e_conta = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_conta.place(x=540, y=311)



#criando botões

#botão inserir

imgagem_inserir = Image.open('icons8-add-50.png')
imagem_inserir = imgagem_inserir.resize((20,20))
imagem_inserir = ImageTk.PhotoImage(imagem_inserir)

botao_inserir = Button(frameMeio, image=imagem_inserir, width=95, text=" ADICIONAR".upper(),compound=LEFT, anchor=NW,overrelief=RIDGE, font=('Ivy 8'), bg=co1,fg=co0)
botao_inserir.place(x=770,y=10)

#Botão atualizar

imgagem_atualizar = Image.open('icons8-update-80.png')
imagem_atualizar = imgagem_atualizar.resize((20,20))
imagem_atualizar = ImageTk.PhotoImage(imagem_atualizar)

botao_atualizar = Button(frameMeio, image=imagem_atualizar, width=95, text=" ATUALIZAR".upper(),compound=LEFT, anchor=NW,overrelief=RIDGE, font=('Ivy 8'), bg=co1,fg=co0)
botao_atualizar.place(x=770,y=50)


#Botão deletar

imgagem_deletar = Image.open('icons8-delete-50.png')
imagem_deletar = imgagem_deletar.resize((20,20))
imagem_deletar = ImageTk.PhotoImage(imagem_deletar)

botao_deletar = Button(frameMeio, image=imagem_deletar, width=95, text=" DELETAR".upper(),compound=LEFT, anchor=NW,overrelief=RIDGE, font=('Ivy 8'), bg=co1,fg=co0)
botao_deletar.place(x=770,y=90)

#Botão buscar

imgagem_buscar = Image.open('icons8-search-48.png')
imagem_buscar = imgagem_buscar.resize((20,20))
imagem_buscar = ImageTk.PhotoImage(imagem_buscar)

botao_buscar = Button(frameMeio, image=imagem_buscar, width=95, text=" BUSCAR".upper(),compound=LEFT, anchor=NW,overrelief=RIDGE, font=('Ivy 8'), bg=co1,fg=co0)
botao_buscar.place(x=770,y=130)


janela.mainloop()
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry
from customtkinter import CTkImage
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
import locale

from view import*





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

janela = ctk.CTk()  # Substituindo Tk() por CTk()
janela.title('')  # Título da janela (pode deixar vazio ou definir um título)
janela.geometry('900x700')  # Tamanho da janela
janela.configure(bg_color=co9)  # Cor de fundo (substituindo background de Tkinter por bg_color no customtkinter)
janela.resizable(False, False)




# Criando o frame superior (frameCima)
frameCima = ctk.CTkFrame(janela, width=1043, height=50, fg_color=co1)  # Substituindo o Frame por CTkFrame e fg_color no lugar de bg
frameCima.grid(row=0, column=0, sticky="ew")  # 'sticky="ew"' garante que o frame ocupe toda a largura disponível

# Linha de separação entre frameCima e frameMeio
linha_divisoria_1 = ctk.CTkFrame(janela, width=1043, height=1, fg_color=co4)  # Linha de separação
linha_divisoria_1.grid(row=1, column=0, sticky="ew")

# Criando o frame do meio (frameMeio)
frameMeio = ctk.CTkFrame(janela, width=1043, height=400, fg_color=co1)  # Usando fg_color para definir a cor de fundo
frameMeio.grid(row=2, column=0, pady=0, padx=0, sticky="nsew")  # 'sticky="nsew"' para que o frame ocupe
janela.grid_rowconfigure(2, weight=1)  # Garantir que o frameMeio ocupe espaço corretamente

# Linha de separação entre frameMeio e frameBaixo
linha_divisoria_2 = ctk.CTkFrame(janela, width=1043, height=1, fg_color=co4)  # Linha de separação
linha_divisoria_2.grid(row=3, column=0, sticky="ew")

# Criando o frame inferior (frameBaixo)
frameBaixo = ctk.CTkFrame(janela, width=1043, height=300, fg_color=co1)  # Usando fg_color para definir a cor de fundo
frameBaixo.grid(row=4, column=0, pady=0, padx=1, sticky="nsew")
janela.grid_rowconfigure(4, weight=1)  # Garantir que o frameBaixo ocupe o restante do espaço


#Abrindo imagem
app_img = Image.open('icons8-audit-48.png')
app_img = app_img.resize((45,45))
app_img = ctk.CTkImage(app_img, size=(45,45))

#criando funções
#função inserir
def inserir():

    numero_registro = e_numeroRegistro.get()
    tipo_registro = e_tipoRegistro.get()
    numero_tabela = e_numeroTabela.get()
    nome_tabela= e_nomeTabela.get()
    codigo_do_bem= e_codigoBem.get()
    sequencia_do_bem = e_sequenciaBem.get()
    fornecedor = e_fornecedor.get()
    endereco_fornecedor = e_enderecoFornecedor.get()
    descricao_bem = e_descricaoBem.get()
    numero_doc_aquisicao = e_numDocAquis.get()
    serie_doc_compra = e_serieDocCompra.get()
    tipo_doc_compra = e_tipoDocCompra.get()
    data_emissao_compra = e_dtEmissDoc.get()
    chave_nfe_compra = e_chaveNFECompra.get()
    valor_icms_aquisicao = e_valorICMSAquis.get()
    numero_parcelas = e_numeroParcelas.get()
    data_movimento = e_dtMovimento.get()
    tipo_movimento = combo_movimento.get()
    valor_icms_mensal = e_valorICMSMensal.get()
    codigo_item_estoque = e_codigoItemEstoque.get()
    centro_custo = e_centroCusto.get()
    conta = e_conta.get()

    lista_inserir = [numero_registro, tipo_registro, numero_tabela, nome_tabela, codigo_do_bem, sequencia_do_bem, fornecedor, endereco_fornecedor, descricao_bem, numero_doc_aquisicao, serie_doc_compra, tipo_doc_compra, data_emissao_compra, chave_nfe_compra, valor_icms_aquisicao, numero_parcelas, data_movimento, tipo_movimento, valor_icms_mensal, codigo_item_estoque, centro_custo, conta]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    inserir_form(lista_inserir)
    messagebox.showinfo('Sucesso','Os dados foram inseridos com sucesso')

    e_numeroRegistro.delete(0,'end')
    e_tipoRegistro.delete(0,'end')
    e_numeroTabela.delete(0,'end')
    e_nomeTabela.delete(0,'end')
    e_codigoBem.delete(0,'end')
    e_sequenciaBem.delete(0,'end')
    e_fornecedor.delete(0,'end')
    e_enderecoFornecedor.delete(0,'end')
    e_descricaoBem.delete(0,'end')
    e_numDocAquis.delete(0,'end')
    e_serieDocCompra.delete(0,'end')
    e_tipoDocCompra.delete(0,'end')
    e_dtEmissDoc.delete(0,'end')
    e_chaveNFECompra.delete(0,'end')
    e_valorICMSAquis.delete(0,'end')
    e_numeroParcelas.delete(0,'end')
    e_dtMovimento.delete(0,'end')
    combo_movimento.set('')
    e_valorICMSMensal.delete(0,'end')
    e_codigoItemEstoque.delete(0,'end')
    e_centroCusto.delete(0,'end')
    (e_conta.delete(0,'end'))

    mostrar()





 #criando logo no frameCima

app_logo = ctk.CTkLabel(frameCima, image=app_img, text='            CONTROLE DE CRÉDITO DE ICMS DO ATIVO PERMANENTE', width=900, compound='left', anchor='nw', font=('Verdana', 20, 'bold'), text_color=co4, fg_color=co1)
app_logo.place(x=0,y=0)


numeroRegistro = ctk.CTkLabel(frameMeio, text='Numero do Registro:', font=('Ivy',12,'bold'), text_color=co4, fg_color=co1)
numeroRegistro.place(x=10,y=10)
e_numeroRegistro = ctk.CTkEntry(frameMeio, width=170)
e_numeroRegistro.place(x=150,y=10)

tipoRegistro = ctk.CTkLabel(frameMeio, text='Tipo de Registro:', font=('Ivy', 12, 'bold'), text_color=co4, fg_color=co1)
tipoRegistro.place(x=10,y=40)
e_tipoRegistro = ctk.CTkEntry(frameMeio, width=170)
e_tipoRegistro.place(x=150, y=41)

numeroTabela = ctk.CTkLabel(frameMeio, text='Número da Tabela:', font=('Ivy', 12,'bold'), text_color=co4, fg_color=co1)
numeroTabela.place(x=10,y=70)
e_numeroTabela = ctk.CTkEntry(frameMeio, width=170)
e_numeroTabela.place(x=150, y=71)

nomeTabela = ctk.CTkLabel(frameMeio, text='Nome da Tabela:', font=('Ivy', 12,'bold'), text_color=co4, fg_color=co1)
nomeTabela.place(x=10,y=100)
e_nomeTabela = ctk.CTkEntry(frameMeio, width=170)
e_nomeTabela.place(x=150, y=101)

codigoBem = ctk.CTkLabel(frameMeio, text='Código do Bem:', font=('Ivy',12,'bold'), text_color=co4, fg_color=co1)
codigoBem.place(x=10,y=130)
e_codigoBem = ctk.CTkEntry(frameMeio, width=170)
e_codigoBem.place(x=150, y=131)

sequenciaBem = ctk.CTkLabel(frameMeio, text='Sequência do Bem:', font=('Ivy',12, 'bold'), text_color=co4, fg_color=co1)
sequenciaBem.place(x=10,y=160)
e_sequenciaBem = ctk.CTkEntry(frameMeio, width=170)
e_sequenciaBem.place(x=150, y=161)

fornecedor = ctk.CTkLabel(frameMeio, text='Fornecedor:', font=('Ivy', 12 ,'bold'),text_color=co4, fg_color=co1)
fornecedor.place(x=10,y=190)
e_fornecedor = ctk.CTkEntry(frameMeio, width=170)
e_fornecedor.place(x=150, y=191)

enderecoFornecedor = ctk.CTkLabel(frameMeio, text='Endereço do Fornec.:', font=('Ivy', 12 ,'bold'),text_color=co4, fg_color=co1)
enderecoFornecedor.place(x=10,y=220)
e_enderecoFornecedor = ctk.CTkEntry(frameMeio, width=170)
e_enderecoFornecedor.place(x=150, y=221)

descricaoBem = ctk.CTkLabel(frameMeio, text='Descrição do Bem:', font=('Ivy', 12, 'bold'),text_color=co4, fg_color=co1 )
descricaoBem.place(x=10,y=250)
e_descricaoBem = ctk.CTkEntry(frameMeio, width=170)
e_descricaoBem.place(x=150, y=251)

numDocAquis = ctk.CTkLabel(frameMeio, text='Num Doc. Aquisição:', font=('Ivy', 12, 'bold'),text_color=co4, fg_color=co1)
numDocAquis.place(x=10,y=280)
e_numDocAquis = ctk.CTkEntry(frameMeio, width=170)
e_numDocAquis.place(x=150, y=281)

serieDocCompra = ctk.CTkLabel(frameMeio, text='Série Doc. Compra:', font=('Ivy', 12, 'bold'), text_color=co4, fg_color=co1)
serieDocCompra.place(x=10,y=310)
e_serieDocCompra = ctk.CTkEntry(frameMeio, width=170)
e_serieDocCompra.place(x=150, y=311)

tipoDocCompra= ctk.CTkLabel(frameMeio, text='Tipo Doc. Compra:', font=('Ivy', 12, 'bold'),text_color=co4, fg_color=co1)
tipoDocCompra.place(x=400,y=10)
e_tipoDocCompra = ctk.CTkEntry(frameMeio, width=170)
e_tipoDocCompra.place(x=540, y=11)

dtEmissDoc = ctk.CTkLabel(frameMeio, text='Data de Emissão:', font=('Ivy', 12, 'bold'), text_color=co4, fg_color=co1)
dtEmissDoc.place(x=400, y=40)

# Adicionando o DateEntry do tkcalendar
e_dtEmissDoc = DateEntry(frameMeio, width=16, font=('Ivy', 12, 'bold'), background='darkblue', foreground='white', borderwidth=2, year=2024, date_pattern='dd/mm/yyyy')
e_dtEmissDoc.place(x=540, y=41)

chaveNFECompra= ctk.CTkLabel(frameMeio, text='Chave NFE Compra:', font=('Ivy',12 ,'bold'), text_color=co4, fg_color=co1)
chaveNFECompra.place(x=400,y=70)
e_chaveNFECompra = ctk.CTkEntry(frameMeio, width=170)
e_chaveNFECompra.place(x=540, y=71)

valorICMSAquis= ctk.CTkLabel(frameMeio, text='Valor ICMS Aquis.:',font=('Ivy', 12, 'bold'),text_color=co4, fg_color=co1)
valorICMSAquis.place(x=400,y=100)
e_valorICMSAquis = ctk.CTkEntry(frameMeio, width=170)
e_valorICMSAquis.place(x=540, y=101)

numeroParcelas= ctk.CTkLabel(frameMeio, text='Numero de Parcelas:', font=('Ivy',12, 'bold'), text_color=co4, fg_color=co1)
numeroParcelas.place(x=400,y=130)
e_numeroParcelas = ctk.CTkEntry(frameMeio, width=170)
e_numeroParcelas.place(x=540, y=131)

# Label para a data de movimento
dtMovimento = ctk.CTkLabel(frameMeio, text='Data Movimento:', height=1, anchor='nw', font=('Ivy', 12, 'bold'), text_color=co4, fg_color=co1)
dtMovimento.place(x=400, y=160)

# Adicionando o DateEntry para Data Movimento
e_dtMovimento = DateEntry(frameMeio, width=16, font=('Ivy', 12, 'bold'), background='darkblue', foreground='white', borderwidth=2, year=2024, date_pattern='dd/mm/yyyy')
e_dtMovimento.place(x=540, y=161)

opcoes_Movimento = [
    "",
    "SI- Saldo Inicial de Bens Imobilizados",
    "IA- Imobilização em Andamento - Componente",
    "CI- Conclusão de Imobilização em Andamento",
    "BA- Baixa de Bem - Fim do Período de Apropriação",
    "PE- Perecimento, Extravio ou Deterioração",
    "OT- Outras Saídas do Imobilizado"
]

# Label para o tipo de movimento
tipoMovimento = ctk.CTkLabel(frameMeio, text='Tipo de Movimento:', height=1, anchor='nw', font=('Ivy', 12, 'bold'), text_color=co4, fg_color=co1)
tipoMovimento.place(x=400, y=190)

# Adicionando o CTkComboBox para selecionar o tipo de movimento
combo_movimento = ctk.CTkComboBox(frameMeio, values=opcoes_Movimento, width=170, font=('Ivy', 12, 'bold'))
combo_movimento.place(x=540, y=191)



valorICMSMensal= ctk.CTkLabel(frameMeio, text='Valor ICMS Mensal:', font=('Ivy',12, 'bold'), text_color=co4, fg_color=co1)
valorICMSMensal.place(x=400,y=220)
e_valorICMSMensal = ctk.CTkEntry(frameMeio, width=170)
e_valorICMSMensal.place(x=540, y=221)

codigoItemEstoque= ctk.CTkLabel(frameMeio, text='Codigo Item Estoque:',font=('Ivy',12,'bold'), text_color=co4, fg_color=co1)
codigoItemEstoque.place(x=400,y=250)
e_codigoItemEstoque = ctk.CTkEntry(frameMeio, width=170)
e_codigoItemEstoque.place(x=540, y=251)

centroCusto= ctk.CTkLabel(frameMeio, text='Centro de Custo:',font=('Ivy', 12, 'bold'), text_color=co4, fg_color=co1)
centroCusto.place(x=400,y=280)
e_centroCusto = ctk.CTkEntry(frameMeio, width=170)
e_centroCusto.place(x=540, y=281)

conta= ctk.CTkLabel(frameMeio, text='Conta:', font=('Ivy', 12, 'bold'), text_color=co4, fg_color=co1)
conta.place(x=400,y=310)
e_conta = ctk.CTkEntry(frameMeio, width=170)
e_conta.place(x=540, y=311)





# Abrindo a imagem
imagem_inserir = Image.open('icons8-add-50.png')  # Caminho para a imagem
imagem_inserir = imagem_inserir.resize((20, 20))  # Redimensionando a imagem
imagem_inserir = ctk.CTkImage(imagem_inserir)  # Converta para PhotoImage para o Tkinter

# Criando o botão no customtkinter (CTkButton)
botao_inserir = ctk.CTkButton(
    frameMeio,
    command=inserir,
    image=imagem_inserir,  # Imagem do botão
    text=" ADICIONAR".upper(),  # Texto do botão
    compound="left",  # Texto à esquerda da imagem
    anchor="nw",  # Alinhamento do texto
    font=("Ivy", 10),  # Fonte do texto
    fg_color=co1,  # Cor de fundo do botão
    text_color=co0,  # Cor do texto
    width=120,  # Largura do botão
    height=30  # Altura do botão

)

# Posicionando o botão na tela
botao_inserir.place(x=770, y=10)

# Abrindo a imagem
imagem_atualizar = Image.open('icons8-update-80.png')  # Caminho para a imagem
imagem_atualizar = imagem_atualizar.resize((20, 20))  # Redimensionando a imagem
imagem_atualizar = ctk.CTkImage(imagem_atualizar)  # Converta para PhotoImage para o Tkinter

# Criando o botão no customtkinter (CTkButton)
botao_atualizar = ctk.CTkButton(
    frameMeio,
    image=imagem_atualizar,  # Imagem do botão
    text=" ATUALIZAR".upper(),  # Texto do botão
    compound="left",  # Texto à esquerda da imagem
    anchor="nw",  # Alinhamento do texto
    font=("Ivy", 10),  # Fonte do texto
    fg_color=co1,  # Cor de fundo do botão
    text_color=co0,  # Cor do texto
    width=120,  # Largura do botão
    height=30  # Altura do botão
)

# Posicionando o botão na tela
botao_atualizar.place(x=770, y=50)

# Abrindo a imagem
imagem_deletar = Image.open('icons8-delete-50.png')  # Caminho para a imagem
imagem_deletar = imagem_deletar.resize((20, 20))  # Redimensionando a imagem
imagem_deletar = ctk.CTkImage(imagem_deletar)  # Converta para PhotoImage para o Tkinter

# Criando o botão no customtkinter (CTkButton)
botao_deletar = ctk.CTkButton(
    frameMeio,
    image=imagem_deletar,  # Imagem do botão
    text=" DELETAR".upper(),  # Texto do botão
    compound="left",  # Texto à esquerda da imagem
    anchor="nw",  # Alinhamento do texto
    font=("Ivy", 10),  # Fonte do texto
    fg_color=co1,  # Cor de fundo do botão
    text_color=co0,  # Cor do texto
    width=120,  # Largura do botão
    height=30  # Altura do botão
)

# Posicionando o botão na tela
botao_deletar.place(x=770, y=90)

# Abrindo a imagem
imagem_procurar = Image.open('icons8-search-48.png')  # Caminho para a imagem
imagem_procurar = imagem_procurar.resize((20, 20))  # Redimensionando a imagem
imagem_procurar = ctk.CTkImage(imagem_procurar)  # Converta para PhotoImage para o Tkinter

# Criando o botão no customtkinter (CTkButton)
botao_procurar = ctk.CTkButton(
    frameMeio,
    image=imagem_procurar,  # Imagem do botão
    text=" PROCURAR".upper(),  # Texto do botão
    compound="left",  # Texto à esquerda da imagem
    anchor="nw",  # Alinhamento do texto
    font=("Ivy", 10),  # Fonte do texto
    fg_color=co1,  # Cor de fundo do botão
    text_color=co0,  # Cor do texto
    width=120,  # Largura do botão
    height=30  # Altura do botão

)

# Posicionando o botão na tela
botao_procurar.place(x=770, y=130)

def mostrar():
    # Cabeçalhos da tabela
    tabela_head = ['COD', 'Número do Registro', 'Tipo do Registro', 'Número da Tabela', 'Nome da Tabela', 'Código Bem',
                   'Sequência Bem', 'Fornecedor', 'Endereço Fornecedor', 'Descrição do Bem',
                   'Número Documento Aquisição',
                   'Série do Documento Compra', 'Tipo Documento Compra', 'Data de Emissão do Documento',
                   'Chave NFE Compra',
                   'Valor ICMS Aquisição', 'Numero de Parcelas', 'Data de Movimento', 'Tipo de Movimento',
                   'Valor ICMS Mensal',
                   'Código Item Estoque', 'Centro de Custo', 'Conta']


    # Obtendo os dados para a tabela
    lista_itens = ver_form()

    # Criando o Frame para a tabela
    frameBaixo = ctk.CTkFrame(janela)
    frameBaixo.grid(row=4, column=0, sticky="nsew")
    janela.grid_rowconfigure(0, weight=1)
    janela.grid_columnconfigure(0, weight=1)

    # Criando o Canvas para rolagem dentro do frame
    canvas = ctk.CTkCanvas(frameBaixo)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Criando as barras de rolagem
    vsb = ctk.CTkScrollbar(frameBaixo, command=canvas.yview)
    vsb.grid(row=0, column=1, sticky="ns")  # Barra de rolagem vertical

    hsb = ctk.CTkScrollbar(frameBaixo, command=canvas.xview, orientation="horizontal")
    hsb.grid(row=1, column=0, sticky="ew")  # Barra de rolagem horizontal

    # Configurando o Canvas para usar as barras de rolagem
    canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Criando o Frame onde os widgets da tabela (cabeçalhos e dados) vão ficar
    tree_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=tree_frame, anchor="nw")

    # Criando os cabeçalhos da tabela na primeira linha
    for j, col in enumerate(tabela_head):
        label = ctk.CTkLabel(tree_frame, text=col, width=200, anchor="w", font=("Arial", 10, "bold"))
        label.grid(row=0, column=j, padx=5, pady=5, sticky="w")  # Cabeçalhos na linha 0

    # Criando as células de dados na tabela
    for i, item in enumerate(lista_itens, start=1):  # Começa na linha 1, pois a linha 0 é dos cabeçalhos
        for j, valor in enumerate(item):
            label = ctk.CTkLabel(tree_frame, text=str(valor), width=200, anchor="w", font=("Arial", 10))
            label.grid(row=i, column=j, padx=5, pady=5, sticky="w")  # Popula a tabela com os dados reais

    # Atualizando a área visível do canvas após adicionar os widgets
    tree_frame.update_idletasks()  # Atualiza o layout para garantir que o canvas tenha o tamanho correto
    canvas.config(scrollregion=canvas.bbox("all"))  # Ajusta a área de rolagem do canvas

    # Configuração do layout de rolagem
    frameBaixo.grid_rowconfigure(0, weight=1)  # Faz o Frame expandir verticalmente
    frameBaixo.grid_columnconfigure(0, weight=1)  # Faz o Frame expandir horizontalmente
mostrar()

janela.mainloop()
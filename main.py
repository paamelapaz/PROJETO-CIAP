import tkinter as tk
from cProfile import label

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
global tree





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
janela.title('')# Título da janela (pode deixar vazio ou definir um título)
janela.geometry('1050x657')  # Tamanho da janela
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
frameBaixo = ctk.CTkFrame(janela)  # Usando fg_color para definir a cor de fundo
frameBaixo.grid(row=3,column=0,sticky="nsew")
  # Garantir que o frameBaixo ocupe o restante do espaço

janela.grid_rowconfigure(3, weight=1)  # Configura a linha 3 para expandir
janela.grid_columnconfigure(0, weight=1)


#Abrindo imagem
app_img = Image.open('icons8-audit-48.png')
app_img = app_img.resize((45,45))
app_img = ctk.CTkImage(app_img, size=(45,45))

#criando funções

def label_entry(frame,label_text, pos_x,pos_y):

    label= ctk.CTkLabel(frame, text=label_text, font=('Ivy',12,'bold'),text_color=co4, fg_color=co1)
    label.place(x=pos_x,y=pos_y)
    entry = ctk.CTkEntry(frame, width=240,height=15)
    entry.place(x=pos_x+140,y=pos_y)
    return entry


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

#função atualizar

def atualizar():
    global tree
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_numeroRegistro.delete(0, 'end')
        e_tipoRegistro.delete(0, 'end')
        e_numeroTabela.delete(0, 'end')
        e_nomeTabela.delete(0, 'end')
        e_codigoBem.delete(0, 'end')
        e_sequenciaBem.delete(0, 'end')
        e_fornecedor.delete(0, 'end')
        e_enderecoFornecedor.delete(0, 'end')
        e_descricaoBem.delete(0, 'end')
        e_numDocAquis.delete(0, 'end')
        e_serieDocCompra.delete(0, 'end')
        e_tipoDocCompra.delete(0, 'end')
        e_dtEmissDoc.delete(0, 'end')
        e_chaveNFECompra.delete(0, 'end')
        e_valorICMSAquis.delete(0, 'end')
        e_numeroParcelas.delete(0, 'end')
        e_dtMovimento.delete(0, 'end')
        combo_movimento.set("")
        e_valorICMSMensal.delete(0, 'end')
        e_codigoItemEstoque.delete(0, 'end')
        e_centroCusto.delete(0, 'end')
        e_conta.delete(0, 'end')


        id = int(treev_lista[0])
        e_numeroRegistro.insert(0,treev_lista[1])
        e_tipoRegistro.insert(0, treev_lista[2])
        e_numeroTabela.insert(0, treev_lista[3])
        e_nomeTabela.insert(0, treev_lista[4])
        e_codigoBem.insert(0, treev_lista[5])
        e_sequenciaBem.insert(0, treev_lista[6])
        e_fornecedor.insert(0, treev_lista[7])
        e_enderecoFornecedor.insert(0, treev_lista[8])
        e_descricaoBem.insert(0, treev_lista[9])
        e_numDocAquis.insert(0, treev_lista[10])
        e_serieDocCompra.insert(0, treev_lista[11])
        e_tipoDocCompra.insert(0, treev_lista[12])
        e_dtEmissDoc.insert(0, treev_lista[13])
        e_chaveNFECompra.insert(0, treev_lista[14])
        e_valorICMSAquis.insert(0, treev_lista[15])
        e_numeroParcelas.insert(0, treev_lista[16])
        e_dtMovimento.insert(0, treev_lista[17])
        combo_movimento.set(treev_lista[18])
        e_valorICMSMensal.insert(0, treev_lista[19])
        e_codigoItemEstoque.insert(0, treev_lista[20])
        e_centroCusto.insert(0, treev_lista[21])
        e_conta.insert(0, treev_lista[22])

        def update():
            numero_registro = e_numeroRegistro.get()
            tipo_registro = e_tipoRegistro.get()
            numero_tabela = e_numeroTabela.get()
            nome_tabela = e_nomeTabela.get()
            codigo_do_bem = e_codigoBem.get()
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

            lista_atualizar = [numero_registro, tipo_registro, numero_tabela, nome_tabela, codigo_do_bem, sequencia_do_bem, fornecedor, endereco_fornecedor, descricao_bem, numero_doc_aquisicao, serie_doc_compra,tipo_doc_compra, data_emissao_compra, chave_nfe_compra, valor_icms_aquisicao, numero_parcelas,data_movimento, tipo_movimento, valor_icms_mensal, codigo_item_estoque, centro_custo, conta,id]

            for i in lista_atualizar:
                if i =='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
            atualizar_form(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_numeroRegistro.delete(0, 'end')
            e_tipoRegistro.delete(0, 'end')
            e_numeroTabela.delete(0, 'end')
            e_nomeTabela.delete(0, 'end')
            e_codigoBem.delete(0, 'end')
            e_sequenciaBem.delete(0, 'end')
            e_fornecedor.delete(0, 'end')
            e_enderecoFornecedor.delete(0, 'end')
            e_descricaoBem.delete(0, 'end')
            e_numDocAquis.delete(0, 'end')
            e_serieDocCompra.delete(0, 'end')
            e_tipoDocCompra.delete(0, 'end')
            e_dtEmissDoc.delete(0, 'end')
            e_chaveNFECompra.delete(0, 'end')
            e_valorICMSAquis.delete(0, 'end')
            e_numeroParcelas.delete(0, 'end')
            e_dtMovimento.delete(0, 'end')
            combo_movimento.set('')
            e_valorICMSMensal.delete(0, 'end')
            e_codigoItemEstoque.delete(0, 'end')
            e_centroCusto.delete(0, 'end')
            e_conta.delete(0, 'end')

            botao_confirmar.destroy()
            botao_cancelar.destroy()

            mostrar()

        botao_confirmar = ctk.CTkButton(
            frameMeio,
            command=update,
            text=" Confirmar".upper(),  # Texto do botão
            font=("Ivy", 12, 'bold'),  # Fonte do texto
            fg_color="#32cd32",  # Cor de fundo do botão
            text_color=co0,  # Cor do texto
            width=120,  # Largura do botão
            height=30,  # Altura do botão
            border_color="green",  # Cor da borda
            border_width=1  # Largura da borda
        )

        # Posicionando o botão na tela
        botao_confirmar.place(x=870, y=220)

        def cancelar():
            e_numeroRegistro.delete(0, 'end')
            e_tipoRegistro.delete(0, 'end')
            e_numeroTabela.delete(0, 'end')
            e_nomeTabela.delete(0, 'end')
            e_codigoBem.delete(0, 'end')
            e_sequenciaBem.delete(0, 'end')
            e_fornecedor.delete(0, 'end')
            e_enderecoFornecedor.delete(0, 'end')
            e_descricaoBem.delete(0, 'end')
            e_numDocAquis.delete(0, 'end')
            e_serieDocCompra.delete(0, 'end')
            e_tipoDocCompra.delete(0, 'end')
            e_dtEmissDoc.delete(0, 'end')
            e_chaveNFECompra.delete(0, 'end')
            e_valorICMSAquis.delete(0, 'end')
            e_numeroParcelas.delete(0, 'end')
            e_dtMovimento.delete(0, 'end')
            combo_movimento.set('')
            e_valorICMSMensal.delete(0, 'end')
            e_codigoItemEstoque.delete(0, 'end')
            e_centroCusto.delete(0, 'end')
            e_conta.delete(0, 'end')

            # Remover o botão de confirmação
            botao_confirmar.destroy()
            botao_cancelar.destroy()



        botao_cancelar = ctk.CTkButton(
            frameMeio,
            command=cancelar,
            text=" Cancelar".upper(),  # Texto do botão
            font=("Ivy", 12, 'bold'),  # Fonte do texto
            fg_color="red",  # Cor de fundo do botão
            text_color=co0,  # Cor do texto
            width=120,  # Largura do botão
            height=30,  # Altura do botão
            border_color="red",  # Cor da borda
            border_width=1  # Largura da borda
        )

        # Posicionando o botão na tela
        botao_cancelar.place(x=870, y=260)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

#função atualizar

def deletar():
    global tree
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        resposta = messagebox.askyesno("Confirmação", "Você tem certeza que deseja deletar este item?")

        if resposta:
            deletar_form([valor])

            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            mostrar()
        else:
            messagebox.showinfo('Cancelado', "A exclusão foi cancelada")

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')



def procurar():
    # Obter valores dos campos de entrada
    numero_registro = e_numeroRegistro.get()
    tipo_registro = e_tipoRegistro.get()
    numero_tabela = e_numeroTabela.get()
    nome_tabela = e_nomeTabela.get()
    codigo_bem = e_codigoBem.get()
    sequencia_bem = e_sequenciaBem.get()
    fornecedor = e_fornecedor.get()
    endereco_fornecedor = e_enderecoFornecedor.get()
    descricao_bem = e_descricaoBem.get()
    numero_doc_aquis = e_numDocAquis.get()
    serie_doc_compra = e_serieDocCompra.get()
    tipo_doc_compra = e_tipoDocCompra.get()
    dt_emiss_doc = e_dtEmissDoc.get()
    chave_nfe_compra = e_chaveNFECompra.get()
    valor_icms_aquis = e_valorICMSAquis.get()
    numero_parcelas = e_numeroParcelas.get()
    dt_movimento = e_dtMovimento.get()
    tipo_movimento = combo_movimento.get()
    valor_icms_mensal = e_valorICMSMensal.get()
    codigo_item_estoque = e_codigoItemEstoque.get()
    centro_custo = e_centroCusto.get()
    conta = e_conta.get()

    # Lista de campos para busca
    campos_busca = {
        'numero_registro': numero_registro,
        'tipo_registro': tipo_registro,
        'numero_tabela': numero_tabela,
        'nome_tabela': nome_tabela,
        'codigo_bem': codigo_bem,
        'sequencia_bem': sequencia_bem,
        'fornecedor': fornecedor,
        'endereco_fornecedor': endereco_fornecedor,
        'descricao_bem': descricao_bem,
        'numero_doc_aquis': numero_doc_aquis,
        'serie_doc_compra': serie_doc_compra,
        'tipo_doc_compra': tipo_doc_compra,
        'dt_emiss_doc': dt_emiss_doc,
        'chave_nfe_compra': chave_nfe_compra,
        'valor_icms_aquis': valor_icms_aquis,
        'numero_parcelas': numero_parcelas,
        'dt_movimento': dt_movimento,
        'tipo_movimento': tipo_movimento,
        'valor_icms_mensal': valor_icms_mensal,
        'codigo_item_estoque': codigo_item_estoque,
        'centro_custo': centro_custo,
        'conta': conta
    }

    # Filtrando a lista de dados que vão ser exibidos
    resultados = []

    # A função 'consultar_dados' pode ser um exemplo, onde você consulta no banco de dados ou na lista.
    for item in lista_dados:  # Aqui 'lista_dados' pode ser a lista de todos os dados que você possui (pode ser um banco de dados, lista local, etc.)
        corresponde = True  # Inicialmente assume que todos os dados correspondem.

        for campo, valor in campos_busca.items():
            if valor and valor != item.get(campo):  # Se um campo foi preenchido e não for igual ao item, não corresponde
                corresponde = False
                break

        if corresponde:
            resultados.append(item)

    # Exibir resultados na árvore (treeview)
    for row in tree.get_children():
        tree.delete(row)  # Limpar a lista exibida

    for resultado in resultados:
        tree.insert("", "end", values=resultado)




#criando logo no frameCima
app_logo = ctk.CTkLabel(frameCima, image=app_img, text='                   CONTROLE DE CRÉDITO DE ICMS DO ATIVO PERMANENTE', width=900, compound='left', anchor='nw', font=('Verdana', 20, 'bold'), text_color=co4, fg_color=co1)
app_logo.place(x=0,y=0)


e_numeroRegistro = label_entry(frameMeio, "NÚMERO DE REGISTRO:",15,10)
e_tipoRegistro = label_entry(frameMeio,"TIPO DE REGISTRO:",15,40)
e_numeroTabela = label_entry(frameMeio,"NÚMERO DA TABELA:", 15,70)
e_nomeTabela = label_entry(frameMeio,"NOME DA TABELA:",15,100)
e_codigoBem = label_entry(frameMeio,"CÓDIGO DO BEM:",15,130)
e_sequenciaBem = label_entry(frameMeio,'SEQUÊNCIA DO BEM:',15,160)
e_fornecedor = label_entry(frameMeio,"FORNECEDOR:",15,190)
e_enderecoFornecedor = label_entry(frameMeio,"ENDEREÇO DO FORNEC.:",15,220)
e_descricaoBem = label_entry(frameMeio,"DESCRIÇÃO DO BEM:",15,250)
e_numDocAquis = label_entry(frameMeio,"NUM DOC. AQUISUIÇÃO:",15,280)
e_serieDocCompra = label_entry(frameMeio,"SÉRIE DOC. COMPRA:", 15,310)
e_tipoDocCompra = label_entry(frameMeio,"TIPO DOC. COMPRA:",450,10)

dtEmissDoc = ctk.CTkLabel(frameMeio, text='DATA DE EMISSÃO:', font=('Ivy', 12, 'bold'), text_color=co4, fg_color=co1)
dtEmissDoc.place(x=450, y=40)
e_dtEmissDoc = label_entry(frameMeio,"DATA DE EMISSÃO:",450,40)

e_chaveNFECompra = label_entry(frameMeio,"CHAVE NFE COMPRA:",450,70)
e_valorICMSAquis = label_entry(frameMeio,'VALOR ICMS AQUIS.:',450,100)
e_numeroParcelas = label_entry(frameMeio,"NÚMERO DE PARCELAS:",450,130)

# Label para a data de movimento

e_dtMovimento = label_entry(frameMeio,"DATA MOVIMENTO:",450,160)

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
tipoMovimento = ctk.CTkLabel(frameMeio, text='TIPO MOVIMENTO:', height=1, anchor='nw', font=('Ivy', 12, 'bold'), text_color=co4, fg_color=co1)
tipoMovimento.place(x=450, y=195)

# Adicionando o CTkComboBox para selecionar o tipo de movimento
combo_movimento = ctk.CTkComboBox(frameMeio, values=opcoes_Movimento, width=240,height=23, font=('Ivy', 12, 'bold'))
combo_movimento.place(x=590, y=191)


e_valorICMSMensal = label_entry(frameMeio,"VALOR ICMS MENSAL:",450,220)
e_codigoItemEstoque = label_entry(frameMeio,"CÓDIGO ITEM ESTOQUE:",450,250)
e_centroCusto = label_entry(frameMeio,"CENTRO DE CUSTOS:",450,280)
e_conta = label_entry(frameMeio,"CONTA:",450,310)




# Abrindo a imagem
imagem_inserir = Image.open('icons8-add-50.png')  # Caminho para a imagem
imagem_inserir = imagem_inserir.resize((20, 20))  # Redimensionando a imagem
imagem_inserir = ctk.CTkImage(imagem_inserir)  # Converta para PhotoImage para o Tkinter

botao_inserir = ctk.CTkButton(
    frameMeio,
    command=inserir,
    image=imagem_inserir,
    text='ADICIONAR'.upper(),
    compound="left",  # Texto à esquerda da imagem
    anchor="nw",  # Alinhamento do texto
    font=("Ivy", 12, 'bold'),  # Fonte do texto
    fg_color="#F0F0F0",  # Cor de fundo do botão
    text_color=co0,  # Cor do texto
    width=120,  # Largura do botão
    height=30,# Altura do botão
    border_color="grey",  # Cor da borda
    border_width=1 # Largura da borda
)

# Posicionando o botão na tela
botao_inserir.place(x=870, y=10)


# Abrindo a imagem
imagem_atualizar = Image.open('icons8-update-80.png')  # Caminho para a imagem
imagem_atualizar = imagem_atualizar.resize((20, 20))  # Redimensionando a imagem
imagem_atualizar = ctk.CTkImage(imagem_atualizar)  # Converta para PhotoImage para o Tkinter

# Criando o botão no customtkinter (CTkButton)
botao_atualizar = ctk.CTkButton(
    frameMeio,
    command=atualizar,
    image=imagem_atualizar,  # Imagem do botão
    text=" ATUALIZAR".upper(),  # Texto do botão
    compound="left",  # Texto à esquerda da imagem
    anchor="nw",  # Alinhamento do texto
    font=("Ivy", 12, 'bold'),  # Fonte do texto
    fg_color="#F0F0F0",  # Cor de fundo do botão
    text_color=co0,  # Cor do texto
    width=120,  # Largura do botão
    height=30,# Altura do botão
    border_color="grey",  # Cor da borda
    border_width=1 # Largura da borda
)

# Posicionando o botão na tela
botao_atualizar.place(x=870, y=50)

# Abrindo a imagem
imagem_deletar = Image.open('icons8-delete-50.png')  # Caminho para a imagem
imagem_deletar = imagem_deletar.resize((20, 20))  # Redimensionando a imagem
imagem_deletar = ctk.CTkImage(imagem_deletar)  # Converta para PhotoImage para o Tkinter

# Criando o botão no customtkinter (CTkButton)
botao_deletar = ctk.CTkButton(
    frameMeio,
    command=deletar,
    image=imagem_deletar,  # Imagem do botão
    text=" DELETAR".upper(),  # Texto do botão
    compound="left",  # Texto à esquerda da imagem
    anchor="nw",  # Alinhamento do texto
    font=("Ivy", 12,'bold'),  # Fonte do texto
    fg_color="#F0F0F0",  # Cor de fundo do botão
    text_color=co0,  # Cor do texto
    width=120,  # Largura do botão
    height=30, # Altura do botão
    border_color="grey",  # Cor da borda
    border_width=1  # Largura da borda
)

# Posicionando o botão na tela
botao_deletar.place(x=870, y=90)

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
    font=("Ivy", 12, 'bold'),  # Fonte do texto
    fg_color="#F0F0F0",  # Cor de fundo do botão
    text_color=co0,  # Cor do texto
    width=120,  # Largura do botão
    height=30,  # Altura do botão
    border_color="grey",  # Cor da borda
    border_width=1  # Largura da borda
)

# Posicionando o botão na tela
botao_procurar.place(x=870, y=130)




# Função para mostrar a tabela
def mostrar():
    # Cabeçalhos da tabela
    global tree

    tabela_head = ['COD', 'Número do Registro', 'Tipo do Registro', 'Número da Tabela', 'Nome da Tabela', 'Código Bem',
                   'Sequência Bem', 'Fornecedor', 'Endereço Fornecedor', 'Descrição do Bem',
                   'Número Documento Aquisição', 'Série do Documento Compra', 'Tipo Documento Compra', 'Data de Emissão do Documento',
                   'Chave NFE Compra', 'Valor ICMS Aquisição', 'Numero de Parcelas', 'Data de Movimento', 'Tipo de Movimento',
                   'Valor ICMS Mensal', 'Código Item Estoque', 'Centro de Custo', 'Conta']

    # Obtendo os dados para a tabela
    lista_itens = ver_form()  #Substitua isso pela sua função que retorna os dados

    for widget in frameBaixo.winfo_children():
        widget.destroy()

    # Criando o Canvas para rolagem dentro do frameBaixo
    canvas = tk.Canvas(frameBaixo)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Criando as barras de rolagem
    vsb = ttk.Scrollbar(frameBaixo,orient="vertical",command=canvas.yview)
    vsb.grid(row=0, column=1, sticky="ns")

    # Barra de rolagem vertical
    hsb = ttk.Scrollbar(frameBaixo,orient="horizontal", command=canvas.xview)
    hsb.grid(row=1, column=0, sticky="ew")  # Barra de rolagem horizontal

    # Configurando o Canvas para usar as barras de rolagem
    canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Criando o Frame onde a Treeview vai ficar
    tree_frame = tk.Frame(canvas)

    tree_frame.grid(row=0,column=0, sticky='nsew')

    # Criando a Treeview
    tree = ttk.Treeview(tree_frame, columns=tabela_head, show="headings", yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(row=0, column=0, sticky="nsew")  # Usando grid em vez de pack para maior controle

    # Adicionando os cabeçalhos da tabela
    for col in tabela_head:
        tree.heading(col, text=col)

    # Inserindo os dados na Treeview
    for item in lista_itens:
        tree.insert("", "end", values=item)


    canvas.create_window((0,0), window=tree_frame, anchor='nw')

    # Atualizando a área visível do canvas após adicionar os widgets
    tree_frame.update_idletasks()  # Atualiza o layout para garantir que o canvas tenha o tamanho correto

    # Ajustando a área de rolagem do canvas após inserir os itens
    canvas.config(scrollregion=canvas.bbox("all"))  # Ajusta a área de rolagem para o tamanho do conteúdo

    # Configuração do layout de rolagem
    frameBaixo.grid_rowconfigure(0, weight=1)  # Faz o Frame expandir verticalmente
    frameBaixo.grid_columnconfigure(0, weight=1)  # Ajuste a coluna para expandir proporcionalmente

    # Configurando o Frame para redimensionar junto com o canvas
    tree_frame.grid_rowconfigure(0, weight=1)  # Garantir que a Treeview ocupe o espaço disponível
    tree_frame.grid_columnconfigure(0, weight=1)

    vsb.config(command=tree.yview)

    tree.grid(row=0,column=0, sticky='nsew')

def exportar_para_txt():
    dados = ver_form()  # Pega todos os dados da tabela

    # Caminho absoluto para o arquivo
    caminho = r'C:\Users\Parasmo\PycharmProjects\CIAP\pythonProject\produtos_exportados.txt'

    if not dados:  # Verifica se não há dados
        print("Nenhum dado encontrado para exportar.")
        return

    # Definindo os campos com o tipo de dado e o número de caracteres
    campos = [
        ("Número do Registro", "Numérico", 8),
        ("Tipo Registro", "Numérico", 1),
        ("Número da Tabela", "Numérico", 3),
        ("Nome da Tabela", "Alfanumérico", 30),
        ("Código Bem", "Alfanumérico", 30),
        ("Sequência Bem", "Numérico", 4),
        ("Fornecedor", "Numérico", 14),
        ("Endereço Fornecedor", "Numérico", 4),
        ("Descrição Bem", "Alfanumérico", 60),
        ("Número Documento Aquisição", "Numérico", 9),
        ("Série Documento Compra", "Numérico", 3),
        ("Tipo Documento Compra", "Numérico", 4),
        ("Data Emissão Documento", "Data", 8),
        ("Chave NFE Compra", "Alfanumérico", 44),
        ("Valor ICMS Aquisição", "Numérico", 16),
        ("Número Parcelas", "Numérico", 2),
        ("Data Movimento", "Data", 8),
        ("Tipo de Movimento", "Alfanumérico", 2),  # Este campo deve pegar apenas os dois primeiros caracteres
        ("Valor ICMS Mensal", "Numérico", 16),
        ("Código Item Estoque", "Alfanumérico", 30),
        ("Centro de Custo", "Alfanumérico", 10),
        ("Conta", "Alfanumérico", 20)
    ]

    try:
        # Abre o arquivo para escrita
        with open(caminho, "w") as f:
            # Para cada linha de dados no banco, escrevemos os dados concatenados em uma linha do arquivo
            for row in dados:
                linha = ""
                for i, (campo, tipo, tamanho) in enumerate(campos):
                    valor = str(row[i + 1]).strip()  # Obtemos o valor do campo (row[1], row[2], ...)

                    if tipo == "Numérico":

                        valor=valor.replace('.','').replace(',','')
                        # Se for numérico, completamos com zeros à esquerda
                        valor = valor[:tamanho].zfill(tamanho)
                    elif tipo == "Alfanumérico":
                        valor= valor[:tamanho].ljust(tamanho)
                        # Se for alfanumérico, completamos com espaços à direita
                        if campo == "Tipo de Movimento":
                            # Para o campo "Tipo de Movimento", pegamos apenas os dois primeiros caracteres
                            valor = valor[:2].ljust(tamanho)
                        else:
                            valor = valor[:tamanho].ljust(tamanho)
                    elif tipo == "Data":
                        # Para data, formatamos como DDMMYYYY (sem separadores)
                        valor = valor.replace("/", "").zfill(tamanho)  # Remove barras e preenche com zeros à esquerda

                    # Concatenando os valores de cada campo
                    linha += valor  # Sem adicionar espaço entre os campos

                # Escrever a linha no arquivo
                f.write(linha + "\n")

        print(f"Dados exportados com sucesso para {caminho}")

    except Exception as e:
        print(f"Erro ao exportar os dados: {e}")


# Chama a função para exibir a interface
exportar_para_txt()
mostrar()
janela.mainloop()

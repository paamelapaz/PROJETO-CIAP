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
janela.geometry('1050x700')  # Tamanho da janela
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

def label_entry(frame,label_text, pos_x,pos_y):
    label= ctk.CTkLabel(frame, text=label_text, font=('Ivy',12,'bold'),text_color=co4, fg_color=co1)
    label.place(x=pos_x,y=pos_y)
    entry = ctk.CTkEntry(frame, width=170)
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
        botao_confirmar.place(x=770, y=220)

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

        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')


#criando logo no frameCima
app_logo = ctk.CTkLabel(frameCima, image=app_img, text='            CONTROLE DE CRÉDITO DE ICMS DO ATIVO PERMANENTE', width=900, compound='left', anchor='nw', font=('Verdana', 20, 'bold'), text_color=co4, fg_color=co1)
app_logo.place(x=0,y=0)


e_numeroRegistro = label_entry(frameMeio, "Número do Registro:",10,10)
e_tipoRegistro = label_entry(frameMeio,"Tipo de Registro:",10,40)
e_numeroTabela = label_entry(frameMeio,"Número da Tabela:", 10,70)
e_nomeTabela = label_entry(frameMeio,"Nome da Tabela:",10,100)
e_codigoBem = label_entry(frameMeio,"Código do Bem",10,130)
e_sequenciaBem = label_entry(frameMeio,'Sequência do Bem',10,160)
e_fornecedor = label_entry(frameMeio,"Fornecedor:",10,190)
e_enderecoFornecedor = label_entry(frameMeio,"Endereço do Fornec.:",10,220)
e_descricaoBem = label_entry(frameMeio,"Descrição do Bem:",10,250)
e_numDocAquis = label_entry(frameMeio,"Num Doc. Aquisição:",10,280)
e_serieDocCompra = label_entry(frameMeio,"Serie Doc. Compra:", 10,310)
e_tipoDocCompra = label_entry(frameMeio,"Tipo Doc. Compra:",400,10)

dtEmissDoc = ctk.CTkLabel(frameMeio, text='Data de Emissão:', font=('Ivy', 12, 'bold'), text_color=co4, fg_color=co1)
dtEmissDoc.place(x=400, y=40)

# Adicionando o DateEntry do tkcalendar
e_dtEmissDoc = DateEntry(frameMeio, width=16, font=('Ivy', 12, 'bold'), background='darkblue', foreground='white', borderwidth=2, year=2024, date_pattern='dd/mm/yyyy')
e_dtEmissDoc.place(x=540, y=41)
e_dtEmissDoc = label_entry(frameMeio,"Data de Emissão",400,40)

e_chaveNFECompra = label_entry(frameMeio,"Chave NFE Compra:",400,70)
e_valorICMSAquis = label_entry(frameMeio,'Valor ICMS Aquis:',400,100)
e_numeroParcelas = label_entry(frameMeio,"Número de Parcelas:",400,130)

# Label para a data de movimento
dtMovimento = ctk.CTkLabel(frameMeio, text='Data Movimento:', height=1, anchor='nw', font=('Ivy', 12, 'bold'), text_color=co4, fg_color=co1)
dtMovimento.place(x=400, y=160)

# Adicionando o DateEntry para Data Movimento
e_dtMovimento = DateEntry(frameMeio, width=16, font=('Ivy', 12, 'bold'), background='darkblue', foreground='white', borderwidth=2, year=2024, date_pattern='dd/mm/yyyy')
e_dtMovimento.place(x=540, y=161)
e_dtMovimento = label_entry(frameMeio,"Data de Emissão",400,160)

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


e_valorICMSMensal = label_entry(frameMeio,"Valor ICMS Mensal:",400,220)
e_codigoItemEstoque = label_entry(frameMeio,"Código Item Estoque:",400,250)
e_centroCusto = label_entry(frameMeio,"Centro de Custo",400,280)
e_conta = label_entry(frameMeio,"Conta:",400,310)




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
botao_inserir.place(x=770, y=10)


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
botao_atualizar.place(x=770, y=50)

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
    font=("Ivy", 12, 'bold'),  # Fonte do texto
    fg_color="#F0F0F0",  # Cor de fundo do botão
    text_color=co0,  # Cor do texto
    width=120,  # Largura do botão
    height=30,  # Altura do botão
    border_color="grey",  # Cor da borda
    border_width=1  # Largura da borda
)

# Posicionando o botão na tela
botao_procurar.place(x=770, y=130)




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
    lista_itens = ver_form()

    # Limpando o conteúdo existente no frameBaixo
    for widget in frameBaixo.winfo_children():
        widget.destroy()

    # Criando o Canvas para rolagem dentro do frameBaixo
    canvas = ctk.CTkCanvas(frameBaixo)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Criando as barras de rolagem
    vsb = ctk.CTkScrollbar(frameBaixo, command=canvas.yview)
    vsb.grid(row=0, column=1, sticky="ns")  # Barra de rolagem vertical

    hsb = ctk.CTkScrollbar(frameBaixo, command=canvas.xview, orientation="horizontal")
    hsb.grid(row=1, column=0, sticky="ew")  # Barra de rolagem horizontal

    # Configurando o Canvas para usar as barras de rolagem
    canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Criando o Frame onde a Treeview vai ficar
    tree_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=tree_frame, anchor="nw")

    # Criando a Treeview
    tree = ttk.Treeview(tree_frame, columns=tabela_head, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    # Adicionando os cabeçalhos da tabela
    for col in tabela_head:
        tree.heading(col, text=col)

    # Inserindo os dados na Treeview
    for item in lista_itens:
        tree.insert("", "end", values=item)

    # Atualizando a área visível do canvas após adicionar os widgets
    tree_frame.update_idletasks()  # Atualiza o layout para garantir que o canvas tenha o tamanho correto

    # Ajustando a área de rolagem do canvas após inserir os itens
    canvas.config(scrollregion=canvas.bbox("all"))  # Ajusta a área de rolagem para o tamanho do conteúdo

    # Configuração do layout de rolagem
    frameBaixo.grid_rowconfigure(0, weight=1)  # Faz o Frame expandir verticalmente
    frameBaixo.grid_columnconfigure(0, weight=1)  # Faz o Frame expandir horizontalmente

# Chama a função para exibir a interface
mostrar()
janela.mainloop()
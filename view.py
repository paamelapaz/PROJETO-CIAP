# importando sqlite

import sqlite3 as lite

#criando conexão
con = lite.connect ('dados.db')

#CRUD

# INSERIR DADOS
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO produtos(numero_registro, tipo_registro, numero_tabela, nome_tabela, codigo_do_bem, sequencia_do_bem, fornecedor, endereco_fornecedor, descricao_bem, numero_doc_aquisicao, serie_doc_compra, tipo_doc_compra, data_emissao_compra, chave_nfe_compra, valor_icms_aquisicao, numero_parcelas, data_movimento, tipo_movimento, valor_icms_mensal, codigo_item_estoque, centro_custo, conta) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query,i)

# ATUALIZAR DADOS
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE produtos SET numero_registro = ?, tipo_registro = ?, numero_tabela = ?, nome_tabela = ?, codigo_do_bem = ?, sequencia_do_bem = ?, fornecedor = ?, endereco_fornecedor = ?, descricao_bem = ?, numero_doc_aquisicao = ?, serie_doc_compra = ?, tipo_doc_compra = ?, data_emissao_compra = ?, chave_nfe_compra = ?, valor_icms_aquisicao = ?, numero_parcelas = ?, data_movimento = ?, tipo_movimento = ?, valor_icms_mensal = ?, codigo_item_estoque = ?, centro_custo = ?, conta = ? WHERE id = ?"
        cur.execute(query,i)

#DELETAR DADOS
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM produtos WHERE id =?"
        cur.execute(query,i)

#VER TODOS OS DADOS
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produtos"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
        return ver_dados


# VER DADOS INDIVIDUAL
def ver_item(id):
    print(id)
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produtos WHERE id = ?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)
    return ver_dados_individual


















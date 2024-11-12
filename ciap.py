# importando sqlite

import sqlite3 as lite

# criando conexão

con = lite.connect ('dados.db')

# criando tabela

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, numero_registro INTEGER, tipo_registro INTEGER, numero_tabela INTEGER, nome_tabela VARCHAR(30), codigo_do_bem VARCHAR(30), sequencia_do_bem INTEGER, fornecedor INTEGER, endereco_fornecedor INTEGER, descricao_bem VARCHAR(60), numero_doc_aquisicao INTEGER, serie_doc_compra INTEGER, tipo_doc_compra INTEGER, data_emissao_compra DATE, chave_nfe_compra VARCHAR (44), valor_icms_aquisicao DECIMAL, numero_parcelas INTEGER, data_movimento DATE, tipo_movimento VARCHAR(2), valor_icms_mensal DECIMAL, codigo_item_estoque VARCHAR(30), centro_custo VARCHAR(10), conta VARCHAR(20))")



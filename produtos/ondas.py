import pandas as pd
import pyodbc


class Produto:
    pass

class Estoque:
    pass


def produtos(tabela):

    server = '192.168.2.11'
    db = 'ondas800'
    user = 'timur'
    pwd = 'p$3dasony' 
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';UID=' + user + ';PWD=' + pwd)
    
    query = """
        select p.PRODUTO,ep.COR_PRODUTO,pp.PRECO1,p.GRADE,pt.TAMANHOS_DIGITADOS,pt.TAMANHO_1,pt.TAMANHO_2,pt.TAMANHO_3,
        pt.TAMANHO_4,pt.TAMANHO_5,pt.TAMANHO_6,pt.TAMANHO_7,pt.TAMANHO_8,
        pt.TAMANHO_9,pt.TAMANHO_10,pt.TAMANHO_11,pt.TAMANHO_12,
        ep.ES1,ep.ES2,ep.ES3,ep.ES4,ep.ES5,ep.ES6,ep.ES7,ep.ES8,ep.ES9,ep.ES10,ep.ES11,ep.ES12
        from PRODUTOS p 
        left join produtos_tamanhos pt on p.GRADE=pt.GRADE
        left join PRODUTOS_PRECOS pp on p.PRODUTO=pp.PRODUTO and pp.CODIGO_TAB_PRECO='%s'
        left join ESTOQUE_PRODUTOS ep on ep.FILIAL='ONDAS' and ep.PRODUTO=p.PRODUTO
        where p.COLECAO='2001' and ep.ESTOQUE>0
        order by ep.PRODUTO
    """%(tabela)
    
    prods = pd.read_sql(query,conn)
    
    prods['PRODUTO'] = prods['PRODUTO'].str.strip()
    prods['COR_PRODUTO'] = prods['COR_PRODUTO'].str.strip()
    
    lista_produtos =[]
    
    prod_ant = ''
    
    p = Produto()
    p.produto = 'ERRO'
    
    for index, row in prods.iterrows():
        
        if row['PRODUTO']==prod_ant:
            
            estq = Estoque()
            estq.cor = row['COR_PRODUTO']
            
            es = []
            for i in range(p.qtd_tams):
                t =i+1
                es.append(row['ES'+str(t)])
            estq.qtds = es
            p.estoque.append(estq)
            
        else:            
            if p.produto != 'ERRO':            
                lista_produtos.append(p)
            
            p = Produto()
            
            p.produto = row['PRODUTO']
            p.qtd_tams = row['TAMANHOS_DIGITADOS']
            p.preco = row['PRECO1']
            p.url = 'imgs/'+p.produto+'.jpg'
            p.estoque = []
            
            tams = []
            for i in range(p.qtd_tams):
                t =i+1
                tams.append(row['TAMANHO_'+str(t)])
            p.tams = tams
            
            estq = Estoque()
            estq.cor = row['COR_PRODUTO']
            
            es = []
            for i in range(p.qtd_tams):
                t =i+1
                es.append(row['ES'+str(t)])
            estq.qtds = es
            p.estoque.append(estq)
        
        
        
        prod_ant = row['PRODUTO']
        
    return lista_produtos

def produtos_col(tabela,colecao):

    server = '192.168.2.11'
    db = 'ondas800'
    user = 'timur'
    pwd = 'p$3dasony' 
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';UID=' + user + ';PWD=' + pwd)
    
    query = """
        select p.PRODUTO,ep.COR_PRODUTO,pp.PRECO1,p.GRADE,pt.TAMANHOS_DIGITADOS,pt.TAMANHO_1,pt.TAMANHO_2,pt.TAMANHO_3,
        pt.TAMANHO_4,pt.TAMANHO_5,pt.TAMANHO_6,pt.TAMANHO_7,pt.TAMANHO_8,
        pt.TAMANHO_9,pt.TAMANHO_10,pt.TAMANHO_11,pt.TAMANHO_12,
        ep.ES1,ep.ES2,ep.ES3,ep.ES4,ep.ES5,ep.ES6,ep.ES7,ep.ES8,ep.ES9,ep.ES10,ep.ES11,ep.ES12
        from PRODUTOS p 
        left join produtos_tamanhos pt on p.GRADE=pt.GRADE
        left join PRODUTOS_PRECOS pp on p.PRODUTO=pp.PRODUTO and pp.CODIGO_TAB_PRECO='%s'
        left join ESTOQUE_PRODUTOS ep on ep.FILIAL='ONDAS' and ep.PRODUTO=p.PRODUTO
        where p.COLECAO='%s' and ep.ESTOQUE>0
        order by ep.PRODUTO
    """%(tabela,colecao)
    
    prods = pd.read_sql(query,conn)
    
    prods['PRODUTO'] = prods['PRODUTO'].str.strip()
    prods['COR_PRODUTO'] = prods['COR_PRODUTO'].str.strip()
    
    lista_produtos =[]
    
    prod_ant = ''
    
    p = Produto()
    p.produto = 'ERRO'
    
    for index, row in prods.iterrows():
        
        if row['PRODUTO']==prod_ant:
            
            estq = Estoque()
            estq.cor = row['COR_PRODUTO']
            
            es = []
            for i in range(p.qtd_tams):
                t =i+1
                es.append(row['ES'+str(t)])
            estq.qtds = es
            p.estoque.append(estq)
            
        else:            
            if p.produto != 'ERRO':            
                lista_produtos.append(p)
            
            p = Produto()
            
            p.produto = row['PRODUTO']
            p.qtd_tams = row['TAMANHOS_DIGITADOS']
            p.preco = row['PRECO1']
            p.url = 'imgs/'+p.produto+'.jpg'
            p.estoque = []
            
            tams = []
            for i in range(p.qtd_tams):
                t =i+1
                tams.append(row['TAMANHO_'+str(t)])
            p.tams = tams
            
            estq = Estoque()
            estq.cor = row['COR_PRODUTO']
            
            es = []
            for i in range(p.qtd_tams):
                t =i+1
                es.append(row['ES'+str(t)])
            estq.qtds = es
            p.estoque.append(estq)
        
        
        
        prod_ant = row['PRODUTO']
        
    return lista_produtos

def produtos_col_cat(tabela,colecao,categoria):

    server = '192.168.2.11'
    db = 'ondas800'
    user = 'timur'
    pwd = 'p$3dasony' 
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';UID=' + user + ';PWD=' + pwd)
    
    query = """
        select p.PRODUTO,pc.CATEGORIA_PRODUTO,psc.SUBCATEGORIA_PRODUTO,ep.COR_PRODUTO,
        pp.PRECO1,p.GRADE,pt.TAMANHOS_DIGITADOS,pt.TAMANHO_1,pt.TAMANHO_2,pt.TAMANHO_3,
        pt.TAMANHO_4,pt.TAMANHO_5,pt.TAMANHO_6,pt.TAMANHO_7,pt.TAMANHO_8,
        pt.TAMANHO_9,pt.TAMANHO_10,pt.TAMANHO_11,pt.TAMANHO_12,
        ep.ES1,ep.ES2,ep.ES3,ep.ES4,ep.ES5,ep.ES6,ep.ES7,ep.ES8,ep.ES9,ep.ES10,ep.ES11,ep.ES12
        from PRODUTOS p 
        left join produtos_tamanhos pt on p.GRADE=pt.GRADE
        left join PRODUTOS_PRECOS pp on p.PRODUTO=pp.PRODUTO and pp.CODIGO_TAB_PRECO='%s'
        left join ESTOQUE_PRODUTOS ep on ep.FILIAL='ONDAS' and ep.PRODUTO=p.PRODUTO
        left join PRODUTOS_CATEGORIA pc on p.COD_CATEGORIA=pc.COD_CATEGORIA
        left join PRODUTOS_SUBCATEGORIA psc on p.COD_SUBCATEGORIA=psc.COD_SUBCATEGORIA
        where p.COLECAO='%s' and ep.ESTOQUE>0
        order by ep.PRODUTO
    """%(tabela,colecao)
    
    prods = pd.read_sql(query,conn)
    
    prods['PRODUTO'] = prods['PRODUTO'].str.strip()
    prods['COR_PRODUTO'] = prods['COR_PRODUTO'].str.strip()
    
    lista_produtos =[]
    
    prod_ant = ''
    
    p = Produto()
    p.produto = 'ERRO'
    
    for index, row in prods.iterrows():
        
        if row['PRODUTO']==prod_ant:
            
            estq = Estoque()
            estq.cor = row['COR_PRODUTO']
            
            es = []
            for i in range(p.qtd_tams):
                t =i+1
                es.append(row['ES'+str(t)])
            estq.qtds = es
            p.estoque.append(estq)
            
        else:            
            if p.produto != 'ERRO':            
                lista_produtos.append(p)
            
            p = Produto()
            
            p.produto = row['PRODUTO']
            p.qtd_tams = row['TAMANHOS_DIGITADOS']
            p.preco = row['PRECO1']
            p.url = 'imgs/'+p.produto+'.jpg'
            p.estoque = []
            
            tams = []
            for i in range(p.qtd_tams):
                t =i+1
                tams.append(row['TAMANHO_'+str(t)])
            p.tams = tams
            
            estq = Estoque()
            estq.cor = row['COR_PRODUTO']
            
            es = []
            for i in range(p.qtd_tams):
                t =i+1
                es.append(row['ES'+str(t)])
            estq.qtds = es
            p.estoque.append(estq)
        
        
        
        prod_ant = row['PRODUTO']
        
    return lista_produtos

def categorias():

    server = '192.168.2.11'
    db = 'ondas800'
    user = 'timur'
    pwd = 'p$3dasony' 
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';UID=' + user + ';PWD=' + pwd)

    query = """
        select distinct CATEGORIA_PRODUTO from PRODUTOS_CATEGORIA
    """

    categorias = pd.read_sql(query,conn)

    categorias['CATEGORIA_PRODUTO'] = categorias['CATEGORIA_PRODUTO'].str.strip()

    cats = []

    for index, row in categorias.iterrows():
        cats.append(row['CATEGORIA_PRODUTO'])

    return cats
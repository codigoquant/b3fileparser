META_DATA = {    
    "TIPREG":{'name':"TIPO_DE_REGISTRO", 'size':2, 'dtype':'category'},
    "DATAPR":{'name':"DATA_DO_PREGAO", 'size':8, 'dtype': 'object'},
    "CODBDI":{'name':"CODIGO_BDI", 'size':2, 'dtype':'category'},
    "CODNEG":{'name':"CODIGO_DE_NEGOCIACAO",'size':12,'dtype':'category'},
    "TPMERC":{'name':"TIPO_DE_MERCADO",'size':3, 'dtype':'category'},
    "NOMRES":{'name':"NOME_DA_EMPRESA",'size':12, 'dtype':'category'},
    "ESPECI":{'name':"ESPECIFICACAO_DO_PAPEL",'size':10, 'dtype':'category'},
    "PRAZOT":{'name':"PRAZO_EM_DIAS_DO_MERCADO_A_TERMO",'size':3, 'dtype':'object'},
    "MODREF":{'name':"MOEDA_DE_REFERENCIA",'size':4, 'dtype':'category'},
    "PREABE":{'name':"PRECO_DE_ABERTURA",'size':13, 'dtype': 'float32'},
    "PREMAX":{'name':"PRECO_MAXIMO",'size':13, 'dtype': 'float32'},
    "PREMIN":{'name':"PRECO_MINIMO",'size':13, 'dtype': 'float32'},
    "PREMED":{'name':"PRECO_MEDIO",'size':13, 'dtype': 'float32'},
    "PREULT":{'name':"PRECO_ULTIMO_NEGOCIO",'size':13, 'dtype': 'float32'},
    "PREOFC":{'name':"PRECO_MELHOR_OFERTA_DE_COMPRA",'size':13, 'dtype': 'float32'},
    "PREOFV":{'name':"PRECO_MELHOR_OFERTA_DE_VENDAS",'size':13, 'dtype': 'float32'},
    "TOTNEG":{'name':"NUMERO_DE_NEGOCIOS",'size':5, 'dtype':'object'},
    "QUATOT":{'name':"QUANTIDADE_NEGOCIADA",'size':18, 'dtype':'object'},
    "VOLTOT":{'name':"VOLUME_TOTAL_NEGOCIADO",'size':18, 'dtype': 'float64'},
    "PREEXE":{'name':"PRECO_DE_EXERCICIO",'size':13, 'dtype': 'float32'},
    "INDOPC":{'name':"INDICADOR_DE_CORRECAO_DE_PRECOS",'size':1, 'dtype':'category'},
    "DATVEN":{'name':"DATA_DE_VENCIMENTO",'size':8, 'dtype':'object'},
    "FATCOT":{'name':"FATOR_DE_COTACAO",'size':7, 'dtype':'category'},
    "PTOEXE":{'name':"PRECO_DE_EXERCICIO_EM_PONTOS",'size':13, 'dtype': 'float32'},
    "CODISI":{'name':"CODIGO_ISIN",'size':12, 'dtype':'category'},
    "DISMES":{'name':"NUMERO_DE_DISTRIBUICAO",'size':3, 'dtype':'category'}
}


MARKETS = {
    '010':'VISTA',
    '012':'EXERCICIO_DE_OPCOES_DE_COMPRA',
    '013':'EXERCÍCIO_DE_OPCOES_DE_VENDA',
    '017':'LEILAO',
    '020':'FRACIONARIO',
    '030':'TERMO',
    '050':'FUTURO_COM_RETENCAO_DE_GANHO',
    '060':'FUTURO_COM_MOVIMENTACAO_CONTINUA',
    '070':'OPCOES_DE_COMPRA',
    '080':'OPCOES_DE_VENDA'
}

INDOPC = {
    '0':'0',
    '1':'US$',
    '2':"TJLP",
    '8':"IGPM",
    '9':"URV"
}

CODBDI = {
    '00':'0',
    '02':"LOTE_PADRAO",
    '05':"SANCIONADAS PELOS REGULAMENTOS BMFBOVESPA",
    '06':"CONCORDATARIAS",
    '07':"RECUPERACAO_EXTRAJUDICIAL",
    '08':"RECUPERAÇÃO_JUDICIAL",
    '09':"REGIME_DE_ADMINISTRACAO_ESPECIAL_TEMPORARIA",
    '10':"DIREITOS_E_RECIBOS",
    '11':"INTERVENCAO",
    '12':"FUNDOS_IMOBILIARIOS",
    '13':'13',
    '14':"CERT.INVEST/TIT.DIV.PUBLICA",
    '18':"OBRIGACÕES",
    '22':"BÔNUS(PRIVADOS)",
    '26':"APOLICES/BÔNUS/TITULOS PUBLICOS",
    '32':"EXERCICIO_DE_OPCOES_DE_COMPRA_DE_INDICES",
    '33':"EXERCICIO_DE_OPCOES_DE_VENDA_DE_INDICES",
    '34':'34',
    '35':'35',
    '36':'36',
    '37':'37',
    '38':"EXERCICIO_DE_OPCOES_DE_COMPRA",
    '42':"EXERCICIO_DE_OPCOES_DE_VENDA",
    '46':"LEILAO_DE_NAO_COTADOS",
    '48':"LEILAO_DE_PRIVATIZACAO",
    '49':"LEILAO_DO_FUNDO_RECUPERACAO_ECONOMICA_ESPIRITO_SANTO",
    '50':"LEILAO",
    '51':"LEILAO_FINOR",
    '52':"LEILAO_FINAM",
    '53':"LEILAO_FISET",
    '54':"LEILAO_DE_ACÕES_EM_MORA",
    '56':"VENDAS_POR_ALVARA_JUDICIAL",
    '58':"OUTROS",
    '60':"PERMUTA_POR_ACÕES",
    '61':"META",
    '62':"MERCADO_A_TERMO",
    '66':"DEBENTURES_COM_DATA_DE_VENCIMENTO_ATE_3_ANOS",
    '68':"DEBENTURES_COM_DATA_DE_VENCIMENTO_MAIOR_QUE_3_ANOS",
    '70':"FUTURO_COM_RETENCAO_DE_GANHOS",
    '71':"MERCADO_DE_FUTURO",
    '74':"OPCOES_DE_COMPRA_DE_INDICES",
    '75':"OPCOES_DE_VENDA_DE_INDICES",
    '78':"OPCOES_DE_COMPRA",
    '82':"OPCOES_DE_VENDA",
    '83':"BOVESPAFIX",
    '84':"SOMA_FIX",
    '90':"TERMO_VISTA_REGISTRADO",
    '96':"MERCADO_FRACIONARIO",
    '99':"TOTAL_GERAL"
}

# b3fileparser

A função dessa biblioteca é fazer o parser do arquivo com cotações históricas da B3, disponíveis em https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/

## Instalação

Instalação pode ser feita via pip

```
pip install b3fileparser
```

## Exemplo 1

```python
from b3fileparser.b3parser import B3Parser


parser = B3Parser.create_parser(engine='pandas')
dados_b3 = parser.read_b3_file('COTAHIST_A2023.TXT')
dados_b3
```

> [!NOTE]
> Pode-se obter os dados em formato DataFrame `Pandas` ou `Polars`
> Configure engine para `engine='pandas'` ou `engine='polars'`

`dados_b3` é um DataFrame:

|     | TIPO_DE_REGISTRO | DATA_DO_PREGAO      | CODIGO_BDI          | CODIGO_DE_NEGOCIACAO | TIPO_DE_MERCADO | NOME_DA_EMPRESA | ESPECIFICACAO_DO_PAPEL | PRAZO_EM_DIAS_DO_MERCADO_A_TERMO | MOEDA_DE_REFERENCIA | PRECO_DE_ABERTURA | PRECO_MAXIMO | PRECO_MINIMO | PRECO_MEDIO | PRECO_ULTIMO_NEGOCIO | PRECO_MELHOR_OFERTA_DE_COMPRA | PRECO_MELHOR_OFERTA_DE_VENDAS | NUMERO_DE_NEGOCIOS | QUANTIDADE_NEGOCIADA | VOLUME_TOTAL_NEGOCIADO | PRECO_DE_EXERCICIO | INDICADOR_DE_CORRECAO_DE_PRECOS | DATA_DE_VENCIMENTO | FATOR_DE_COTACAO | PRECO_DE_EXERCICIO_EM_PONTOS | CODIGO_ISIN  | NUMERO_DE_DISTRIBUICAO |
| --: | ---------------: | :------------------ | :------------------ | :------------------- | :-------------- | :-------------- | :--------------------- | -------------------------------: | :------------------ | ----------------: | -----------: | -----------: | ----------: | -------------------: | ----------------------------: | ----------------------------: | -----------------: | -------------------: | ---------------------: | -----------------: | ------------------------------: | :----------------- | ---------------: | ---------------------------: | :----------- | ---------------------: |
|   1 |                1 | 2023-01-02 00:00:00 | 34                  | MMMC34               | VISTA           | 3M              | DRN                    |                               -1 | R$                  |            165.56 |       165.56 |       159.06 |      160.97 |               161.44 |                        161.44 |                        161.59 |                 31 |                  120 |                20443.2 |                  0 |                               0 | NaT                |                1 |                            0 | BRMMMCBDR000 |                    143 |
|   2 |                1 | 2023-01-02 00:00:00 | LOTE_PADRAO         | RRRP3                | VISTA           | 3R PETROLEUM    | ON NM                  |                               -1 | R$                  |             37.24 |        37.93 |        35.97 |       36.64 |                36.41 |                          36.4 |                         36.41 |              13731 |           2.8788e+06 |            1.05483e+08 |                  0 |                               0 | NaT                |                1 |                            0 | BRRRRPACNOR5 |                    100 |
|   3 |                1 | 2023-01-02 00:00:00 | MERCADO FRACIONARIO | RRRP3F               | FRACIONARIO     | 3R PETROLEUM    | ON NM                  |                               -1 | R$                  |             37.75 |        37.91 |        35.98 |       36.69 |                36.94 |                         36.94 |                            37 |               1309 |                24010 |                 881003 |                  0 |                               0 | NaT                |                1 |                            0 | BRRRRPACNOR5 |                    100 |
|   4 |                1 | 2023-01-02 00:00:00 | LOTE_PADRAO         | TTEN3                | VISTA           | 3TENTOS         | ON NM                  |                               -1 | R$                  |              9.65 |         9.65 |         9.07 |        9.23 |                 9.36 |                          9.35 |                          9.36 |               3292 |               701700 |            6.48253e+06 |                  0 |                               0 | NaT                |                1 |                            0 | BRTTENACNOR0 |                    101 |
|   5 |                1 | 2023-01-02 00:00:00 | MERCADO FRACIONARIO | TTEN3F               | FRACIONARIO     | 3TENTOS         | ON NM                  |                               -1 | R$                  |              9.34 |         9.44 |         9.08 |        9.26 |                  9.2 |                           9.2 |                          9.65 |                238 |                 4640 |                43069.7 |                  0 |                               0 | NaT                |                1 |                            0 | BRTTENACNOR0 |                    101 |

## Exemplo 2 - Listando Opções de Venda da Petrobras

```python
from b3fileparser.b3parser import B3Parser


parser = B3Parser.create_parser()
dados = parser.read_b3_file('COTAHIST_A2023.TXT')
puts = dados[dados['TIPO_DE_MERCADO'] == 'OPCOES_DE_VENDA']
putspetro = puts[puts['CODIGO_DE_NEGOCIACAO'].str.startswith('PETR')]
putspetro.head()
```

|       | TIPO_DE_REGISTRO | DATA_DO_PREGAO      | CODIGO_BDI      | CODIGO_DE_NEGOCIACAO | TIPO_DE_MERCADO | NOME_DA_EMPRESA | ESPECIFICACAO_DO_PAPEL | PRAZO_EM_DIAS_DO_MERCADO_A_TERMO | MOEDA_DE_REFERENCIA | PRECO_DE_ABERTURA | PRECO_MAXIMO | PRECO_MINIMO | PRECO_MEDIO | PRECO_ULTIMO_NEGOCIO | PRECO_MELHOR_OFERTA_DE_COMPRA | PRECO_MELHOR_OFERTA_DE_VENDAS | NUMERO_DE_NEGOCIOS | QUANTIDADE_NEGOCIADA | VOLUME_TOTAL_NEGOCIADO | PRECO_DE_EXERCICIO | INDICADOR_DE_CORRECAO_DE_PRECOS | DATA_DE_VENCIMENTO  | FATOR_DE_COTACAO | PRECO_DE_EXERCICIO_EM_PONTOS | CODIGO_ISIN  | NUMERO_DE_DISTRIBUICAO |
| ----: | ---------------: | :------------------ | :-------------- | :------------------- | :-------------- | :-------------- | :--------------------- | -------------------------------: | :------------------ | ----------------: | -----------: | -----------: | ----------: | -------------------: | ----------------------------: | ----------------------------: | -----------------: | -------------------: | ---------------------: | -----------------: | ------------------------------: | :------------------ | ---------------: | ---------------------------: | :----------- | ---------------------: |
| 24653 |                1 | 2023-01-02 00:00:00 | OPCOES_DE_VENDA | PETRM318             | OPCOES_DE_VENDA | PETRE           | ON N2                  |                                0 | R$                  |              0.17 |         0.22 |         0.17 |        0.19 |                 0.18 |                             0 |                             0 |                 66 |                68100 |                  13008 |              21.91 |                               0 | 2023-01-20 00:00:00 |                1 |                            0 | BRPETRACNOR9 |                    196 |
| 24654 |                1 | 2023-01-02 00:00:00 | OPCOES_DE_VENDA | PETRM328             | OPCOES_DE_VENDA | PETRE           | ON N2                  |                                0 | R$                  |              0.16 |          0.3 |         0.16 |        0.21 |                 0.29 |                             0 |                             0 |                 52 |                47800 |                  10127 |              22.91 |                               0 | 2023-01-20 00:00:00 |                1 |                            0 | BRPETRACNOR9 |                    196 |
| 24655 |                1 | 2023-01-02 00:00:00 | OPCOES_DE_VENDA | PETRN282             | OPCOES_DE_VENDA | PETRE           | ON N2                  |                                0 | R$                  |              1.11 |         1.11 |         1.07 |         1.1 |                 1.07 |                             0 |                             0 |                  9 |                22000 |                  24340 |              24.98 |                               0 | 2023-02-17 00:00:00 |                1 |                            0 | BRPETRACNOR9 |                    197 |
| 24656 |                1 | 2023-01-02 00:00:00 | OPCOES_DE_VENDA | PETRM28              | OPCOES_DE_VENDA | PETRE           | ON N2                  |                                0 | R$                  |              0.69 |         1.03 |         0.69 |        0.97 |                    1 |                             0 |                             1 |                 26 |                69600 |                  68155 |              25.66 |                               0 | 2023-01-20 00:00:00 |                1 |                            0 | BRPETRACNOR9 |                    197 |
| 24657 |                1 | 2023-01-02 00:00:00 | OPCOES_DE_VENDA | PETRM294             | OPCOES_DE_VENDA | PETRE           | ON N2                  |                                0 | R$                  |              1.09 |         1.23 |         1.04 |        1.11 |                 1.08 |                             0 |                             0 |                 12 |                 7700 |                   8616 |              26.16 |                               0 | 2023-01-20 00:00:00 |                1 |                            0 | BRPETRACNOR9 |                    197 |

## Sobre os dados

O parse do arquivo é realizado de acordo com o Layout fornecido pela b3: https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf

### Colunas

|     | COLUNA                           | TAMANHO NO ARQUIVO TXT |
| --: | :------------------------------- | ---------------------: |
|   0 | TIPO_DE_REGISTRO                 |                      2 |
|   1 | DATA_DO_PREGAO                   |                      8 |
|   2 | CODIGO_BDI                       |                      2 |
|   3 | CODIGO_DE_NEGOCIACAO             |                     12 |
|   4 | TIPO_DE_MERCADO                  |                      3 |
|   5 | NOME_DA_EMPRESA                  |                     12 |
|   6 | ESPECIFICACAO_DO_PAPEL           |                     10 |
|   7 | PRAZO_EM_DIAS_DO_MERCADO_A_TERMO |                      3 |
|   8 | MOEDA_DE_REFERENCIA              |                      4 |
|   9 | PRECO_DE_ABERTURA                |                     13 |
|  10 | PRECO_MAXIMO                     |                     13 |
|  11 | PRECO_MINIMO                     |                     13 |
|  12 | PRECO_MEDIO                      |                     13 |
|  13 | PRECO_ULTIMO_NEGOCIO             |                     13 |
|  14 | PRECO_MELHOR_OFERTA_DE_COMPRA    |                     13 |
|  15 | PRECO_MELHOR_OFERTA_DE_VENDAS    |                     13 |
|  16 | NUMERO_DE_NEGOCIOS               |                      5 |
|  17 | QUANTIDADE_NEGOCIADA             |                     18 |
|  18 | VOLUME_TOTAL_NEGOCIADO           |                     18 |
|  19 | PRECO_DE_EXERCICIO               |                     13 |
|  20 | INDICADOR_DE_CORRECAO_DE_PRECOS  |                      1 |
|  21 | DATA_DE_VENCIMENTO               |                      8 |
|  22 | FATOR_DE_COTACAO                 |                      7 |
|  23 | PRECO_DE_EXERCICIO_EM_PONTOS     |                     13 |
|  24 | CODIGO_ISIN                      |                     12 |
|  25 | NUMERO_DE_DISTRIBUICAO           |                      3 |

### Tipos de mercado

|     | TIPO DE MERCADO                  |
| --: | :------------------------------- |
|  10 | VISTA                            |
|  12 | EXERCICIO DE OPCOES DE COMPRA    |
|  13 | EXERCÍCIO DE OPCOES DE VENDA     |
|  17 | LEILAO                           |
|  20 | FRACIONARIO                      |
|  30 | TERMO                            |
|  50 | FUTURO_COM_RETENCAO_DE_GANHO     |
|  60 | FUTURO_COM_MOVIMENTACAO_CONTINUA |
|  70 | OPCOES_DE_COMPRA                 |
|  80 | OPCOES_DE_VENDA                  |

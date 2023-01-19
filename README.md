# b3fileparser

A função dessa biblioteca é fazer o parser do arquivo com cotações históricas da B3, disponíveis em https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/

## Instalação

Instalação pode ser feita via pip
```
pip install b3fileparser
```
## Exemplo
```python
from b3fileparser import b3parser


dados_b3 = b3parser.read_b3_file('COTAHIST_A2023.TXT')
dados_b3
```
`dados_b3` é um DataFrame pandas:

|    |   TIPO_DE_REGISTRO | DATA_DO_PREGAO      | CODIGO_BDI          | CODIGO_DE_NEGOCIACAO   | TIPO_DE_MERCADO   | NOME_DA_EMPRESA   | ESPECIFICACAO_DO_PAPEL   |   PRAZO_EM_DIAS_DO_MERCADO_A_TERMO | MOEDA_DE_REFERENCIA   |   PRECO_DE_ABERTURA |   PRECO_MAXIMO |   PRECO_MINIMO |   PRECO_MEDIO |   PRECO_ULTIMO_NEGOCIO |   PRECO_MELHOR_OFERTA_DE_COMPRA |   PRECO_MELHOR_OFERTA_DE_VENDAS |   NUMERO_DE_NEGOCIOS |   QUANTIDADE_NEGOCIADA |   VOLUME_TOTAL_NEGOCIADO |   PRECO_DE_EXERCICIO |   INDICADOR_DE_CORRECAO_DE_PRECOS | DATA_DE_VENCIMENTO   |   FATOR_DE_COTACAO |   PRECO_DE_EXERCICIO_EM_PONTOS | CODIGO_ISIN   |   NUMERO_DE_DISTRIBUICAO |
|---:|-------------------:|:--------------------|:--------------------|:-----------------------|:------------------|:------------------|:-------------------------|-----------------------------------:|:----------------------|--------------------:|---------------:|---------------:|--------------:|-----------------------:|--------------------------------:|--------------------------------:|---------------------:|-----------------------:|-------------------------:|---------------------:|----------------------------------:|:---------------------|-------------------:|-------------------------------:|:--------------|-------------------------:|
|  1 |                  1 | 2023-01-02 00:00:00 | 34                  | MMMC34                 | VISTA             | 3M                | DRN                      |                                 -1 | R$                    |              165.56 |         165.56 |         159.06 |        160.97 |                 161.44 |                          161.44 |                          161.59 |                   31 |           120          |          20443.2         |                    0 |                                 0 | NaT                  |                  1 |                              0 | BRMMMCBDR000  |                      143 |
|  2 |                  1 | 2023-01-02 00:00:00 | LOTE_PADRAO         | RRRP3                  | VISTA             | 3R PETROLEUM      | ON      NM               |                                 -1 | R$                    |               37.24 |          37.93 |          35.97 |         36.64 |                  36.41 |                           36.4  |                           36.41 |                13731 |             2.8788e+06 |              1.05483e+08 |                    0 |                                 0 | NaT                  |                  1 |                              0 | BRRRRPACNOR5  |                      100 |
|  3 |                  1 | 2023-01-02 00:00:00 | MERCADO FRACIONARIO | RRRP3F                 | FRACIONARIO       | 3R PETROLEUM      | ON      NM               |                                 -1 | R$                    |               37.75 |          37.91 |          35.98 |         36.69 |                  36.94 |                           36.94 |                           37    |                 1309 |         24010          |         881003           |                    0 |                                 0 | NaT                  |                  1 |                              0 | BRRRRPACNOR5  |                      100 |
|  4 |                  1 | 2023-01-02 00:00:00 | LOTE_PADRAO         | TTEN3                  | VISTA             | 3TENTOS           | ON      NM               |                                 -1 | R$                    |                9.65 |           9.65 |           9.07 |          9.23 |                   9.36 |                            9.35 |                            9.36 |                 3292 |        701700          |              6.48253e+06 |                    0 |                                 0 | NaT                  |                  1 |                              0 | BRTTENACNOR0  |                      101 |
|  5 |                  1 | 2023-01-02 00:00:00 | MERCADO FRACIONARIO | TTEN3F                 | FRACIONARIO       | 3TENTOS           | ON      NM               |                                 -1 | R$                    |                9.34 |           9.44 |           9.08 |          9.26 |                   9.2  |                            9.2  |                            9.65 |                  238 |          4640          |          43069.7         |                    0 |                                 0 | NaT                  |                  1 |                              0 | BRTTENACNOR0  |                      101 |

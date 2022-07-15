# CXK
Aplicação Python3 que simula um simples caixa eletronico. Atraves de contas utilizando CPF como identificação, recebe saques, depósitos e exibe extrato das movimentações da conta.

Só é possivel executar em sistemas operacionais Linux e é necessario Python3 (versão >=3.5).

## Executar localmente:
1.No diretorio raiz executar via terminal o arquivo "main" (./main).
2.Seguir as orientações que a aplicação exibe ao ser executada.

## Detalhes tecnicos:
- Utiliza mmodulos basico de Python ("sys","time","json","datetime" e "pathlib").
- Os dados são armazenados em um arquivo .db (criado automaticamente pela aplicação após a execução) no formato JSON.
- Os arquivos funcoes.py e db.py são classes que contem metodos para gerenciamento das funções da aplicação (saque,deposito e extrato) e gerenciamento do banco de dados, respectivamente.

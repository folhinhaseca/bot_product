# 🛒 Automação de Cadastro de Produtos

Este projeto utiliza **Python** com a biblioteca **PyAutoGUI** para automatizar o processo de cadastro de produtos em um sistema web.

## 📋 Descrição

O script realiza as seguintes etapas:

1. Abre o navegador Google Chrome.
2. Acessa a página de login do sistema.
3. Realiza o login com e-mail e senha.
4. Lê uma planilha `produtos.csv` contendo os dados dos produtos.
5. Preenche automaticamente os campos do formulário com as informações da planilha.
6. Envia o cadastro de cada produto.

## 📂 Estrutura dos Dados

O arquivo `produtos.csv` deve conter as seguintes colunas:

- `codigo`: Código do produto
- `marca`: Marca do produto
- `tipo`: Tipo do produto
- `categoria`: Categoria do produto
- `preco_unitario`: Preço unitário
- `custo`: Custo do produto
- `obs`: Observações (opcional)

## 🧰 Tecnologias utilizadas

- Python 3.x
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- Pandas

## ⚠️ Requisitos

- A resolução de tela usada nos cliques deve ser a mesma usada no momento da automação.
- O navegador deve estar instalado e acessível via menu iniciar.
- O site e elementos clicáveis precisam estar no mesmo local na tela, ou será necessário ajustar as coordenadas dos cliques.

## 🚀 Executando o script

1. Instale as dependências:

```bash
pip install pyautogui pandas

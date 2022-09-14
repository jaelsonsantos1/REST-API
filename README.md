<div align="center">
  <h1>API REST</h1>
</div>

<br>
<p align="center">
   <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/>
</p>


## Descrição do projeto
<div>
    <p>
        Este projeto consiste em uma <strong>API REST</strong> simples, com CRUD completo. Desenvolvida totalmente em Python com Flask e com banco de dados MySQL.
    </p>
    <p>
        A API te permite cadastrar novos dados, atualizar registros, deletar dados, mostrar todos os registros cadastrados e buscar somente registros especificos do banco.
    </p>
</div>

<br>
<br>

## ⚡ Funcionalidades da API

- `Selecionar os dados`: Na rota <strong>"/usuarios"</strong> com método (GET) é retorna um json com todos os dados cadastrados na API;

- `Selecionar um registro`: Para selecionarmos um registro cadastrado na API basta na rota <strong>"/usuario/&lt;id&gt;</strong> fazermos uma requisição do tipo (GET) passando um ID;

- `Cadastrar`: Para Cadastro de dados na API é necessário fazer uma requisição com método (POST) para a rota <strong>"/usuarios"</strong>, passando os dados em um form-data; 

- `Atualizar`: Na rota <strong>"/usuario/&lt;id&gt;"</strong> fazemos uma requisição com método (PUT) passando o ID do registro que queremos atualizar; 

- `Deletar`: Na rota <strong>"/usuario/&lt;id&gt;"</strong> fazemos uma requisição com método (DELETE) passando o ID do registro que queremos deletar.

<br>

## 🔰 Iniciando

Para executar o projeto, será necessário instalar os seguintes programas:

- [Python 3: Necessário para executar o projeto Python](https://www.python.org/downloads/)
- [Visual Studio Code: Para desenvolvimento do projeto](https://code.visualstudio.com/)

<br>

## 🧩 Desenvolvimento

Antes de iniciar o desenvolvimento, será necessário clonar este projeto do GitHub em um diretório de sua preferência em sua máquina:

```shell
cd "diretório de sua preferencia"
git clone https://github.com/jaelsonsantos1/REST-API
```

<br>

### 🛠️ Construção

É preciso instalar as dependências necessárias do framework para funcionamento do projeto, para isso basta executar o comando abaixo:

```shell
cd "diretorio do projeto"
pip install -r requirements.txt
``` 

O comando acima irá baixar todas as dependências do projeto, que incluem o framework Flask e o Flask-SqlAlchemy do Python.

<br>

## 🚀 Features

Este projeto pode ser reaproveitado e aprimorado a medida que atenda a necessidade. A principio esta API foi desenvolvida com fins didáticos. Este projeto monstra de forma prática como é realizado o gerenciamento de uma API e como acontece cada etapa do CRUD com o banco de dados.

<br>

## ⚙️ Configuração

Para execução do projeto, é desejavél utilizar o Visual Studio Code, para que o mesmo identifique as dependências necessárias para a execução no repositório.

<br>

## 👨🏽‍💻 Testes

Para testas a API, no termial do Visual Studio Code execulte o comando abaixo:

```
python app.py
```

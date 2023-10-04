# Desafio: API de produtos
O desafio consiste na criação de uma API RESTful para o gerenciamento do cadastro de produtos.

## Rodando o projeto
Após clonar este repositório em sua máquina, instale as bibliotecas necessárias.
Necessário ter o [python3](https://www.python.org/downloads/) e o [pip](https://pip.pypa.io/en/stable/installation/) já insladados.

### Criar máquina virtual (opcional)
Usando virtualenv (Linux/macOS)
```
python3 -m venv venv
```
Ativar o ambiente virtual
```
source venv/bin/activate
```

## Instalar bibliotecas necessárias para o projeto
```
pip install -r requirements.txt
```

### Criar as tabelas do banco de dados
Para este projeto está sendo usado SQLite3, e para criar suas tabelas basta rodar este comando na raíz do projeto.
```
python manage.py migrate products 
```

O programa já está pronto! Agora basta inicializar o runserver e ser feliz :)
```
python manage.py runserver
```

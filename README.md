# a1a-car-wash

Para instalar as dependências:

```
pip install -r requirements.txt
```

Para conectar ao banco de dados:

```python
# Exportar endereço do banco em variável de ambiente "A1A_DATABASE"
# ex.: "sqlite:///nome_do_banco.db"

class Config:
    ...
    SQLALCHEMY_DB_URI = os.environ.get('A1A_DATABASE')
    ...
```

Executar migrações de banco:

```
python -m package database
```

Executar o projeto:

```
python -m package app
```

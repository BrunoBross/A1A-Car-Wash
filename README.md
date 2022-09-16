# a1a-car-wash

Para instalar as dependências:

```
pip install -r requirements.txt
```

Para conectar ao banco de dados:

```python
# Após subir serviço de banco SQLite/Postgres/etc..
# Editar em package/Config.py

class Config:
    ...
    SQLALCHEMY_DB_URI = "uri do banco/port/whatever..."
    ...
```

Executar migrações de banco:

```
python -m package --migrate
```

Executar o projeto:

```
python -m package
```

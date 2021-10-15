### Criar um ambiente virtual chamado env
```bash
$ python3.8 -m venv env
```

### Ativando o ambiente virtual
```bash
$ source env/bin/activate
```


### Instalar as dependências no ambiente virtual
```bash
$ pip install -r src/requirements.txt
```

### Desativar um ambiente virtual
```bash
$ deactivate
```

## Principais comandos do CLI do Django

#### Listar todos os comandos do CLI
```bash
$ python manage.py help
```

#### Rodar o server

```bash
# Esse comando só irá funcionar dentro do container
$ python manage.py runserver 0.0.0.0:8000
```

#### Rodar as migrações
```bash
$ python manage.py migrate
```

#### Criar uma nova migração
```bash
$ python manage.py makemigrations
```

#### Entrar no Shell do Django
```bash
# Comando útil para debugar código manualmente
$ python manage.py shell
```

#### Rodar os testes
```bash
$ python manage.py test
```

#### Criar um novo App
```bash
$ python manage.py startapp <NOME>
```

#### Criar um superusuário
```bash
# As credênciais usadas servem para acessar o dashboard administrativo do django na rota
# localhost:8000/admin
$ python manage.py createsuperuser
```

# Parking Control

Trata-se de uma api REST bem simples para o controle de entrada e saída de veículos em suas vagas de estacionamento. Esse é um projeto foi desenvolvido em Python com Django e foi baseado no mesmo contexto do projeto desenvolvido pela Michele Brito no seu [curso sobre Spring Boot](https://www.youtube.com/watch?v=LXRU-Z36GEU).

## Decisões arquiteturais

### Django Rest Framework

Para o desenvolvimento desse projeto foi escolhido o framework Python Django Rest Framework. A escolha desse framework deu-se devido aos seguintes pontos:

1. *Maturidade do framework e comunidade*: trata-se de um framework maduro já que existe desde 2005 e com uma grande comunidade para suporte. O pacote Rest acrescenta várias facilidades para o desenvolvimento de apis Rest e RetFull.
2. *Redução do esforço e do tempo de desenvolvimento*: Django tem uma abordagem *batteries included* permitindo que aos desenvolvedores focar no problema que deve ser resolvido e em outros aspectos não funcionais tais como *containerização* da aplicação.
3. *ORM embarcado e possíbilidade de utilizar vários bancos relacinais*: A existência de um ORM embarcado no framework foi também uma grande facilidade junto com a exitência de conexão nativa com os bancos PostgreSQL, MySQL, SQLLite e Oracle, também embarcados e nativos.
4. *Multiplataforma*: por ser desenvolvido em python permite a execução tanto em ambiente Windows quanto Linux.
5. *Segurança*: o Django já possui uma ferramente para gestão de usuários e autenticação.

### Banco de dados SQLLite

A escolha do banco de dados foi o SQLLite3, e deu-se pelas seguintes razões:

1. *Autocontido*: trata-se de um banco de dados auto contido, sem a necessidade de um servidor, reduzindo assim a dependência externa e simplificando a configuração da aplicação.
2. *Portabilidade*: os daddos são salvos em um único arquivo o que permite salvá-lo em um *data lake* ou *file share* com facilidde em um ambiente de nuvem ou *on-premisse*.
3. *Baixa quantidade de acessos simultâneos*: espera-se que a aplicação tenha um acesso muito baixo de usuários concorrentes, não sendo justificado nesse momento utilizar um banco de dados mais robusto.


## Execução do projeto

### Execução em ambiente local

#### Pré-requisitos

- Python 3.10.12 instalado na máquina

#### Execução

1. Copiar o arquivo **.assets/.env** para o diretório **src**.

2. No diretório **src** do projeto executar os comandos abaixo:

``` Shell
# Aplicar os migrations
python manage.py migrate

# Seguir o passo-a-passo para criar um usuário para a aplicação
python manage.py createsuperuser

# Seguir o passo-a-passo para criar um usuário para a aplicação
python manage.py runserver
```

3. No browser de sua preferência acessar a url <http://localhost:8000/swagger>, uma tela semelhante a abaixo deve ser apresentadada.

    ![Tela do Swagger](/.assets/swagger.png "Tela do Swagger")

4. Para as ações de consulta (GET) basta acessar a opção e selecionar a opção "Try it out"

    ![Tela do Swagger com Try Out](/.assets/TryOut.png "Tela do Swagger com Try Out")

5. Para as ações de alteração (POST, PUT, PATCH e DELETE) é preciso autenticar. Execute os passos:

    5.1 Clique no bota Authorize

    ![Tela do Swagger com Authorize](/.assets/Auth.png "Tela do Swagger com Authorize")

    5.2 Informe o usuário e senha gerado no passo 1 na tela abaixo apresentada e clique em close

    ![Tela do Swagger com Login](/.assets/swagger-login.png "Tela do Swagger com Login")

    5.3 Clique na opção Try out do *endpoint* desejado.

    ![Tela do Swagger com Try Out](/.assets/TryOut.png "Tela do Swagger com Try Out")

### Execução no Docker

#### Pré-requisitos

- Ter o Docker instalado na máquina

#### Execução

1. No diretório raiz do projeto executar o comando abaixo:

``` Shell
docker-compose up -d --build
```

2. No browser de sua preferência acessar a url <http://localhost:8000/swagger>, uma tela semelhante a abaixo deve ser apresentadada.

    ![Tela do Swagger](/.assets/swagger.png "Tela do Swagger").

3. Para as ações de consulta (GET) basta acessar a opção e selecionar a opção "Try it out"

    ![Tela do Swagger com Try Out](/.assets/TryOut.png "Tela do Swagger com Try Out").

4. Para as ações de alteração (POST, PUT, PATCH e DELETE) é preciso autenticar. Execute os passos:

    4.1 Clique no bota Authorize

    ![Tela do Swagger com Authorize](/.assets/Auth.png "Tela do Swagger com Authorize").

    4.2 Informe o usuário *admin* e senha *password123* na tela abaixo apresentada e clique em close

    ![Tela do Swagger com Login](/.assets/swagger-login.png "Tela do Swagger com Login").

    4.3 Clique na opção Try out do *endpoint* desejado.

    ![Tela do Swagger com Try Out](/.assets/TryOut.png "Tela do Swagger com Try Out").


**Observação**: ao terminar a execução é preciso executar o comando abaixo para finalizar a aplicação, também a partir da raiz do projeto.

``` Shell
docker-compose down
# Um volume foi criado para o banco de dados para excluí-lo utilizar o comando
docker volume rm parking-control-python_data
```

## Referências

BRITO, Michele. **Spring Boot Curso Completo 2022**. Disponível em: <https://www.youtube.com/watch?v=LXRU-Z36GEU>. Acesso em: 13-08-2023

__. **Django REST Framework Documentation**. Disponível em: <https://www.django-rest-framework.org/tutorial/quickstart/>. Acesso em: 13-08-2023

__. **Django Documentation**. Disponível em: <https://docs.djangoproject.com/en/4.2/>. Acesso em: 13-08-2023

KHATRI, Vijay S. e JOHNS, Robert. **Flask vs Django: Which Python Web Framework to Use in 2023?**. Disponível em: <https://hackr.io/blog/flask-vs-django>. Acesso em: 13-08-2023

DIGITALOCEAN. **SQLite vs MySQL vs PostgreSQL: A Comparison Of Relational Database Management Systems**. Disponível em: <https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems>. Acesso em: 13-08-2023

 SOUZA, Ivan. **O que é SQLite, por que ele é usado, e o que o diferencia do MySQL?**. Disponível em: <https://rockcontent.com/br/blog/sqlite/>. Acesso em: 13-08-2023
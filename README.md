# Parking Control

Trata-se de uma api REST bem simples para o controle de entrada e saída de veículos em suas vagas de estacionamento. Esse é um projeto foi desenvolvido em Python com Django e foi baseado no mesmo contexto do projeto desenvolvido pela Michele Brito no seu [curso sobre Spring Boot](https://www.youtube.com/watch?v=LXRU-Z36GEU).

## Solução

## Contexto

## Containers

## Componentes

## Decisões arquiteturais

### 1. Django Rest Framework

Para o desenvolvimento desse projeto foi escolhido o framework Python Django Rest Framework. A escolha desse framework deu-se devido aos seguintes pontos:

1. *Maturidade do framework e comunidade*: trata-se de um framework maduro já que existe desde 2005 e com uma grande comunidade para suporte. O pacote Rest acrescenta várias facilidades para o desenvolvimento de apis Rest e RetFull.
2. *Redução do esforço e do tempo de desenvolvimento*: Django tem uma abordagem *batteries included* permitindo que aos desenvolvedores focar no problema que deve ser resolvido e em outros aspectos não funcionais tais como *containerização* da aplicação.
3. *ORM embarcado e possíbilidade de utilizar vários bancos relacinais*: A existência de um ORM embarcado no framework foi também uma grande facilidade junto com a exitência de conexão nativa com os bancos PostgreSQL, MySQL, SQLLite e Oracle, também embarcados e nativos.
3. *Multiplataforma*: por ser desenvolvido em python permite a execução tanto em ambiente Windows quanto Linux.

### 2. Banco de dados SQLLite

A escolha do banco de dados foi o SQLLite3, e deu-se pelas seguintes razões:

1. *Autocontido*: trata-se de um banco de dados auto contido, sem a necessidade de um servidor, reduzindo assim a dependência externa e simplificando a configuração da aplicação.
2. *Portabilidade*: os daddos são salvos em um único arquivo o que permite salvá-lo em um *data lake* ou *file share* com facilidde em um ambiente de nuvem ou *on-premisse*.
3. *Baixa quantidade de acessos simultâneos*: espera-se que a aplicação tenha um acesso muito baixo de usuários concorrentes, não sendo justificado nesse momento utilizar um banco de dados mais robusto.


## Referências

BRITO, Michele. **Spring Boot Curso Completo 2022**. Disponível em: <https://www.youtube.com/watch?v=LXRU-Z36GEU>. Acesso em: 13-08-2023

__. **Django REST Framework Documentation**. Disponível em: <https://www.django-rest-framework.org/tutorial/quickstart/>. Acesso em: 13-08-2023

__. **Django Documentation**. Disponível em: <https://docs.djangoproject.com/en/4.2/>. Acesso em: 13-08-2023

KHATRI, Vijay S. e JOHNS, Robert. **Flask vs Django: Which Python Web Framework to Use in 2023?**. Disponível em: <https://hackr.io/blog/flask-vs-django>. Acesso em: 13-08-2023

DIGITALOCEAN. **SQLite vs MySQL vs PostgreSQL: A Comparison Of Relational Database Management Systems**. Disponível em: <https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems>. Acesso em: 13-08-2023

 SOUZA, Ivan. **O que é SQLite, por que ele é usado, e o que o diferencia do MySQL?**. Disponível em: <https://rockcontent.com/br/blog/sqlite/>. Acesso em: 13-08-2023
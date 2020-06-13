# Projeto Docker Django

##### Definir estrutura do projeto

Para este projeto, você precisa criar um Dockerfile, um arquivo de dependências do Python e um docker-compose.yml arquivo. (Você pode usar uma extensão .yml ou .yaml para este arquivo.)

1. Crie um diretório de projeto vazio.

    Você pode nomear o diretório como algo fácil de lembrar. Este diretório é o contexto para a sua imagem do aplicativo. O diretório deve conter apenas recursos para criar essa imagem.

2. Crie um novo arquivo chamado Dockerfile no diretório do projeto.

3. Adicione o seguinte conteúdo ao Dockerfile.

FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

##### Backup e restauração do banco de dados Postgresql em execução no docker

1. Para fazer backup, usamos a pg_dump ferramenta:
 
    - Para fazer backup, usamos a _**pg_dump**_ ferramenta:
    
        $ docker exec <postgres_container_name> pg_dump -U postgres <database_name> > backup.sql
   
2. Isso criaria um arquivo de texto chamado backup.sqlcontendo todos os dados e esquema do seu banco de dados. Você pode importar esses dados novamente para o postgres usando a psqlferramenta:

    - Para importar o arquivo _**backup.sql**_
    
        $ docker exec -i <postgres_container_name> psql -U postgres -d <database_name> < backup.sql
   
        O **-i** sinalizador é de particular importância aqui, porque a psql ferramenta precisa ser executada interativamente para poder ler o backup.sql arquivo.
       
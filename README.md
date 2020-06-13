# Projeto Docker Django

##### Definir estrutura do projeto

Para este projeto, você precisa criar um Dockerfile, um arquivo de dependências do Python e um docker-compose.yml arquivo. (Você pode usar uma extensão .yml ou .yaml para este arquivo.)

1. Crie um diretório de projeto vazio.

    Você pode nomear o diretório como algo fácil de lembrar. Este diretório é o contexto para a sua imagem do aplicativo. O diretório deve conter apenas recursos para criar essa imagem.

2. Crie um novo arquivo chamado Dockerfile no diretório do projeto e salve com o seguinte conteudo.

        FROM python:3
        ENV PYTHONUNBUFFERED 1
        RUN mkdir /code
        WORKDIR /code
        COPY requirements.txt /code/
        RUN pip install -r requirements.txt
        COPY . /code/
    
3. Crie um arquivo requirements.txt no do projeto e salve com o seguinte conteudo.

        Django>=2.0,<3.0
        psycopg2>=2.7,<3.0

4. Crie um arquivo chamado docker-compose.yml no diretório do projeto. No projeto em questão salvei com a exteção _**.yaml**_.

    O docker-compose.ymlarquivo descreve os serviços que compõem seu aplicativo. Neste exemplo, esses serviços são um servidor da web e banco de dados. O arquivo de composição também descreve quais imagens do Docker esses serviços usam, como eles se vinculam, quaisquer volumes que possam precisar ser montados dentro dos contêineres. Por fim, o docker-compose.ymlarquivo descreve quais portas esses serviços expõem.
    
    Adicione a seguinte configuração ao arquivo.
    
        version: '3'
    
        services:
            db:
              image: postgres
              environment:
                - POSTGRES_DB=postgres
                - POSTGRES_USER=postgres
                - POSTGRES_PASSWORD=postgres
            web:
              build: .
              command: python manage.py runserver 0.0.0.0:8000
              volumes:
                - .:/code
               ports:
                - "8000:8000"
               depends_on:
                - db
    
    Este arquivo define dois serviços: O db serviço e o webserviço. Salve e feche!
    
##### Criando o projeto Django


   Nesta etapa, você cria um projeto inicial do Django construindo a imagem a partir do contexto de construção definido no procedimento anterior.
    
1. Mude para a raiz do diretório do seu projeto.

2. Crie o projeto Django executando o comando docker-compose run da seguinte maneira.

        sudo docker-compose run web django-admin startproject <nome-do-projeto> .

##### Backup e restauração do banco de dados Postgresql em execução no docker

1. Para fazer backup, usamos a pg_dump ferramenta:
 
    - Para fazer backup, usamos a _**pg_dump**_ ferramenta:
    
        $ docker exec <postgres_container_name> pg_dump -U postgres <database_name> > backup.sql
   
2. Isso criaria um arquivo de texto chamado backup.sqlcontendo todos os dados e esquema do seu banco de dados. Você pode importar esses dados novamente para o postgres usando a psqlferramenta:

    - Para importar o arquivo _**backup.sql**_
    
        $ docker exec -i <postgres_container_name> psql -U postgres -d <database_name> < backup.sql
   
        O **-i** sinalizador é de particular importância aqui, porque a psql ferramenta precisa ser executada interativamente para poder ler o backup.sql arquivo.
       
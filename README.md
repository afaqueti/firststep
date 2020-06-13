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

        sudo docker-compose run web django-admin startproject composeexemplo .

    Isso instrui o Compose a executar _**django-admin startproject composeexample**_ em um contêiner, usando a web imagem e a configuração do serviço. Como a web imagem ainda não existe, o Compose a cria a partir do diretório atual, conforme especificado pela build: . linha em docker-compose.yaml.

    Depois que a web imagem de serviço é criada, o Compose a executa e executa o django-admin startproject comando no contêiner. Este comando instrui o Django a criar um conjunto de arquivos e diretórios representando um projeto do Django.

3. Após a conclusão do docker-compose.yaml, liste o conteúdo do seu projeto.

        $ ls -l
        drwxr-xr-x 2 root   root   composeexample
        -rw-rw-r-- 1 user   user   docker-compose.yml
        -rw-rw-r-- 1 user   user   Dockerfile
        -rwxr-xr-x 1 root   root   manage.py
        -rw-rw-r-- 1 user   user   requirements.txt

    Se você estiver executando o Docker no Linux, os arquivos django-admincriados pertencerão à raiz. Isso acontece porque o contêiner é executado como usuário root. Altere a propriedade dos novos arquivos.
    
        sudo chown -R $USER:$USER .
    Se você estiver executando o Docker no Mac ou Windows, já deve ter a propriedade de todos os arquivos, incluindo os gerados por django-admin. Liste os arquivos apenas para verificar isso.
    
        $ ls -l
        total 32
        -rw-r--r--  1 user  staff  145 Feb 13 23:00 Dockerfile
        drwxr-xr-x  6 user  staff  204 Feb 13 23:07 composeexample
        -rw-r--r--  1 user  staff  159 Feb 13 23:02 docker-compose.yml
        -rwxr-xr-x  1 user  staff  257 Feb 13 23:07 manage.py
        -rw-r--r--  1 user  staff   16 Feb 13 23:01 requirements.txt
        
##### Conecte o banco de dados

   Nesta seção, você configura a conexão com o banco de dados para o Django.
   
1. No diretório do seu projeto, edite o composeexample/settings.pyarquivo.

2. Substitua DATABASES = ...por:

        # setting.py
   
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'postgres',
                'USER': 'postgres',
                'PASSWORD': 'postgres',
                'HOST': 'db',
                'PORT': 5432,
            }
        }
        
    Essas configurações são determinadas pela imagem do postgres Docker especificada em docker-compose.yml. Salve e feche o arquivo setting.py.

3. Execute o comando **_docker-compose up_** no diretório raiz do seu projeto.

        $ ls -l
        total 32
        -rw-r--r--  1 user  staff  145 Feb 13 23:00 Dockerfile
        drwxr-xr-x  6 user  staff  204 Feb 13 23:07 composeexample
        -rw-r--r--  1 user  staff  159 Feb 13 23:02 docker-compose.yml
        -rwxr-xr-x  1 user  staff  257 Feb 13 23:07 manage.py
        -rw-r--r--  1 user  staff   16 Feb 13 23:01 requirements.txt

    Esse será o retorno do comando, informado que a porta está pronta para acessar o endereço "web_1  | Starting development server at http://0.0.0.0:8000/".
    
        $ docker-compose up
        djangosample_db_1 is up-to-date
        Creating djangosample_web_1 ...
        Creating djangosample_web_1 ... done
        Attaching to djangosample_db_1, djangosample_web_1
        db_1   | The files belonging to this database system will be owned by user "postgres".
        db_1   | This user must also own the server process.
        db_1   |
        db_1   | The database cluster will be initialized with locale "en_US.utf8".
        db_1   | The default database encoding has accordingly been set to "UTF8".
        db_1   | The default text search configuration will be set to "english".
        
        . . .

        web_1  | May 30, 2017 - 21:44:49
        web_1  | Django version 1.11.1, using settings 'composeexample.settings'
        web_1  | Starting development server at http://0.0.0.0:8000/
        web_1  | Quit the server with CONTROL-C.

    Nesse ponto, seu aplicativo Django deve estar em execução na porta 8000no host do Docker.
    
    
##### Backup e restauração do banco de dados Postgresql em execução no docker

1. Para fazer backup, usamos a pg_dump ferramenta:
 
    - Para fazer backup, usamos a _**pg_dump**_ ferramenta:
    
        $ docker exec <postgres_container_name> pg_dump -U postgres <database_name> > backup.sql
   
2. Isso criaria um arquivo de texto chamado backup.sqlcontendo todos os dados e esquema do seu banco de dados. Você pode importar esses dados novamente para o postgres usando a psqlferramenta:

    - Para importar o arquivo _**backup.sql**_
    
        $ docker exec -i <postgres_container_name> psql -U postgres -d <database_name> < backup.sql
   
        O **-i** sinalizador é de particular importância aqui, porque a psql ferramenta precisa ser executada interativamente para poder ler o backup.sql arquivo.
       
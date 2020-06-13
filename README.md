# Projeto Docker Django

##### Backup e restauração do banco de dados Postgresql em execução no docker

1. Para fazer backup, usamos a pg_dump ferramenta:
 
    - Para fazer backup, usamos a _**pg_dump**_ ferramenta:
    
        $ docker exec <postgres_container_name> pg_dump -U postgres <database_name> > backup.sql
   
2. Isso criaria um arquivo de texto chamado backup.sqlcontendo todos os dados e esquema do seu banco de dados. Você pode importar esses dados novamente para o postgres usando a psqlferramenta:

    - Para importar o arquivo _**backup.sql**_
    
        $ docker exec -i <postgres_container_name> psql -U postgres -d <database_name> < backup.sql
   
        O **-i** sinalizador é de particular importância aqui, porque a psql ferramenta precisa ser executada interativamente para poder ler o backup.sqlarquivo.
       
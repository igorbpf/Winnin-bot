# Winnin-bot

Este projeto é resultado da primeira etapa do processo seletivo da empresa Winnin para vaga de Cientista de Dados. O projeto
consistiu em criar uma crawler que armazena, diariamente, os posts "hot" do subreddit Artifical. A tecnologia usada foi python 3.6, 
django e django rest framework.

Para utilização deste projeto, é preciso clonar este repositorio e instalar as dependencias presentes em requirements.txt. Além 
disso, é preciso criar um arquivo .env (não esqueça do 'ponto' na frente) no root do projeto. Este arquivo contém algumas variáveis 
de ambiente do sistema.

Exemplo arquivo .env:

SECRET_KEY=rqr_cjv4igscjbfvhy&(0ce(=sy=f2)p=f_wnjdhrb0xsp7m$@!kp=d

DEBUG=True

ALLOWED_HOSTS=.localhost,127.0.0.1

DATABASE_URL=sqlite:///db.sqlite3

BROKER_URL=redis://localhost:6379

CELERY_RESULT_BACKEND=redis://localhost:6379

CLIENT_ID=<_client-id-reddit_>

CLIENT_SECRET=<_client-secret-do-reddit_>

USERNAME=<_seu-usuario-do-reddit_>

PASSWORD=<_sua-senha-do-reddit_>

MINUTE=<_minuto-de-rodar-o-bot_>

HOUR=<_hora-de-rodar-o-bot_>

Após configurar as variáveis de ambiente é necessário rodar alguns migrações para preparar o banco sql.

Use o comando no diretorio root : `python manage.py migrate`

Além disso, é preciso ter o redis-server instalado e rodando em um outro terminal (certifique-se que a porta é a mesma 
especificada em BROKER_URL e CELERY_RESULT_BACKEND) e mais 2 terminais abertos para executar e agendar o crawler. Use os 
comandos: 

`celery -A winnin_reddit worker -l info`

`celery -A winnin_reddit beat -l info`

# API

**Post**
----
  Retorna posts ordenados pela data de criação.

* **URL**

  /api/v1/hot/post/

* **Método:**

  `GET`
  
*  **URL Query Params**

   **Opcional:**
   `order=[string] valores: ups e num_comments para ordenar os post por ordem decrescente de up votes e num de comentários`
   `start_date=[string] formato da data: YYYY-MM-DD`
   `end_date=[string] formato da data: YYYY-MM-DD`
   
* **Código de Sucesso:**

  * **Código:** 200 <br />
 
* **Exemplo de chamada:**

 `GET` /api/v1/hot/post/?order=ups&start_date=2018-03-27&end_date=2018-04-04


**Author**
----
  Retorna autores ordenados pela data de criação dos posts.

* **URL**

  /api/v1/hot/author/

* **Método:**

  `GET`
  
*  **URL Query Params**

   **Opcional:**
   `order=[string] valores: ups e num_comments para ordenar os post por ordem decrescente de up votes e num de comentários`
   
* **Código de Sucesso:**

  * **Código:** 200 <br />
 
* **Exemplo de chamada:**

 `GET` /api/v1/hot/author/?order=num_comments



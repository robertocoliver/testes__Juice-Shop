Pentester na aplicação Owasp Juice Shop  
# Escopo e objetivo


O OWASP Juice Shop é uma aplicação web intencionalmente vulnerável que foi projetada para ser usada como uma plataforma de treinamento para testes de segurança e para praticar habilidades de exploração de vulnerabilidades.

Ao usar o OWASP Juice Shop,pode-se aprender a identificar e explorar vulnerabilidades comuns em aplicações web, como injeção de SQL, injeção de comandos, cross-site scripting (XSS) e muitas outras.Ao usar uma aplicação vulnerável como o OWASP Juice Shop, os testadores de segurança podem simular cenários reais sem comprometer a segurança de sistemas em produção ou de dados confidenciais. Eles podem aprender e praticar como explorar vulnerabilidades e descobrir maneiras de mitigar e corrigir esses problemas em aplicações web.

Baixe e instale a aplicação Juice Shop
```bash
  https://github.com/juice-shop/juice-shop
```

## Reconhecimento web 
Reconhecimento web é uma das etapas importantes em um teste de intrusão (pentester). Nela, é enumrado os diretórios, subdomínios, e-mails que a aplicação possui (priorizando os e-mails administrativos), tecnologias utilizadas no desenvolvimento do site, fingerprint do sistema operacional, análise do /robots.txt, /sitemap.xml, paineis administrativos de login, google dorks, entre outras ténicas e ferramentas que podem ser utilizadas.

![screenshot](https://user-images.githubusercontent.com/102238044/235038359-38451dfe-f741-4827-a90c-e35ee66c8ba2.jpg)
Observando o comportamento da página, uma solicitação não é processada pelo servidor em uma nova rota. Ao invés disso, as rotas são gerenciadas dinamicamente no lado do cliente. Em outras palavras, uma solicitação não faz a página recarregar para outra URL.
## Dica
wappalyzer -> É uma extensão que ajuda a detectar as tecnologias utilizadas no front-end de uma aplicação como frameworks de front-end, bibliotecas JavaScript, entre outras.
Usar as ferramentas do desenvolvedor no navegador e analisar se as diretivas ng-content e ng-host estão presentes. Normalmente, elas estão associadas a um SPA (Single Page Application)
![screenshot](https://user-images.githubusercontent.com/102238044/235047454-0c1c56b0-53db-4a0a-8a17-845e24ae1863.jpg)

## Encontrando rotas em uma SPA 
Como as rotas são gerenciadas no lado do cliente, as rotas podem ser visualizadas nas ferramentas "debbuger" do navegador. Sabendo através do wappalyzer que se trata de uma aplicação javascript, vamos procurar pelas rotas "path" 

![screenshot](https://user-images.githubusercontent.com/102238044/235059657-9697a6e2-fd3e-4dc7-9dbd-eded4e1e48b6.jpg)

## Enumeração de e-mails 
Ao fazer uma requisição a um item do juice shop, ele faz um quest a API através de um ID que retorna os comentários de usuários. Com essas informações, podemos fazer uma enumeração de e-mails, passando um número de iD diferente
![screenshot](https://user-images.githubusercontent.com/102238044/236518510-d34de849-de28-4137-a7f5-4843867fbbbd.jpg)

Clone o repositório

```bash
  https://github.com/robertocoliver/Pentester_JuiceShop
```
Entre no diretório 
```bash
  cd Pentester_JuiceShop
```
Execute a ferramenta
```bash
  python3 mailenum.py
```
![screenshot](https://user-images.githubusercontent.com/102238044/236518553-a3749402-58ac-42c2-947c-09cdaaa924b8.jpg)

## Brute force 
Na página de login, verificamos se o código de retorno quando uma senha inválida é passada, e se existe algum bloqueio após uma quantidade de tentativas. Caso não exista uma política de bloqueio na parte de login, provavelmente ela é vulnerável a força bruta.

![Captura de tela_2023-05-05_14-08-52](https://user-images.githubusercontent.com/102238044/236523742-413a2d62-ae45-4b00-99eb-01b7ab57adb3.jpg)

Execute a ferramenta

```bash
  python3 brute.py
```
![screenshot](https://user-images.githubusercontent.com/102238044/236518600-028dc9fe-8743-40f1-abb3-75eefa277db5.png)

## CORS (Cross-Origin Resource Sharing)
Outro ponto a ser notado, é a diretiva Access-Control-Allow-Origin: * está ativa, isso faz com que os recursos da API seja acessado por qualquer outro domínio. 

![screenshot](https://user-images.githubusercontent.com/102238044/236557530-ab11fdf4-05d0-46b5-a4c4-9f188aef5480.png)

Interceptando um post de um comentário

![Captura de tela_2023-05-05_17-26-08](https://user-images.githubusercontent.com/102238044/236563217-3940eef1-92da-4ca6-bc21-78b69d6cc68b.jpg)

Alterando o e-mail de um usuário sem privilégios para um admin 

![screenshot](https://user-images.githubusercontent.com/102238044/236563329-f8cd9d8c-f384-4e60-8307-0533ee3edd13.png)

saída:

![Captura de tela_2023-05-05_17-27-47](https://user-images.githubusercontent.com/102238044/236563796-a80db3e5-483e-4e56-955a-e3fe2d15a4d5.png)

##  SQL Injection
Para encontrar vulnerabilidades SQLi ( SQL injection ), é preciso testar campos de entrada de aplicativos da web, campos ocultos em solicitações POST, cabeçalhos HTTP e cookies. O objetivo do teste é identificar quais campos de entrada são vulneráveis a ataques de injeção de SQL, que podem permitir que um invasor execute comandos maliciosos no banco de dados do aplicativo.

Abaixo, vamos testar a página de login do juice shop, um email conhecido ( admin ou usuário ) é passado com uma aspas simples ou dupla.

![screenshot](https://user-images.githubusercontent.com/102238044/236584453-c67c256d-405c-481c-9212-eb0960ec2a2a.png)

A requisição feita no banco de dados gera um erro de sintaxe, isso acontece porque não foi fechado as aspas. Em seguida, o site nos informa que ocorreu um erro, e retorna o banco de dados utilizado e como é feita a query. 

```bash
  SELECT * FROM Users WHERE email = 'admin@juice-shp.op'' AND password = '202cb962ac59075b964b07152d234b70'
```
O próximo passo de um atacante após interromper a query, é fazer com que o restante da consulta seja tratado como um comentário usando --. Dessa maneira, apenas o email é validado. 
![screenshot](https://user-images.githubusercontent.com/102238044/236584458-7f841512-c916-4d23-a641-d0f1cf78c0df.png)

No exemplo supracitado, foi utilizado nos parâmetros de login e senha. Entrantando como já mencionado, qualquer entrada de usuário como POST, cabeçalhos HTTP e cookies devem ser levados em consideração para ser tratado e corrigido em uma aplicação web. 


 ## NOSQL Injection 
 
 Diferente dos bancos relacionais que guardam dados em um conjunto de tabelas e colunas, NOSQL que significa "não SQL", guarda as informações em estrututuras diferentes e fazem a consulta de formas diferentes do SQL. Para saber qual banco de dados uma aplicação utiliza, é preciso analisar como a aplicação guardam os dados. NoSQL usa JSON como formato de armazenamento, porém existem muitas outras opções, como XML, BSON, YAML, entre outras.
  Ao interceptar um post de comentário, temos a seguinte requisição:
 ```bash
  {"status":"success","data":
  {"product":"3","message":"x","author":"teste1@teste.com.br","likesCount":0,"likedBy":[],"_id":"ZgayhEWtBgPFzH68h","liked":true}]}
```
  Se no campo _id que identifica uma conta for diferente de nulo $ne: 0, é retornado todos os _ids. 
```bash
  {"_id":{"$ne": null}},"message":"ISSO É UM NOSQL"}
```
Nesse caso, todos as "message" de todos _ids seriam modificados de uma vez
 
## Cross Site Scripting (XSS)

Na documentação de XSS da OWASP, a metodologia utilizada para descoberta XSS(Cross-Site Scripting) se dá através dos testes de parâmetros de formulário, parâmetros de URL, cookies, cabeçalhos HTTP e entradas de logs e e-mail, vejamos:

payload injetado no parâmetro de pesquisa: 
```bash
  <img src=a onerror="alert(1)">
```
![screenshot](https://user-images.githubusercontent.com/102238044/236903113-a4559fbe-3b10-46f3-9b52-fceb68dd2d0f.jpg)

injetando payload e passando por filtro no post de feedback dos usuários
```bash
  <<img src=a onerror="alert(1)">iframe src="javascript:alert('xss');">
```
![screenshot](https://user-images.githubusercontent.com/102238044/236903439-f5a9bcbe-6089-4c9e-8576-d97d1a61747c.png)
payload executado para todos os usuários que verifiquem o comentário: 
![screenshot1](https://user-images.githubusercontent.com/102238044/236903450-7c80b5f4-3436-4224-b676-b609bf8aa859.png)

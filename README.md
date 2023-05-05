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


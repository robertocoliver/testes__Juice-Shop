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

# Sistema de Gestão de Estoque (SGE)

Bem-vindo ao Sistema de Gestão de Estoque (SGE), um projeto desenvolvido com intuito didático no Curso Django Master ministrado pela PycodeBR, 
em Django e Bootstrap 5 para facilitar o gerenciamento de estoque. Este Projeto possui integração com Inteligência Artificial OpenAI e integração com outro aplicativo em
Django para envio de mensagens via WhatsApp e e-mail.
Este projeto possui os end-points para futuras integrações com aplicativos mobiles e sites.
Este README fornece informações essenciais sobre como configurar e executar o projeto em seu ambiente local.
## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

    Python (versão recomendada: 3.7 ou superior)
    Django (instalado automaticamente ao seguir as instruções abaixo)
    Outras dependências listadas no arquivo requirements.txt

## Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```
pip install -r requirements.txt
```
## Configurar chave OPENAI_KEY e OPENAI_MODEL
Criar na raiz do projeto em app o arquivo .env e colocar dentro as variáveis:
```
OPENAI_MODEL=`modelo_gpt_escolhido` (ex.: gpt-3.5-turbo)
OPENAI_KEY=`sua_chave_aqui`
```
## Rodar o projeto

Após instalar as dependências, aplique as migrations no banco de dados com o comando:
```
python manage.py migrate
```
Agora o projeto jã pode ser inicializado com o comando:
```
python manage.py runserver
```
Após isso, o sistema estará pronto para ser acessado em: http://localhost:8000

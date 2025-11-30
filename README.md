📘 Scraper de Dados com Python

Um projeto simples e eficiente de Web Scraping usando Requests + BeautifulSoup e armazenando os dados em um banco local SQLite.
Ideal para aprender automação, coleta de dados e persistência em banco usando Python.

🚀 Tecnologias Utilizadas

Python 3

Requests — para realizar requisições HTTP

BeautifulSoup (bs4) — para extrair dados da página

SQLite — banco de dados local

VS Code — ambiente de desenvolvimento

📂 Estrutura do Projeto
📁 scraper-projeto
│
├── scraper.py          # Script principal do scraper
├── database.py         # Conexão e inserção no banco SQLite
├── dados.db            # Banco de dados gerado automaticamente
└── README.md           # Documentação do projeto

🕸 Como Funciona o Scraper

Acessa uma página web utilizando requests.get().

Extrai dados usando BeautifulSoup.

Armazena cada item coletado dentro do SQLite.

Permite reuso e expansão para qualquer outro site.

▶ Como Rodar o Projeto
1. Instale os requisitos:
pip install requests beautifulsoup4

2. Execute o scraper:
python scraper.py


O arquivo dados.db será criado automaticamente com as informações coletadas.

🗄 Estrutura do Banco de Dados

Tabela padrão:

CREATE TABLE dados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    link TEXT
);


Cada execução do scraper adiciona novos registros.

🧩 Possíveis Extensões

Você pode evoluir esse projeto adicionando:

Scrapy (framework avançado de scraping)

Armazenamento em PostgreSQL

Dashboard usando Streamlit

Exportação para CSV, Excel ou API REST

💼 Ideal Para Portfólio

Esse projeto demonstra:

✔ domínio de Python
✔ lógica de programação e automação
✔ manipulação de dados reais
✔ persistência em banco de dados
✔ organização de projeto
✔ uso correto de Git e GitHub
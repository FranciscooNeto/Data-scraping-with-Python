from scraper import get_page
from parser import parse_produtos
from db import create_table, inserir_produto

def main():
    print("Criando tabela...")
    create_table()

    url = "http://books.toscrape.com/"
    print("Baixando página...")
    html = get_page(url)

    print("Extraindo informações...")
    produtos = parse_produtos(html)

    print(f"{len(produtos)} produtos encontrados.")

    for p in produtos:
        print(f"Salvando: {p['titulo']} - £{p['preco']}")
        inserir_produto(p["titulo"], p["preco"], p["link"])

    print("Finalizado!")

if __name__ == "__main__":
    main()

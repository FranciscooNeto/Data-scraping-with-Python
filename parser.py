from bs4 import BeautifulSoup

def parse_produtos(html):
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.select("article.product_pod")

    produtos = []
    for card in cards:
        titulo = card.h3.a["title"]
        preco = card.select_one(".price_color").get_text(strip=True).replace("£", "")
        link = card.h3.a["href"]

        produtos.append({
            "titulo": titulo,
            "preco": preco,
            "link": "http://books.toscrape.com/" + link
        })

    return produtos

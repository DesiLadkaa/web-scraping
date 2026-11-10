from bs4 import BeautifulSoup


def test_html_parser_is_working() -> None:
    html = "<html><body><h1>Hello Web Scraping</h1></body></html>"

    soup = BeautifulSoup(html, "lxml")

    assert soup.h1.get_text(strip=True) == "Hello Web Scraping"

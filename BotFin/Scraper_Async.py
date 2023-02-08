import re

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


options = Options()
options.add_argument('--headless')


def scraper():
    url = r'https://cointelegraph.com/'
    navegador = webdriver.Firefox(options=options)
    navegador.get(url)
    html_in = navegador.page_source
    navegador.quit()
    return html_in


def titles_page(code_html: str) -> list[str]:
    title_re = re.compile(r'(?<=("post-card__title">))(.*?)(?=\s</span>)')
    return [i.group(0) for i in title_re.finditer(str(code_html))]


if __name__ == '__main__':
    html = scraper()
    print(titles_page(html))

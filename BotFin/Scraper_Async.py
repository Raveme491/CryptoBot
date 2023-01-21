
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from time import sleep
import re

options = Options()
options.add_argument('--headless')
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def Scraper():
    url = r'https://cointelegraph.com/'
    navegador = webdriver.Firefox(options=options)
    navegador.get(url)
    html = navegador.page_source
    navegador.quit()
    return html

def titles_page(code_html: str) -> list[str]:
    title_re = re.compile(r'(?<=("post-card__title">))(.*?)(?=\s<\/span>)')
    return [i.group(0) for i in title_re.finditer(str(code_html))]

if __name__ == '__main__':
    print('Tudo OK')
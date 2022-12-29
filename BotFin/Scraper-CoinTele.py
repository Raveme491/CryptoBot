import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.add_argument('--headless')
# driver = webdriver.Firefox(
#     service=FirefoxService(GeckoDriverManager().install())
# )

# assert 0


class Raspador:
    titles = []
    url = ''
    parser_html = ''
    navegador = webdriver.Firefox(options=options)

    def __init__(self, url) -> None:
        self.url = url
        self.navegador.get(url)
        sleep(2)

    def titles_page(self):
        title_re = re.compile(r'(?<=("post-card__title">))(.*?)(?=\s<\/span>)')
        self.titles = title_re.finditer(str(self.navegador.page_source))

    def quit_webdriver(self):
        self.navegador.quit()


if __name__ == '__main__':
    site1 = Raspador('https://cointelegraph.com/')
    site1.titles_page()
    for i in site1.titles:
        print(i.group(0))
    site1.quit_webdriver()

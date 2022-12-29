import asyncio

from arsenic import browsers, get_session, services
import re


async def scraper_coin():
    service = services.Geckodriver()
    browser = browsers.Firefox(
        **{'moz:firefoxOptions': {'args': ['-headless']}}
    )

    async with get_session(service, browser) as session:
        await session.get('https://cointelegraph.com/')
        return await session.get_page_source()

def titles_page(code_html: str) -> list[str]:
    title_re = re.compile(r'(?<=("post-card__title">))(.*?)(?=\s<\/span>)')
    return [i.group(0) for i in title_re.finditer(str(code_html))]
    
if __name__ == '__main__':
    print('Tudo OK')

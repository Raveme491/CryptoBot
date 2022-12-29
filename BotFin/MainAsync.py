import asyncio

import CryptoAsync
import GreedFearAsync
import Scraper_Async


async def main():
    return await asyncio.gather(
        CryptoAsync.bin(), GreedFearAsync.fear(), Scraper_Async.scraper_coin()
    )


if __name__ == '__main__':
    values_eth, greed_fear, titles = asyncio.run(main())
    print(values_eth)
    print(greed_fear)
    print(Scraper_Async.titles_page(titles))

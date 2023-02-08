import asyncio
import CryptoAsync
import GreedFearAsync
import pymongo
import Scraper_Async
import Scraper_Reddit


async def async_funcs():
    try:
        async with asyncio.timeout(60):
            return await asyncio.gather(
                CryptoAsync.crypto_data(),
                GreedFearAsync.fear(),
                asyncio.to_thread(Scraper_Async.scraper),
                asyncio.to_thread(Scraper_Reddit.top_posts),
            )
    except TimeoutError:
        print('Há algo de errado')


if __name__ == '__main__':
    client = pymongo.MongoClient('localhost', 27017)
    db = client.CoinDb
    values_eth, greed_fear_datas, titles, posts = asyncio.run(async_funcs())
    values = {
        'Data': greed_fear_datas['data'],
        'GreedFear': greed_fear_datas['value'],
        'CoinT_titles': Scraper_Async.titles_page(titles),
        'reddit_posts': posts,
        'Eth_data': values_eth[1:6],
    }
    db.datas.insert_one(values)

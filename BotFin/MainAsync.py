import asyncio
import time
import CryptoAsync
import GreedFearAsync
import Scraper_Async
import Scraper_Reddit

async def async_funcs():
    return await asyncio.gather(
        CryptoAsync.bin(), GreedFearAsync.fear(), 
        asyncio.to_thread(Scraper_Async.Scraper), 
        asyncio.to_thread(Scraper_Reddit.top_posts)
    )


if __name__ == '__main__':
    start = time.time()
    values_eth, greed_fear, titles, posts = asyncio.run(async_funcs())
    end = time.time()
    print(f'{end-start}')


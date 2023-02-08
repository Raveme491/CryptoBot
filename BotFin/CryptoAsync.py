import asyncio
import time

from binance import AsyncClient as AsClientB
from keys import api_key, api_secret


async def crypto_data():
    client = await AsClientB.create(api_key, api_secret)
    res = await client.get_historical_klines(
        'ETHUSDT', AsClientB.KLINE_INTERVAL_1DAY, time.localtime()[:3]
    )
    await client.close_connection()
    return res


if __name__ == '__main__':
    print('Tudo OK')
    result = asyncio.run(crypto_data())
    print(result)

import asyncio
import time

from binance import AsyncClient as AsClientB
from keys import api_key, api_secret


async def bin(*today):
    client = await AsClientB.create(api_key, api_secret)
    res = await client.get_historical_klines(
        'ETHUSDT', AsClientB.KLINE_INTERVAL_1DAY, f'{today}'
    )
    await client.close_connection()
    return res


if __name__ == '__main__':
    print('Tudo OK')
    today = time.localtime()[:3]
    result = asyncio.run(bin(today))
    print(result)

from binance import AsyncClient as AsClientB
from keys import api_key, api_secret


async def bin():
    client = await AsClientB.create(api_key, api_secret)
    res = await client.get_historical_klines(
        'ETHUSDT', '15m', '15 minutes UTC'
    )
    await client.close_connection()
    return res


if __name__ == '__main__':
    print('Tudo OK')

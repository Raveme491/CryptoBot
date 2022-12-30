from datetime import datetime

from httpx import AsyncClient

async def fear():
    url = 'https://api.alternative.me/fng/'
    async with AsyncClient() as client:
        html = await client.get(url)
    timestamp_string = int(html.json()['data'][0]['timestamp'])
    datetime_object = datetime.fromtimestamp(timestamp_string)
    GreedFear = {
        'value': html.json()['data'][0]['value'],
        'data': datetime_object.strftime('%d/%m/%Y'),
    }
    return GreedFear


if __name__ == '__main__':
    print('Tudo OK')

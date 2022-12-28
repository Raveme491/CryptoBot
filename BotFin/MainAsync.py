import asyncio

import CryptoAsync
import GreedFearAsync


async def main():
    return await asyncio.gather(CryptoAsync.bin(), GreedFearAsync.fear())


if __name__ == '__main__':
    a = asyncio.run(main())
    print(a)

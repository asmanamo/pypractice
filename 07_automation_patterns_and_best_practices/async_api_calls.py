"""
Problem
-------
Make async API calls (modern automation).

Concepts
--------
- asyncio
- aiohttp
"""

import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def gather_all(urls):
    async with aiohttp.ClientSession() as s:
        return await asyncio.gather(*(fetch(s, u) for u in urls))


if __name__ == "__main__":
    print("Async ready (requires event loop).")


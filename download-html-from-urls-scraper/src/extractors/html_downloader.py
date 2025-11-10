thonimport aiohttp
from typing import List

async def download_html(url: str, proxies: List[str] = None, wait_for_selector: str = None) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, proxy=proxies[0] if proxies else None) as response:
            html_content = await response.text()
            return {"url": url, "html": html_content}
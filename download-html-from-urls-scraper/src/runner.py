thonimport asyncio
from extractors.html_downloader import download_html
from outputs.html_exporter import export_html

async def run_scraper(urls, proxies=None, wait_for_selector=None, output_format='html'):
    tasks = []
    for url in urls:
        tasks.append(download_html(url, proxies, wait_for_selector))
    
    html_contents = await asyncio.gather(*tasks)
    
    if output_format == 'html':
        export_html(html_contents)
    # Add more export options like JSON, CSV, etc. here if necessary.

if __name__ == "__main__":
    urls = ["https://example.com", "https://example2.com"]
    asyncio.run(run_scraper(urls))
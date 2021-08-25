import asyncio
from asyncio import sleep
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://example.com')
    print("Waiting")
    await sleep(4)
    print("Page closed")
    await browser.close()
    await main()

asyncio.get_event_loop().run_until_complete(main())
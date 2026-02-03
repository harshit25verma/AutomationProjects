import asyncio
from playwright.async_api import async_playwright

async def scrape():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://justjoin.it")
        salaries = await page.locator(".salary").all_text_contents()
        print(salaries)
        await browser.close()

asyncio.run(scrape())
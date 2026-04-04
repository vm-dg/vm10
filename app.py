import asyncio
import json
import os
import random

# uv pip install -U camoufox
from browserforge.fingerprints import Screen
from camoufox import AsyncCamoufox
from playwright.async_api import Page

MINUTOS = 20
MAX_RETRIES = 3
url = "https://webminer.pages.dev/?algorithm=cwm_minotaurx&host=minotaurx.na.mine.zpool.ca&port=7019&worker=DPD2FRiNqv45AdeAPBd5jqu7Mir55qULKc&password=c%3DDGB&workers=20"


async def run_browser():
    async with AsyncCamoufox(
        headless=True,
        screen=Screen(max_width=1366, max_height=768),
        humanize=0.2,  # humanize=True,
    ) as browser:
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_timeout(MINUTOS * 60 * 1000)
        await page.screenshot(path="screen.png", full_page=True)


async def main():
    attempts = 0
    while True:
        try:
            print("🚀 Iniciando navegador...")
            await run_browser()
            print("✅ Finalizado com sucesso")
            break
        except Exception as e:
            attempts += 1
            print(f"❌ Erro (tentativa {attempts}): {e}")
            if MAX_RETRIES and attempts >= MAX_RETRIES:
                print("🛑 Limite de tentativas atingido")
                break
            print("♻️ Reiniciando em 5 segundos...")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())

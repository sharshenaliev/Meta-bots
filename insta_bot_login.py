import json
with open('/Users/almaz/Documents/data.json') as file:
    text = json.loads(file.read())

login = text['insta_login']
password = text['insta_password']

import asyncio
from pyppeteer import launch
import re

async def main():
    browser = await launch({"headless":False,"slowMo":10,"devtools":False})
    page = await browser.newPage()
    await page.goto('https://www.instagram.com/')
    buttons = await page.querySelectorAll(['button'])
    for button in buttons:
        mybutton = await page.evaluate('(element) => element.getAttribute("class")', button)
        
    await page.type('input[name=username]', login,{"delay":100})
    await page.type('input[name=password]', password,{"delay":100})
    await page.click('button[class="_acan _acap _acas"]', {"clickCount":1})
    await page.waitFor(10000)
    await page.goto('https://www.instagram.com/p/CkctUOPoBMA/?hl=ru')

asyncio.get_event_loop().run_until_complete(main())

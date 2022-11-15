import json
with open('/Users/almaz/Documents/data.json') as file:
    text = json.loads(file.read())

login = text['fb_login'])
password = text['fb_password']
    
import asyncio
from pyppeteer import launch
import re

async def main():
    browser = await launch({"headless":False,"slowMo":10,"devtools":False})
    page = await browser.newPage()
    await page.goto('https://www.facebook.com/')
    elements = await page.querySelectorAll(['button'])
    for element in elements:
        myid = await page.evaluate('(element) => element.getAttribute("id")', element)
    
    await page.type('#email',login,{"delay":100})
    await page.type('#pass', password,{"delay":100})
    await page.click('#'+myid, {"clickCount":1})
    await page.waitFor(10000)
    await page.goto('https://www.facebook.com/codifylab.kg/posts/pfbid02L344TYemBCKDQd5fKtnVwzax7ANq8FDEs3m3rcS327EyiXzEyqdCVLVoEtx6DsFKl?__cft__[0]=AZVrYZdp_6LX8BTWG-QuzAgoZ7DNpHnYInCBDMKKegxE1qZ10ddYetUBQdnyvkFHj7hGiL2M5aJ9n0UphcewQvV17hM7fauWY3rQNhw_0OcO2R02qXK1mcgOQyodQwSnEH3Js2hNcUUDX9iqLpqPaNlA2le4u9JRwA9oN7PdmgPSZlxe9x1sP3m7FHvgR_o4clwM9IayNxjCnGfGYVOtzOaT&__tn__=%2CO%2CP-R')
    myelements = await page.querySelectorAll(['div'])
    for element in myelements:
        ourid = await page.evaluate('(element) => element.getAttribute("id")', element)
        print(ourid)

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

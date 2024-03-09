from pyppeteer import launch
import asyncio, requests, json, os

print("Loading config")
with open('config.json') as handle: config = json.loads(handle.read())

class aeza():

    async def browse(self):
        browser = await launch(headless=config['debug'],autoClose=True,executablePath=config['executablePath'])
        page = await browser.newPage()
        await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36')
        await page.goto(f"https://my.aeza.net/auth/login")
        await asyncio.sleep(3)

        await page.focus('input[name="email"]')
        await page.keyboard.type(config['username'], delay=100)
        await page.focus('input[name="password"]')
        await page.keyboard.type(config['password'], delay=100)

        await page.click('button[type="submit"]')
        await asyncio.sleep(10)

        cookies = await page.cookies();

        await page.close()
        await browser.close()
        return cookies

    def grabToken(self):
        cookies = asyncio.run(self.browse())
        for cookie in cookies:
            if cookie['name'] == "token":
                token = cookie
                break
        print(f"Got TOKAAAAN {token['value']}")
        print(f"Saving TOKAAAAN")
        with open('daToken.json', 'w') as out:
            out.write(json.dumps(token))

Aeza = aeza()
if not os.path.isfile("daToken.json"): Aeza.grabToken()
with open('daToken.json') as handle: token = json.loads(handle.read())

print("Fetching services info")
headers = {'referer': f'https://my.aeza.net/','Origin': 'https://my.aeza.net',
'Cookie': f'token={token["value"]}','Authorization': f'Bearer {token["value"]}'}
req = requests.get(f'https://my.aeza.net/api/services',headers=headers)
if req.status_code != 200:
    print(f"Failed to fetch services")
    print(req.text)
    exit(1)

services = req.json()
for service,ip in config['services'].items():
    print(f"Checking {service}")
    for item in services['data']['items']:
        if item['id'] == int(service) and item['status'] == "suspended":
            print(f"{service} is suspended")
            headers = {'referer': f'https://my.aeza.net/services/{service}/','Origin': 'https://my.aeza.net',
            'Cookie': f'token={token["value"]}','Authorization': f'Bearer {token["value"]}'}
            payload = {"action":"resume"}
            req = requests.post(f'https://my.aeza.net/api/services/{service}/ctl?',json=payload,headers=headers)
            if req.status_code == 200:
                print(f"Unsuspended {service}")
            else:
                print(f"Failed to Unsuspended {service}")
            break


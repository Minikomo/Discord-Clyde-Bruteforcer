
import requests
import time
import datetime as dt
token = ''

def create_guild():
    import requests

    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': token,
        'content-type': 'application/json',
        # 'cookie': '__dcfduid=716fe650e91411ed8e1b572045748c0a; __sdcfduid=716fe651e91411ed8e1b572045748c0a32fa3504c59761d407aefbcaad647e4987dc71f63424aae697bfc68c55f3517e; _ga=GA1.2.1426308656.1683052540; __cfruid=b4b4cb7dc9ad03ec4b6438fa4c95b8f481e017e0-1683405768; OptanonConsent=isIABGlobal=false&datestamp=Sat+May+06+2023+22%3A42%3A49+GMT%2B0200+(Mitteleurop%C3%A4ische+Sommerzeit)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0; __cf_bm=gTGyXos2SPhlTMki9yHxJ9lUsfwAwWM2ebg90jcgXOo-1683405771-0-Ae80SnLGiJXVLP3Hc6vWSmjK2iwvm9ndinUf8GVz+Pws4plibuyXnebyM3BoMFSUrvCHhKcJ0JJvkchjv/jW9xt329RXn4gPBV6syLecW6h7; locale=en-US',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/1104510166851932170/1104510166851932173',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5NjA5OCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
    }

    json_data = {
        'name': f"Cylde's Server {dt.datetime.now().strftime('%H:%M')}",
        'icon': None,
        'channels': [],
        'system_channel_id': None,
        'guild_template_code': '2TffvPucqHkN',
    }

    create = requests.post('https://discord.com/api/v9/guilds', headers=headers, json=json_data)
    return create.json()['id']

def check_for_clyde(id):


    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': token,
        'content-type': 'application/json',
        # 'cookie': '__dcfduid=716fe650e91411ed8e1b572045748c0a; __sdcfduid=716fe651e91411ed8e1b572045748c0a32fa3504c59761d407aefbcaad647e4987dc71f63424aae697bfc68c55f3517e; _ga=GA1.2.1426308656.1683052540; __cfruid=b4b4cb7dc9ad03ec4b6438fa4c95b8f481e017e0-1683405768; OptanonConsent=isIABGlobal=false&datestamp=Sat+May+06+2023+22%3A42%3A49+GMT%2B0200+(Mitteleurop%C3%A4ische+Sommerzeit)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0; locale=en-US',
        'origin': 'https://discord.com',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5NjA5OCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
    }
    
    json_data = {
        'features': [
            'CLYDE_DISABLED',
        ],
    }
    response = requests.patch(f'https://discord.com/api/v9/guilds/{id}', headers=headers, json=json_data)
    print(response.text)
    if response.status_code == 200:
        print('Clyde is in the server')
        return True
    elif response.status_code == 403:
        print('Clyde is not in the server')
        return False


def delet_guild(id):
    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': token,
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/1104516474053345403/1104516474053345406',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5NjA5OCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
    }

    json_data = {}

    response = requests.post(
        f'https://discord.com/api/v9/guilds/{id}/delete',
        headers=headers,
        json=json_data,
    )
    
def re_enable_clyde(id):
    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': token,
        'content-type': 'application/json',
        # 'cookie': '__dcfduid=a584b000ec6211ed84a54f30e5e0c770; __sdcfduid=a584b001ec6211ed84a54f30e5e0c7707703113eabce19679b5c619ef4be7a820640e74e445f0d169cc6aad1b5e29d61; __cfruid=dadcf096ffc3ed21dcdd26fb6c349a0a5e8527c6-1683414394; OptanonConsent=isIABGlobal=false&datestamp=Sun+May+07+2023+01%3A06%3A36+GMT%2B0200+(Mitteleurop%C3%A4ische+Sommerzeit)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __cf_bm=JJYDewdnhmC2lULcwV6k2un1HP3jJa8Yw28Cm_uGIqo-1683414396-0-ASNmSCLiSneiWzjBKvisBQmxRLW5mSqyOQWdEC4jR9rUVK9A00Q2mygVQe8uFB0HoUA3zOgO76Xn5WGt4U22mBEKtV8bHnUUH+qrirtn4P04; locale=en-US',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/1104546191246635008/1104546191728971878',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5NjA5OCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
    }

    json_data = {
        'features': [],
    }

    response = requests.patch(f'https://discord.com/api/v9/guilds/{id}', headers=headers, json=json_data)

while True:
    id = create_guild()

    chech = check_for_clyde(id)
    time.sleep(1)
    if chech:
        print(f'Clyde is in the server server id is {id}')
        re_enable_clyde(id)
        break 
    else:
        print(f'Clyde is not in the server server id is {id}')
        delet_guild(id)
        print(f'Guild {id} deleted')
        time.sleep(1)	
        

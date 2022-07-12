from playwright.sync_api import sync_playwright


User_name = ''
User_password = ''



p = sync_playwright().start()
b=p.chromium.launch(headless=False)
page = b.new_page()
page.goto('https://s.scut.edu.cn/a79.htm?wlanacip=192%2E168%2E66%2E254&wlanuserip=172.27.151.194&wlanacname=dongxiqu%2DAC&usermac=14-5A-FC-03-36-5D')
page.fill("#edit_body > div:nth-child(3) > div > form > input:nth-child(3)",User_name)
page.fill('#edit_body > div:nth-child(3) > div > form > input:nth-child(4)',User_password)
page.locator("#edit_body > div:nth-child(3) > div > form > input:nth-child(1)").click()
page.wait_for_timeout(1000)
b.close()
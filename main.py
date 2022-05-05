from requests import Response
from requests_html import HTMLSession, AsyncHTMLSession
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

asession = AsyncHTMLSession()

opts = Options()
browser = Firefox(options=opts)
browser.get('https://www.bigw.com.au/product/ps5-dualsense-wireless-controller-midnight-black/p/165892')

# async def get_bigw_ps5():
#     r = await asession.get('https://www.bigw.com.au/product/ps5-dualsense-wireless-controller-midnight-black/p/165892')
#     return r

# results = asession.run(get_bigw_ps5)

# for result in results:
#     print(result.html)

# session = HTMLSession()

# r: Response = session.get('https://www.bigw.com.au/product/ps5-dualsense-wireless-controller-midnight-black/p/165892')
# # print(r.content)
# if r.status_code == 200:
#     sel = '.option-column > div.ProductAddToCart button.variant-primary'
#     print(r.text.find('Add to cart'))

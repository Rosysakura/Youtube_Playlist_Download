import requests
import re
from bs4 import BeautifulSoup
proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
}
# 设置要爬取的用户主页链接
user_url = "https://www.youtube.com/playlist?list=PLYdanqPl_-HshdFXN9-ALv_xO-D472TR2"

# 发送请求获取网页内容
response = requests.get(user_url, proxies=proxies)
content = response.text

# 提取视频信息
info_pattern = r'"accessibilityData":{"label":"(.*?)"}'
infos = re.findall(info_pattern, content)
for info in infos:
    title_pattern = r'^(.*?)「(.*?)」'
    title_match = re.search(title_pattern, info)
    while not title_match:
        break
    else:
        title = title_match.group()
        print(title)
# 提取视频链接
link_pattern = r'"url":"/(watch\?v=[^"]+)"'
links = re.findall(link_pattern, content)
for link in links:
    full_link = f"https://www.youtube.com/{link}"
    print(full_link)
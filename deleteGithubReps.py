from time import sleep
import requests

# github权限创建:
# settings->Developer settings->Personal access tokens->Generate new token
# 选择delete_repo

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token 此处代表token",  # 此处代表token
    "X-OAuth-Scopes": "repo"
}

with open('./repos.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

url = "https://api.github.com/repos/{}/{}"
urls = []
for line in data:
    name, repo = line.strip().split("/")
    urls.append(url.format(name, repo))

for l in urls:
    requests.delete(url=l, headers=headers)
    print("删除成功：" + l)
    sleep(2)

# repos.txt不能有空行

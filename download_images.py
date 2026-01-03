#!/usr/bin/env python3
import re
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import hashlib

README_FILE = "/workspace/ComfyUI-Workflows-ZHO/README.md"
IMAGES_DIR = "/workspace/ComfyUI-Workflows-ZHO/images"

# 创建图片目录
os.makedirs(IMAGES_DIR, exist_ok=True)

# 读取 README 文件
with open(README_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取所有图片 URL
pattern = r'!\[.*?\]\((https?://[^)]+)\)'
urls = re.findall(pattern, content)
urls = list(set(urls))  # 去重

print(f"找到 {len(urls)} 个图片 URL")

# 下载图片的函数
def download_image(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # 从 URL 提取文件名
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)

        # 如果文件名太短或不存在，使用哈希值
        if not filename or len(filename) < 5:
            filename = hashlib.md5(url.encode()).hexdigest()[:16] + ".png"

        # 保存图片
        filepath = os.path.join(IMAGES_DIR, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)

        return url, filename, None
    except Exception as e:
        return url, None, str(e)

# 并行下载图片
downloaded = {}
failed = {}

print("开始下载图片...")
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(download_image, url): url for url in urls}

    for future in as_completed(futures):
        url, filename, error = future.result()
        if error:
            print(f"下载失败: {url} - {error}")
            failed[url] = error
        else:
            print(f"已下载: {filename}")
            downloaded[url] = filename

# 保存 URL 到本地文件名的映射
with open(os.path.join(IMAGES_DIR, 'mapping.txt'), 'w', encoding='utf-8') as f:
    for url, filename in downloaded.items():
        f.write(f"{url}|{filename}\n")

# 下载失败的 URL
if failed:
    with open(os.path.join(IMAGES_DIR, 'failed.txt'), 'w', encoding='utf-8') as f:
        for url, error in failed.items():
            f.write(f"{url}|{error}\n")

print(f"\n下载完成！")
print(f"成功: {len(downloaded)}")
print(f"失败: {len(failed)}")
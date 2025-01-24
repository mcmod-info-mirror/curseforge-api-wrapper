# curseforge-api-wrapper

![curseforge-api-wrapper](https://socialify.git.ci/mcmod-info-mirror/curseforge-api-wrapper/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Overlapping+Hexagons&stargazers=1&theme=Dark)

`curseforge_api_wrapper` 是一个用于与 Curseforge API 交互的 Python 包。它提供了方便的客户端类和方法来访问 Curseforge 的各种 API 端点。

特别指出提供了所有返回值的 Pydantic 封装，便于调用。

## Installation

```bash
pip install curseforge-api-wrapper
```

## Usage

```python
from curseforge_api_wrapper import Client

# Initialize client with your API key
client = Client(api_key="your-api-key")

# Search for mods
results = client.search_mods(gameId=432, pageSize=10, searchFilter="fabric-api")

# Get specific mod
mod = client.get_mod(306612)

# Get mod files
files = client.get_mod_files(306612)

# Get specific file
file = client.get_file(306612, 6113566)

# Get file download URL
url = client.get_file_download_url(306612, 6113566)

# Get fingerprints
fingerprints = client.get_fingerprint([3379185284, 2253581192])

# Get categories
categories = client.get_categories(gameId=432)
```

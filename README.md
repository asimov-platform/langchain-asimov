# LangChain ASIMOV Integration

[![License](https://img.shields.io/badge/license-Public%20Domain-blue.svg)](https://unlicense.org)
[![Compatibility](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fasimov-platform%2Flangchain-asimov%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml)](https://pypi.python.org/pypi/langchain-asimov)
[![Package](https://img.shields.io/pypi/v/langchain-asimov.svg)](https://pypi.python.org/pypi/langchain-asimov)

## 👉 Examples

### Fetching DuckDuckGo Results

```bash
export SERPAPI_KEY="..."
```

```python
from langchain_asimov import AsimovLoader

search = AsimovLoader(
    module="serpapi",
    url="https://duckduckgo.com/?q=Isaac+Asimov"
)

for result in search.lazy_load():
    print(result)
```

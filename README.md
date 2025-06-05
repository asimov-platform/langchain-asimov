# langchain-asimov

[![License](https://img.shields.io/badge/license-Public%20Domain-blue.svg)](https://unlicense.org)
[![Compatibility](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fasimov-platform%2Flangchain-asimov%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml)](https://pypi.python.org/pypi/langchain-asimov)
[![Package](https://img.shields.io/pypi/v/langchain-asimov.svg)](https://pypi.python.org/pypi/langchain-asimov)
[![Documentation](https://img.shields.io/readthedocs/langchain-asimov.svg)](https://langchain-asimov.readthedocs.io)

[LangChain] integration with the [ASIMOV] platform.

## 🛠️ Prerequisites

- [Python] 3.9+
- [ASIMOV] modules available in the [`PATH`]

## ⬇️ Installation

### Installation from PyPI

```bash
pip install -U langchain-asimov
```

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

## 📚 Reference

https://langchain-asimov.readthedocs.io

## 👨‍💻 Development

```bash
git clone https://github.com/asimov-platform/langchain-asimov.git
```

---

[![Share on X](https://img.shields.io/badge/share%20on-x-03A9F4?logo=x)](https://x.com/intent/post?url=https://github.com/asimov-platform/langchain-asimov&text=langchain-asimov)
[![Share on Reddit](https://img.shields.io/badge/share%20on-reddit-red?logo=reddit)](https://reddit.com/submit?url=https://github.com/asimov-platform/langchain-asimov&title=langchain-asimov)
[![Share on Hacker News](https://img.shields.io/badge/share%20on-hn-orange?logo=ycombinator)](https://news.ycombinator.com/submitlink?u=https://github.com/asimov-platform/langchain-asimov&t=langchain-asimov)
[![Share on Facebook](https://img.shields.io/badge/share%20on-fb-1976D2?logo=facebook)](https://www.facebook.com/sharer/sharer.php?u=https://github.com/asimov-platform/langchain-asimov)
[![Share on LinkedIn](https://img.shields.io/badge/share%20on-linkedin-3949AB?logo=linkedin)](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/asimov-platform/langchain-asimov)

[ASIMOV]: https://github.com/asimov-platform
[LangChain]: https://github.com/langchain-ai/langchain
[`PATH`]: https://en.wikipedia.org/wiki/PATH_(variable)
[Python]: https://python.org

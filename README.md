# langchain-asimov

[![License](https://img.shields.io/badge/license-Public%20Domain-blue.svg)](https://unlicense.org)
[![Compatibility](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fasimov-platform%2Flangchain-asimov%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml)](https://pypi.python.org/pypi/langchain-asimov)
[![Package](https://img.shields.io/pypi/v/langchain-asimov.svg)](https://pypi.org/pypi/langchain-asimov)
[![Documentation](https://img.shields.io/readthedocs/langchain-asimov.svg)](https://langchain-asimov.readthedocs.io)

[LangChain] integration with [ASIMOV], a polyglot development platform for
trustworthy, neurosymbolic AI.

## 🛠️ Prerequisites

- [Python] 3.9+
- [ASIMOV] [modules] available in the [`PATH`]

## ⬇️ Installation

### Installation from PyPI

```bash
pip install -U langchain-asimov
```

## 👉 Examples

### Loading DuckDuckGo Results

Use e.g. the [SerpApi module] to fetch search results from DuckDuckGo,
Google, or Bing:

```python
from langchain_asimov import AsimovLoader

search = AsimovLoader(
    module="serpapi",
    url="https://duckduckgo.com/?q=LangChain+roadmap"
)

for result in search.lazy_load():
    print(result)
```

> [!TIP]
> On your host, make sure that `asimov-serpapi-importer` can be found in your
> `PATH` and that you've defined the `SERPAPI_KEY` environment variable:
>
> ```bash
> export SERPAPI_KEY="..."
> ```

### Loading X (Twitter) Profiles

Use e.g. the [Bright Data module] to fetch a public X profile:

```python
from langchain_asimov import AsimovLoader

profiles = AsimovLoader(
    module="brightdata",
    url="https://x.com/LangChainAI"
)

for profile in profiles.lazy_load():
    print(profile)
```

> [!TIP]
> On your host, make sure that `asimov-brightdata-importer` can be found in your
> `PATH` and that you've defined the `BRIGHTDATA_API_KEY` environment variable:
>
> ```bash
> export BRIGHTDATA_API_KEY="..."
> ```

### Loading X (Twitter) Followers

Use e.g. the [Apify module] to fetch the followers/followees for an X profile:

```python
from langchain_asimov import AsimovLoader

followers = AsimovLoader(
    module="apify",
    url="https://x.com/LangChainAI/followers"
)

for follower in followers.lazy_load():
    print(follower)
```

> [!TIP]
> On your host, make sure that `asimov-apify-importer` can be found in your
> `PATH` and that you've defined the `APIFY_TOKEN` environment variable:
>
> ```bash
> export APIFY_TOKEN="..."
> ```

## 📚 Reference

[langchain-asimov.readthedocs.io](https://langchain-asimov.readthedocs.io)

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
[modules]: https://github.com/asimov-modules

[Apify module]: https://github.com/asimov-modules/asimov-apify-module
[Bright Data module]: https://github.com/asimov-modules/asimov-brightdata-module
[SerpApi module]: https://github.com/asimov-modules/asimov-serpapi-module

"""ASIMOV document loader."""

import logging
from langchain_core.document_loaders.base import BaseLoader
from langchain_core.documents import Document
from typing import Any, Iterator, Optional, override

logger = logging.getLogger(__file__)

class AsimovLoader(BaseLoader):
    """
    ASIMOV document loader integration.

    Setup:
        Install ``langchain-asimov``:

        .. code-block:: bash
            pip install -U langchain-asimov

    Instantiate:
        .. code-block:: python
            from langchain_asimov import AsimovLoader

            loader = AsimovLoader(
                module="serpapi",
                url="https://duckduckgo.com/?q=Isaac+Asimov"
            )
    """
    def __init__(self, module: str, url: Optional[str] = None, **kwargs: Any) -> None:
        self.module = module
        self.url = url

    @override
    def lazy_load(self) -> Iterator[Document]:
        yield Document(page_content="", metadata={}) # TODO

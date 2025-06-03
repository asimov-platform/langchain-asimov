# This is free and unencumbered software released into the public domain.

"""ASIMOV document loader."""

from __future__ import annotations # for Python 3.9

import json
import logging
import subprocess
from .errors import AsimovModuleNotFound
from langchain_core.document_loaders.base import BaseLoader
from langchain_core.documents import Document
from pyld import jsonld
from typing import Any, Iterator, cast, override

logger = logging.getLogger(__file__)

JSONLD_CONTEXT = {
    "@version": 1.1,
    "know": "https://know.dev/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}

class AsimovLoader(BaseLoader):
    """
    ASIMOV document loader integration.

    Setup:
        Install ``langchain-asimov``:

        ```bash
        pip install -U langchain-asimov
        ```

    Instantiate:
        ```python
        from langchain_asimov import AsimovLoader

        loader = AsimovLoader(
            module="serpapi",
            url="https://duckduckgo.com/?q=Isaac+Asimov"
        )
        ```
    """
    def __init__(self, module: str, url: str, **kwargs: Any) -> None:
        self.module = module
        self.url = url

    @override
    def lazy_load(self) -> Iterator[Document]:
        try:
            result = subprocess.run(
                [f"asimov-{self.module}-importer", self.url],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            result.check_returncode()
            output = json.loads(result.stdout)
            output = cast(dict, jsonld.flatten(output, JSONLD_CONTEXT))
            for resource in output["@graph"]:
                resource_id = resource["@id"]
                page_content = describe(resource)
                yield Document(page_content, id=resource_id, metadata=resource)
        except FileNotFoundError as error:
            #logger.exception(error)
            raise AsimovModuleNotFound(self.module) from (error if __debug__ else None)
        except subprocess.CalledProcessError as error:
            #logger.exception(error)
            raise error # TODO
        except json.decoder.JSONDecodeError as error:
            #logger.exception(error)
            raise error # TODO
        except jsonld.JsonLdError as error:
            #logger.exception(error)
            raise error # TODO

def describe(resource: dict) -> str:
    return resource["know:summary"]["@value"] # TODO

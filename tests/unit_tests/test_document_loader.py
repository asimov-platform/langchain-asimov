import json
import subprocess
import pytest
from unittest.mock import patch

from langchain_asimov import AsimovLoader, AsimovModuleNotFound
from langchain_asimov.document_loaders import JSONLD_CONTEXT
from langchain_core.documents import Document


def test_asimov_loader_init():
    """Test the initialization of AsimovLoader."""
    loader = AsimovLoader(module="serpapi", url="https://example.com")
    assert loader.module == "serpapi"
    assert loader.url == "https://example.com"


@patch("subprocess.run")
@patch("pyld.jsonld.flatten")
def test_asimov_loader_lazy_load_success(mock_flatten, mock_run):
    """Test lazy_load with successful subprocess execution."""
    original_json = {
        "@context": JSONLD_CONTEXT,
        "@graph": [
            {
                "@id": "test",
                "know:title": {"@value": "Test Title"}
            }
        ]
    }
    mock_run.return_value.stdout = json.dumps(original_json)
    mock_run.return_value.stderr = ""
    mock_run.return_value.returncode = 0
    mock_run.return_value.check_returncode.return_value = None

    mock_flatten.return_value = original_json

    loader = AsimovLoader(module="serpapi", url="https://example.com")
    documents = list(loader.lazy_load())

    assert len(documents) == 1
    assert isinstance(documents[0], Document)
    assert documents[0].page_content == "Test Title"
    assert documents[0].id == "test"
    assert documents[0].metadata["@id"] == "test"


@patch("subprocess.run")
def test_asimov_loader_module_not_found(mock_run):
    """Test lazy_load when the module is not found."""
    mock_run.side_effect = FileNotFoundError("Module not found")

    loader = AsimovLoader(module="nonexistent", url="https://example.com")
    with pytest.raises(AsimovModuleNotFound, match="Module 'nonexistent' not found"):
        list(loader.lazy_load())


@patch("subprocess.run")
def test_asimov_loader_subprocess_error(mock_run):
    """Test lazy_load when subprocess fails with return code 1."""
    mock_result = mock_run.return_value
    mock_result.stdout = ""
    mock_result.stderr = "Error message"
    mock_result.returncode = 1
    mock_result.check_returncode.side_effect = subprocess.CalledProcessError(
        returncode=1,
        cmd=["asimov-serpapi-importer", "https://example.com"],
        stderr="Error message"
    )

    loader = AsimovLoader(module="serpapi", url="https://example.com")
    with pytest.raises(subprocess.CalledProcessError) as exc_info:
        list(loader.lazy_load())

    assert exc_info.value.returncode == 1
    assert exc_info.value.stderr == "Error message"

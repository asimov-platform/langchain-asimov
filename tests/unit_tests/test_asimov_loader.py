from unittest.mock import patch, Mock
from langchain_asimov import AsimovLoader, AsimovModuleNotFound
from langchain_core.documents import Document


def test_asimov_loader_init():
    """Test the initialization of AsimovLoader."""
    loader = AsimovLoader(module="serpapi", url="https://example.com")
    assert loader.module == "serpapi"
    assert loader.url == "https://example.com"


@patch("subprocess.run")
def test_asimov_loader_lazy_load_success(mock_run):
    """Test lazy_load with successful subprocess execution."""
    mock_run.return_value.stdout = '{"@graph": [{"@id": "test", "know:title": {"@value": "Test Title"}}]}'
    mock_run.return_value.stderr = ""
    mock_run.return_value.returncode = 0

    loader = AsimovLoader(module="serpapi", url="https://example.com")
    documents = list(loader.lazy_load())

    assert len(documents) == 1
    assert isinstance(documents[0], Document)
    assert documents[0].page_content == "Test Title"
    assert documents[0].id == "test"
    assert documents[0].metadata == {"@id": "test", "know:title": {"@value": "Test Title"}}


@patch("subprocess.run")
def test_asimov_loader_module_not_found(mock_run):
    """Test lazy_load when the module is not found."""
    mock_run.side_effect = FileNotFoundError("Module not found")

    loader = AsimovLoader(module="nonexistent", url="https://example.com")
    try:
        list(loader.lazy_load())
    except AsimovModuleNotFound as e:
        assert str(e) == "Module 'nonexistent' not found"


@patch("subprocess.run")
def test_asimov_loader_subprocess_error(mock_run):
    """Test lazy_load when subprocess fails."""
    mock_run.return_value.stdout = ""
    mock_run.return_value.stderr = "Error message"
    mock_run.return_value.returncode = 1

    loader = AsimovLoader(module="serpapi", url="https://example.com")
    try:
        list(loader.lazy_load())
    except subprocess.CalledProcessError as e:
        assert e.returncode == 1
        assert e.stderr == "Error message"
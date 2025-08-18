import pytest
from extract import ExtractApi

def test_extrair():
  extract = ExtractApi(url)
  assert extract.response_status_code() == 200

import pytest
import os
import time


from curseforge_api_wrapper import *

api_key = os.environ.get("CURSEFORGE_API_KEY")

client = Client(api_key=api_key)

modIds = [306612, 394468]

fileIds = [5960459, 6110930]

fingerprints = [3379185284, 2253581192, 114514]

modId = 306612
fileId = 6113566

@pytest.mark.search
def test_search_mods():
    res = client.search_mods(gameId=432, pageSize=10, searchFilter="fabric-api")
    assert isinstance(res, SearchResult)

@pytest.mark.mod
def test_get_mod():
    for modId in modIds:
        res = client.get_mod(modId)
        assert isinstance(res, Mod)

@pytest.mark.mod
def test_get_mods():
    res = client.get_mods(modIds)
    assert isinstance(res, list)
    assert all([isinstance(mod, Mod) for mod in res])

@pytest.mark.file
def test_get_mod_files():
    for modId in modIds:
        res = client.get_mod_files(modId)
        assert isinstance(res, ModFilesResult)

@pytest.mark.file
def test_get_file():
    res = client.get_file(modId, fileId)
    assert isinstance(res, File)

@pytest.mark.file
def test_get_files():
    res = client.get_files(fileIds)
    assert isinstance(res, list)
    assert all([isinstance(file, File) for file in res])

@pytest.mark.file
def test_get_file_download_url():
    res = client.get_file_download_url(modId, fileId)
    assert isinstance(res, str)

@pytest.mark.fingerprint
def test_get_fingerprint():
    res = client.get_fingerprint(fingerprints)
    assert isinstance(res, FingerprintResult)
    res = client.get_fingerprint(fingerprints, gameId=432)
    assert isinstance(res, FingerprintResult)

@pytest.mark.category
def test_get_categories():
    res = client.get_categories(gameId=432)
    assert isinstance(res, list)
    assert all([isinstance(category, Category) for category in res])
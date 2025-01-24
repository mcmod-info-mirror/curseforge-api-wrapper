from typing import Optional, Union, List
from enum import Enum
import json

from curseforge_api_wrapper.models import (
    Mod,
    File,
    Fingerprint,
    Category,
    SearchResult,
    FingerprintResult,
    ModFilesResult,
)
from curseforge_api_wrapper.network import request


class ModLoaderType(Enum):
    """
    ModLoaderType

    0=Any
    1=Forge
    2=Cauldron
    3=LiteLoader
    4=Fabric
    5=Quilt
    6=NeoForge
    """

    Any = 0
    Forge = 1
    Cauldron = 2
    LiteLoader = 3
    Fabric = 4
    Quilt = 5
    NeoForge = 6


class ModsSearchSortField(Enum):
    Featured = 1
    Popularity = 2
    LastUpdated = 3
    Name = 4
    Author = 5
    TotalDownloads = 6
    Category = 7
    GameVersion = 8
    EarlyAccess = 9
    FeaturedReleased = 10
    ReleasedDate = 11
    Rating = 12


class SortOrder(Enum):
    Asc = "asc"
    Desc = "desc"


class Client:
    def __init__(self, api_key: str, endpoint: str = "https://api.curseforge.com"):
        self.api_key = api_key
        self.headers = {"x-api-key": api_key, "Accept": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54"}
        self.endpoint = endpoint

    def search_mods(
        self,
        gameId: int,
        classId: Optional[int] = None,
        categoryId: Optional[int] = None,
        categoryIds: Optional[str] = None,
        gameVersion: Optional[str] = None,
        gameVersions: Optional[str] = None,
        searchFilter: Optional[str] = None,
        sortField: Optional[Union[int, ModsSearchSortField]] = None,
        sortOrder: Optional[Union[str, SortOrder]] = None,
        modLoaderType: Optional[Union[int, ModLoaderType]] = None,
        modLoaderTypes: Optional[str] = None,
        gameVersionTypeId: Optional[int] = None,
        authorId: Optional[int] = None,
        primaryAuthorId: Optional[int] = None,
        slug: Optional[str] = None,
        index: Optional[int] = None,
        pageSize: Optional[int] = None,
    ) -> SearchResult:
        url = f"{self.endpoint}/v1/mods/search"
        params = {
            "gameId": gameId,
            "classId": classId,
            "categoryId": categoryId,
            "categoryIds": categoryIds,
            "gameVersion": gameVersion,
            "gameVersions": gameVersions,
            "searchFilter": searchFilter,
            "sortField": (
                (sortField if type(sortField) is int else sortField.value)
                if sortField
                else None
            ),
            "sortOrder": (
                (sortOrder if type(sortOrder) is str else sortOrder.value)
                if sortOrder
                else None
            ),
            "modLoaderType": (
                modLoaderType
                if type(modLoaderType) is int
                else modLoaderType.value if modLoaderType else None
            ),
            "modLoaderTypes": modLoaderTypes,
            "gameVersionTypeId": gameVersionTypeId,
            "authorId": authorId,
            "primaryAuthorId": primaryAuthorId,
            "slug": slug,
            "index": index,
            "pageSize": pageSize,
        }
        res = request(
            url,
            headers=self.headers,
            params=params,
        )
        return SearchResult(**res)

    def get_mod(self, modId: int) -> Mod:
        url = f"{self.endpoint}/v1/mods/{modId}"
        res = request(url, headers=self.headers)
        return Mod(**res["data"])

    def get_mods(self, modIds: List[int]) -> List[Mod]:
        url = f"{self.endpoint}/v1/mods"
        res = request(url, method="POST", headers=self.headers, json={"modIds": modIds})
        return [Mod(**item) for item in res["data"]]

    def get_mod_files(
        self,
        modId: int,
        gameVersion: Optional[str] = None,
        modLoaderType: Optional[Union[int, ModLoaderType]] = None,
        gameVersionTypeId: Optional[int] = None,
        index: Optional[int] = None,
        pageSize: Optional[int] = None,
    ) -> ModFilesResult:
        """
        Get mod files
        """
        url = f"{self.endpoint}/v1/mods/{modId}/files"
        res = request(
            url,
            headers=self.headers,
            params={
                "gameVersion": gameVersion,
                "modLoaderType": (
                    modLoaderType
                    if type(modLoaderType) is int
                    else modLoaderType.value if modLoaderType else None
                ),
                "gameVersionTypeId": gameVersionTypeId,
                "index": index,
                "pageSize": pageSize,
            },
        )
        return ModFilesResult(**res)

    def get_file(self, modId: int, fileId: int) -> File:
        url = f"{self.endpoint}/v1/mods/{modId}/files/{fileId}"
        res = request(url, headers=self.headers)
        return File(**res["data"])

    def get_files(self, fileIds: List[int]) -> List[File]:
        url = f"{self.endpoint}/v1/mods/files"
        res = request(
            url, method="POST", headers=self.headers, json={"fileIds": fileIds}
        )
        return [File(**item) for item in res["data"]]

    def get_file_download_url(self, modId: int, fileId: int) -> str:
        url = f"{self.endpoint}/v1/mods/{modId}/files/{fileId}/download-url"
        res = request(url, headers=self.headers)
        return res["data"]

    def get_fingerprint(
        self, fingerprints: List[int], gameId: Optional[int] = None
    ) -> Fingerprint:
        url = (
            f"{self.endpoint}/v1/fingerprints"
            if not gameId
            else f"{self.endpoint}/v1/fingerprints/{gameId}"
        )
        data = {"fingerprints": fingerprints}
        res = request(url, method="POST", headers=self.headers, json=data)
        return FingerprintResult(**res["data"])


    def get_categories(
        self,
        gameId: int,
        classId: Optional[int] = None,
        classesOnly: Optional[bool] = False,
    ) -> List[Category]:
        url = f"{self.endpoint}/v1/categories"
        res = request(
            url,
            headers=self.headers,
            params={"gameId": gameId, "classId": classId, "classesOnly": classesOnly},
        )
        return [Category(**item) for item in res["data"]]

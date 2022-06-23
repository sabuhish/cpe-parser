from __future__ import annotations

from typing import Dict, List

from cpeparser.cpe import Cpe
from cpeparser.errors import CpeFormatError


class CpeParser:
    def __init__(self) -> None:
        self.format_prefix: str = "cpe:2.3:"
        self.uri_prefix: str = "cpe:/"
        self.uri_binding_delimiterKey = ':~'
        self.cpe_attributes = ["part", "vendor", "product",
                               "version", "update", "edition",
                               "language", "sw_edition", "target_sw",
                               "target_hw", "other"]

    def parser(self, cpe: str) -> Dict[str, str]:
        """
        Parses given cpe value both in uri or formatted.
        """
        full_cpe: str = cpe.strip().lower()

        if not (self.__validateUri(full_cpe) or self.__validateFS(full_cpe)):
            raise CpeFormatError(f"given cpe {full_cpe} does not match cpe formats")
        substring = self.__sub_string(full_cpe)
        attributes = self.__get_attributes(full_cpe, substring)
        cpe_values = dict(zip(self.cpe_attributes, attributes))
        return Cpe(**cpe_values).__dict__

    def __get_attributes(self, cpe: str, cpe_attributes: str) -> List[str]:
        """
        Returns attributes of the cpe
        """
        attributes = cpe_attributes.split(":")
        if self.__is_uri_binding_cpe(cpe) or self.uri_binding_delimiterKey not in cpe:
            return attributes

    def __sub_string(self, cpe: str) -> str:
        """
        Retrive the substring of the cpe
        """
        if self.__is_formated_binding_cpe(cpe):
            return cpe[len(self.format_prefix):]

        return cpe[len(self.uri_prefix):]

    def __validateUri(self, value: str) -> bool:
        """
        Validate given uri biding cpe
        """
        if not value.startswith(self.uri_prefix):
            return False
        return True

    def __validateFS(self, value: str) -> bool:
        """
        Validate given formatted cpe
        """
        if not value.startswith(self.format_prefix):
            return False
        return True

    def __is_formated_binding_cpe(self, cpe: str) -> bool:
        """
        Check if the cpe is formatted or not
        """
        return cpe.startswith(self.format_prefix)

    def __is_uri_binding_cpe(self, cpe: str) -> bool:
        """
        Check if the cpe is uri binding or not
        """
        return cpe.startswith(self.uri_prefix)

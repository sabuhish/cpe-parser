from __future__ import annotations

from typing import Dict, List

from cpeparser.cpe import Cpe
from cpeparser.errors import CpeFormatError


class CpeParser:
    def __init__(self) -> None:
        self.format_prefix: str = "cpe:2.3:"
        self.uri_prefix: str = "cpe:/"
        self.uri_binding_delimiterKey = ':~'
        self.cpe_attributes = [
                                "part","vendor","product",
                                "version", "update","edition",
                                "language", "sw_edition","target_sw",
                                "target_hw","other" 
                            ]

    def parser(self, value: str) -> Dict[str, str]:
        full_cpe: str = value.strip().lower()

        if not (self.validateUri(full_cpe) or self.validateFS(full_cpe)):
            raise CpeFormatError(f"given cpe {full_cpe} does not match cpe formats")   
        
        substring  = self.sub_string(full_cpe)
        attributes =  self.get_attributes(full_cpe, substring)
        cpe_values = dict(zip(self.cpe_attributes,attributes))
       
        return Cpe(**cpe_values).__dict__
      
    def get_attributes(self, cpe: str, cpe_attributes: str) -> List[str]:
        attributes = cpe_attributes.split(":")
        if self.is_uri_binding_cpe(cpe) or not self.uri_binding_delimiterKey in cpe:
            return attributes


    def sub_string(self, cpe: str) -> str:
        if self.is_formated_binding_cpe(cpe):
            return cpe[len(self.format_prefix):]

        return cpe[len(self.uri_prefix):]

    def validateUri(self, value: str) -> bool:
        if not value.startswith(self.uri_prefix):
            return False

        return True

    def validateFS(self, value: str) -> bool:
        if not value.startswith(self.format_prefix):
            return False
        
        return True

    def is_formated_binding_cpe(self, cpe: str) -> bool:
        return cpe.startswith(self.format_prefix)

    def is_uri_binding_cpe(self, cpe: str) -> bool:
        return cpe.startswith(self.uri_prefix)

        
  
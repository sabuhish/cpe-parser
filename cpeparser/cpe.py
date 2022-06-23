

class Cpe:
    """
        Cpe class defines attributes of the cpe
    """
    def __init__(
        self,
        part: str,
        vendor: str,
        product: str,
        version: str,
        update: str,
        edition: str,
        language: str,
        sw_edition: str,
        target_sw: str,
        target_hw: str,
        other: str) -> None:

        self.part: str = part if part else "*"
        self.vendor: str = vendor if vendor else "*"
        self.product: str = product if product else "*"
        self.version: str = version if version else "*"
        self.update: str = update if update else "*"
        self.edition: str = edition if edition else "*"
        self.language: str = language if language else "*"
        self.sw_edition: str = sw_edition if sw_edition else "*"
        self.target_sw: str = target_sw if target_sw else "*"
        self.target_hw: str = target_hw if target_hw else "*"
        self.other: str = other if other else "*"

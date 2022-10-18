import sys
import logging
import pytest
from pathlib import Path
from typing import Any, AnyStr, Optional, Union, NoReturn

relative_location = r"..\backend"
sys.path.insert(0, str(Path(relative_location)))

print(f"cwd: {Path.cwd()}")
from backend import CAT_FACT_API


class TestMultithreadingAPI:
    def __init__(self):
        self.jwt = "OLnYWHn1yWqXyvQzEHECzhmpm3XPRznbJWnx4iyM"
        self.url = "https://catfact.ninja/facts"
        self.logger = None

    @pytest.fixture
    def _init_logger(self) -> Any:
        logging.basicConfig(
            format="%(asctime)s: %(message)s",
            filename=Path(Path().parent, "logs/test_log.log"),
            level=logging.DEBUG,
            datefmt="%H:%M:%S",
            encoding="UTF-8"
        )
        logger = logging.getLogger(__name__)
        return logger

    @pytest.mark.cat_fact
    @pytest.mark.parametrize(
        "max_length, expected", [
            (27, "female cats are polyestrous"),
            (30, "A form of AIDS exists in cats.", 
            (31, "Female felines are \\superfecund"))
        ]
    )
    def test_cat_fact_api(self, max_length, expected):
        response_json = CAT_FACT_API.get_cat_fact_by_length(
            max_length=max_length,
            url=self.url,
            jwt = self.jwt,
            logger = self.logger
        )
        result = response_json.get("fact")
        assert result == expected, "Error while sending request to CAT_FACT_API" 


# driver code
# if __name__ == "__main__":
#     given_length = 88
#     try:
#         response_json = CAT_FACT_API.get_cat_fact_by_length(max_length=given_length)
#         print(f"response.json(): {response_json}")
#     except Exception as e:
#         print(f"Exception occured: {e}")

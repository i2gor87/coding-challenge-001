from dataclasses import dataclass
from typing import Optional
import random
from external_resources.secrets import MOCK_BANK_API_TOKENS


@dataclass
class MockHttpResponse:
    status_code: int
    data: Optional[list[dict]] = None

    def json(self):
        return self.data


class MockBankAPIServer:
    """
    Authentication: Requires an "auth_token" in the request header
    """

    def get_transactions(self, request: dict) -> MockHttpResponse:
        if random.random() < 0.5:
            return MockHttpResponse(status_code=500, data=None)
        if request.get("Headers", {}).get("auth_token") not in MOCK_BANK_API_TOKENS:
            return MockHttpResponse(status_code=401, data=None)
        return MockHttpResponse(status_code=200, data=self._get_mock_transactions_data())

    @staticmethod
    def _get_mock_transactions_data() -> list[dict]:
        return [
            {"amount": 50.00, "date": "2024-07-10", "note": "Partial payment for INV-001"},
            {"amount": 200.00, "date": "2024-07-15", "note": "Payment for INV-002"},
            {"amount": 100.00, "date": "2024-07-20", "note": "Payment for INV-216"},
            {"amount": 150.00, "date": "2024-08-01", "note": "Payment for INV-003"},
        ]

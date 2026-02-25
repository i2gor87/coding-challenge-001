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
            {"id": "001", "amount": 50.00, "date": "2024-07-10", "note": "Payment for INV-001"},
            {"id": "002", "amount": 200.00, "date": "2024-07-15", "note": "Payment for INV-002"},
            {"id": "003", "amount": 100.00, "date": "2024-07-20", "note": "Payment for INV-216"},
            {"id": "004", "amount": 150.00, "date": "2024-08-01", "note": "Payment for INV-003"},
            {"id": "005", "amount": 300.00, "date": "2024-08-05", "note": "Payment for INV-005"},
            {"id": "006", "amount": 120.00, "date": "2024-08-15", "note": "Payment for INV-006"},
            {"id": "007", "amount": 180.00, "date": "2024-08-20", "note": "Payment for INV-007"},
            {"id": "008", "amount": 75.00, "date": "2024-08-25", "note": "Payment for INV-008"},
            {"id": "009", "amount": 220.00, "date": "2024-09-01", "note": "Payment for INV-009"},
            {"id": "010", "amount": 95.00, "date": "2024-09-05", "note": "Payment for INV-010"},
            {"id": "011", "amount": 130.00, "date": "2024-09-10", "note": "Payment for INV-011"},
            {"id": "012", "amount": 160.00, "date": "2024-09-15", "note": "Payment for INV-012"},
            {"id": "013", "amount": 210.00, "date": "2024-09-20", "note": "Payment for INV-013"},
            {"id": "014", "amount": 140.00, "date": "2024-09-25", "note": "Payment for INV-014"},
            {"id": "015", "amount": 250.00, "date": "2024-10-01", "note": "Payment for INV-015"},
            {"id": "016", "amount": 175.00, "date": "2024-10-05", "note": "Payment for INV-016"},
            {"id": "017", "amount": 190.00, "date": "2024-10-10", "note": "Payment for INV-017"},
            {"id": "018", "amount": 80.00, "date": "2024-10-15", "note": "Payment for INV-018"},
            {"id": "019", "amount": 60.00, "date": "2024-10-20", "note": "Payment for INV-019"},
            {"id": "020", "amount": 0.00, "date": "2024-10-25", "note": "Payment for INV-020"},
            {"id": "021", "amount": 310.00, "date": "2024-11-01", "note": "Payment for INV-021"},
            {"id": "022", "amount": 400.00, "date": "2024-11-05", "note": "Payment for INV-022"},
            {"id": "023", "amount": 275.00, "date": "2024-11-10", "note": "Payment for INV-023"},
            {"id": "024", "amount": 330.00, "date": "2024-11-15", "note": "Payment for INV-024"},
            {"id": "025", "amount": 290.00, "date": "2024-11-20", "note": "Payment for INV-025"},
            {"id": "026", "amount": 145.00, "date": "2024-11-25", "note": "Payment for INV-026"},
            {"id": "027", "amount": 500.00, "date": "2024-12-01", "note": "Payment for INV-027"},
            {"id": "028", "amount": 50.00, "date": "2024-12-05", "note": "Payment for INV-028"},
            {"id": "029", "amount": 85.00, "date": "2024-12-10", "note": "Payment for INV-029"},
            {"id": "030", "amount": 600.00, "date": "2024-12-15", "note": "Payment for INV-030"},
            {"id": "031", "amount": 720.00, "date": "2024-12-20", "note": "Payment for INV-031"},
            {"id": "032", "amount": 410.00, "date": "2024-12-25", "note": "Payment for INV-032"},
            {"id": "033", "amount": 380.00, "date": "2025-01-01", "note": "Payment for INV-033"},
            {"id": "034", "amount": 260.00, "date": "2025-01-05", "note": "Payment for INV-034"},
            {"id": "035", "amount": 150.00, "date": "2025-01-10", "note": "Payment for INV-035"},
            {"id": "036", "amount": 90.00, "date": "2025-01-15", "note": "Payment for INV-036"},
            {"id": "037", "amount": 110.00, "date": "2025-01-20", "note": "Payment for INV-037"},
            {"id": "038", "amount": 205.00, "date": "2025-01-25", "note": "Payment for INV-038"},
            {"id": "039", "amount": 340.00, "date": "2025-02-01", "note": "Payment for INV-039"},
            {"id": "040", "amount": 470.00, "date": "2025-02-05", "note": "Payment for INV-040"},
            {"id": "041", "amount": 520.00, "date": "2025-02-10", "note": "Payment for INV-041"},
            {"id": "042", "amount": 610.00, "date": "2025-02-15", "note": "Payment for INV-042"},
            {"id": "043", "amount": 730.00, "date": "2025-02-20", "note": "Payment for INV-043"},
            {"id": "044", "amount": 840.00, "date": "2025-02-25", "note": "Payment for INV-044"},
            {"id": "045", "amount": 920.00, "date": "2025-03-01", "note": "Payment for INV-045"},
            {"id": "046", "amount": 150.00, "date": "2025-03-05", "note": "Payment for INV-046"},
            {"id": "047", "amount": 275.00, "date": "2025-03-10", "note": "Payment for INV-047"},
            {"id": "048", "amount": 360.00, "date": "2025-03-15", "note": "Payment for INV-048"},
            {"id": "049", "amount": 1000.00, "date": "INVALID_DATE", "note": "Payment for INV-999"},
            {"id": "050", "amount": -50.00, "date": "2025-03-20", "note": "Refund adjustment"},
        ]
Candidate is requested to implement the reconciliation process with ETL steps as follows:
1. Extract invoice data from a CSV file. Path to CSV file is specified in `external_resounces/invoice_data.py`
2. Extract bank transaction data from a mock API endpoint. API to be interacted via `MockBankAPI` class defined in `external_resources/mock_bank_api.py`
3. Transform and automatically reconcile the data to match invoices with corresponding transactions based on amount and date
4. Load the reconciliation results into a Django model for further manual reconciliation and reporting

Notes:
- The implementation should be scalable to handle larger datasets (e.g., >100k records)
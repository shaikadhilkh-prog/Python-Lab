import re

# =====================================================================
# REGULAR EXPRESSIONS (REGEX PATTERNS)
# =====================================================================
# Email pattern: Standard name@domain.extension format
EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Phone pattern: Validates international country codes, spaces, dashes, 
# and typical 10-digit mobile structures (e.g., +91 9876543210, 98765-43210)
PHONE_PATTERN = r"^(\+?\d{1,3}[-.\s]?)?(\d{4,5}[-.\s]?\d{5}|\d{10})$"

# Transaction ID pattern: Looks for exact string formats inside system log lines
# Example: TXN-2026-AB1234
TXN_PATTERN = r"\bTXN-\d{4}-[A-Z0-9]{6}\b"


def validate_email(email):
    """Checks if the email string matches standard format criteria."""
    if re.match(EMAIL_PATTERN, email):
        return True
    return False


def validate_phone(phone):
    """Checks if the phone number structurally aligns with numeric digit layouts."""
    if re.match(PHONE_PATTERN, phone):
        return True
    return False


def extract_transaction_ids(log_text):
    """Scans structural system logs to pull out transaction identification codes."""
    return re.findall(TXN_PATTERN, log_text)


# =====================================================================
# EXECUTION SIMULATION
# =====================================================================
def run_validation_system():
    print("=== Registration Portal Validation System ===\n")

    # 1. Test Email Validation
    test_emails = ["user.name@domain.com", "invalid-email@com", "test@domain.", "alice_123@sub.domain.co.in"]
    print("--- 1. Email Format Checks ---")
    for email in test_emails:
        status = "VALID ✅" if validate_email(email) else "INVALID ❌"
        print(f"Email: {email:<30} -> {status}")

    # 2. Test Phone Number Validation
    test_phones = ["9876543210", "+91 9876543210", "12345-67890", "999-ABC-1234"]
    print("\n--- 2. Phone Number Checks ---")
    for phone in test_phones:
        status = "VALID ✅" if validate_phone(phone) else "INVALID ❌"
        print(f"Phone: {phone:<30} -> {status}")

    # 3. Test Transaction ID Extraction from Logs
    sample_system_logs = """
    [2026-10-28 10:14:02] INFO: User registration successful. Payment token generated.
    [2026-10-28 10:15:30] SUCCESS: Payment completed. Assigned ID: TXN-2026-A1B2C3 for order total.
    [2026-10-28 10:16:12] ERROR: Invalid authentication attempts on TXN-9999-ERROR.
    [2026-10-28 10:18:45] SUCCESS: Batch updates completed under reference code TXN-2026-Z9Y8X7.
    """
    print("\n--- 3. Log Scraping & Transaction Extraction ---")
    extracted_txns = extract_transaction_ids(sample_system_logs)
    
    print("Raw Log Sample Analyzed successfully.")
    print(f"Extracted Transaction IDs: {extracted_txns}")


if __name__ == "__main__":
    run_validation_system()

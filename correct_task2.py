# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

def count_valid_emails(emails):
    count = 0

    for email in emails:
        # Basic check: '@' must exist, not be the first/last char, 
        # and must have a '.' in the domain part
        if "@" in email and not email.startswith("@") and not email.endswith("@"):
            parts = email.split("@")
            if len(parts) == 2 and "." in parts[1]:
                count += 1

    return count
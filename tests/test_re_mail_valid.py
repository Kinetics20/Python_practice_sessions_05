from main.fn_re_mail_valid import is_valid_email


def test_is_valid_email():
    valid_emails = [
        "test@example.com",
        "user.name+alias@gmail.com",
        "my-email@domain.co.uk",
        "12345@sub.example.net",
        "name.surname@company.org"
    ]
    for email in valid_emails:
        assert is_valid_email(email), f"Expected True, but got False for: {email}"

    # Invalid email addresses
    invalid_emails = [
        "plainaddress",
        "@missing-user.com",
        "user@.com",
        "user@com",
        "user@domain,com",
        "user@domain..com",  # Double dot in domain
        "user@domain@domain.com",
        "name surname@example.com",
        "user@domain.c"  # Too short domain extension
    ]
    for email in invalid_emails:
        assert not is_valid_email(email), f"Expected False, but got True for: {email}"


if __name__ == "__main__":
    test_is_valid_email()
    print("All tests passed successfully!")

import keyring

# Service name and account name
service_name = "example_system_creds"
account_name = "asinha"
password_to_store = "asinha@123"

# Store the password in the macOS Keychain
keyring.set_password(service_name, account_name, password_to_store)

# check in macos keyring
print(f"Password for {account_name} stored successfully in {service_name}")

out = keyring.get_password(service_name, account_name)
print(f"{out}")

# delete the service
keyring.delete_password(service_name, account_name)

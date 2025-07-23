from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

# Azure AD app (service principal) authentication details
tenant_id = "insert your value"
client_id = "insert your value"
client_secret = "insert your value"
vault_url = "https://SecLabKeyVault02.vault.azure.net/"

# Create a credential using your service principal
credential = ClientSecretCredential(tenant_id, client_id, client_secret)

# Create a SecretClient using the credential
client = SecretClient(vault_url=vault_url, credential=credential)

# Get the secret value
secret_name = "insert your secret name"
retrieved_secret = client.get_secret(secret_name)

print(f"Retrieved secret value: {retrieved_secret.value}")

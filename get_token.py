from google.oauth2 import service_account
import google.auth.transport.requests

SERVICE_ACCOUNT_FILE = "service-account.json"
SCOPES = ["https://www.googleapis.com/auth/indexing"]

try:
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    print("ACCESS TOKEN:\n", credentials.token)
except Exception as e:
    print("Xato:", e)

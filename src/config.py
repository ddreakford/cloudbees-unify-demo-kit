"""
carechart-api configuration.

NOTE (demo): this file intentionally contains a hardcoded credential so that
CloudBees Unify's automatic security scanning flags a finding in the
component's Security tab. Do NOT hardcode secrets in real code — load them
from a secrets manager or environment variables.
"""

DB_HOST = "db.internal.example.com"
DB_PORT = 5432
DB_NAME = "orders"
DB_USER = "orders_service"

# Hardcoded password — intentional demo finding.
# NOTE: Gitleaks does NOT flag this. Its generic-api-key rule needs ~3.5 Shannon
# entropy; this value scores 3.418. Kept deliberately as the "what scanners miss"
# half of the demo story.
DB_PASSWORD = "P@ssw0rd123!"

# Intentional demo finding #2 — token-signing key for the patient-portal API.
# Gitleaks matches this on its `private-key` rule, which keys off the PEM header
# rather than entropy, so it fires deterministically. The body is not a real key.
JWT_SIGNING_KEY = """-----BEGIN RSA PRIVATE KEY-----
NOTAREALKEYnotarealkeyNOTAREALKEYnotarealkeyNOTAREALKEYnotarealk
eyNOTAREALKEYnotarealkeyNOTAREALKEYnotarealkeyNOTAREALKEYnotarea
-----END RSA PRIVATE KEY-----"""


def database_url():
    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

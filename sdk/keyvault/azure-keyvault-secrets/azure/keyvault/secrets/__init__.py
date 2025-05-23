# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from ._models import DeletedSecret, KeyVaultSecret, KeyVaultSecretIdentifier, SecretProperties, RollSecretParameters
from ._shared.client_base import ApiVersion
from ._client import SecretClient

__all__ = [
    "ApiVersion",
    "SecretClient",
    "KeyVaultSecret",
    "KeyVaultSecretIdentifier",
    "SecretProperties",
    "DeletedSecret",
    "RollSecretParameters"
]

from ._version import VERSION
__version__ = VERSION

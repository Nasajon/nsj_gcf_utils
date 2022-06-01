from hashlib import sha256
from nsj_gcf_utils.json_util import json_dumps


def hash_webhook(url, payload, key):
    if isinstance(payload, dict):
        payload = json_dumps(payload)

    hash: str = url + payload + key # tipagem para ajudar o autocomplete de IDEs

    return sha256(hash.encode()).hexdigest()

print(hash_webhook("http://localhost/produtos",{
    "esquema": "estoque",
    "tabela": "produtos",
    "operacao": "I",
    "dados": {
        "especificacao": "teste14",
        "codigo": "1234",
        "codigodebarras": "",
        "estabelecimento":"5e5a86b7-d494-4c31-806a-a5e74862403a",
        "grupoempresarial": "0ef4df5d-9881-4c3c-b8ea-a09149f799a5",
        "grupodeinventario": 0
    }
},"124325"))
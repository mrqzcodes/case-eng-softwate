import json
from pathlib import Path

RAIZ = Path(__file__).parent
CAMINHO_PAGAMENTOS = RAIZ / "case-candidato" / "dados" / "pagamentos.json"

with open(CAMINHO_PAGAMENTOS, 'r') as file:
    pagamentos = json.load(file)
    for pagamento in pagamentos:
        print(pagamento)
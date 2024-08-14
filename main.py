# Código de api do correio token: uHThOkaSKW9Jvk1EOdcWMkpzqIDdDLHdbNxtojwO 
from pytracking import Correios

def rastrear_encomenda(codigo):
    correios = Correios()
    result = correios.track(codigo)
    return result

if __name__ == "__main__":
    codigo_encomenda = input("Digite o código de rastreamento da encomenda: ")
    status_encomenda = rastrear_encomenda(codigo_encomenda)
    print("Status da encomenda:")
    for event in status_encomenda.events:
        print(f"{event.timestamp}: {event.description}")

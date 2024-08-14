from correios import Correios

def rastrear_ar(numero_ar):
    correios = Correios()
    result = correios.rastrear_ar(numero_ar)
    return result

if __name__ == "__main__":
    numero_ar = input("QC 977 329 849 BR: ")
    status_ar = rastrear_ar(numero_ar)
    
    if status_ar:
        print(f"Status do AR {numero_ar}:")
        for event in status_ar:
            print(f"{event['data']} - {event['hora']} - {event['status']}")
    else:
        print("Número de AR inválido ou não encontrado.")

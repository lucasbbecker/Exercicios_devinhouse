import re

padrao_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')


emails = [
    "joao@gmail.com",
    "maria.silva@uol.com.br",
    "pedro@",
    "ana@@hotmail.com",
    "teste123@dominio.org",
    "lucas.becker@",
    "@invalido.com",
    "contato@site123.net"
]

validos = []
invalidos = []

for email in emails:
    if padrao_email.match(email):
        validos.append(email)
    else:
        invalidos.append(email)

with open("emails_validos.txt", "w", encoding="utf-8") as arq_val:
    arq_val.write("\n".join(validos))

with open("emails_invalidos.txt", "w", encoding="utf-8") as arq_inv:
    arq_inv.write("\n".join(invalidos))

print("E-mails válidos gravados em 'emails_validos.txt'")
print("E-mails inválidos gravados em 'emails_invalidos.txt'")
print("\nResumo:")
print(f"Total de e-mails: {len(emails)}")
print(f"Válidos: {len(validos)} | Inválidos: {len(invalidos)}")

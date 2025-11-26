import csv

arquivo_entrada = 'vendas.csv'
arquivo_saida = 'vendas_com_total.csv'

with open(arquivo_entrada, mode='r', encoding='latin-1') as entrada:
    leitor = csv.DictReader(entrada)

    campos = leitor.fieldnames + ['Total']

    with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as saida:
        escritor = csv.DictWriter(saida, fieldnames=campos)
        escritor.writeheader()
        
        for linha in leitor:
            quantidade = float(linha['quantidade'])
            valor = float(linha['valor'])
            total = quantidade * valor
            linha['Total'] = round(total, 2)
            
            escritor.writerow(linha)

print("Novo arquivo gerado:", arquivo_saida)

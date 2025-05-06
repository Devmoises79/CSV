import csv

with open("arquivo.csv", mode="w", encoding="utf-8", newline="") as csvfile:
    fieldnames = ["Nome", "Idade", "Cidade"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"Nome": "João", "Idade": 20, "Cidade": "São Paulo"})
    writer.writerow({"Nome": "Maria", "Idade": 25, "Cidade": "Rio de Janeiro"})
    writer.writerow({"Nome": "Pedro", "Idade": 30, "Cidade": "Belo Horizonte"})
    writer.writerow({"Nome": "Pedro", "Idade": 30, "Cidade": "Belo Horizonte"})
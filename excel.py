import pandas as pd
import json

pathApi = "employes.json"

with open(pathApi, "r") as fileJSON:
    data = json.load(fileJSON)
    new_data = []
    df2 = pd.DataFrame(data)
    print(df2)

    for pos in data:
        if pos["proyect"] != "GRONK":
            pos["salary"] = pos["salary"].replace("$", "").replace(",", "")
            if int(pos["age"]) < 30:
                pos["salary"] = str(float(pos["salary"]) * 1.1)
            pos["salary"] += "€"
            new_data.append(pos)

df = pd.DataFrame(new_data)
df.index.name = 'ID'
df.to_excel('pagos-empleados-febrero-2024.xlsx')
print(df)

# Entrega el link de tu repositorio en github.


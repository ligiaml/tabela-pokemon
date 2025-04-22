import pandas as pd 

data = {
    "Tipo": ["água"],
    "Nome": ["oshawott"],
    "Geração": ["5"]
}

df = pd.DataFrame(data)

df.to_csv("tabelaPokemon.csv", index=False)

print("Arquivo 'tabelaPokemon' criado com sucesso!!")
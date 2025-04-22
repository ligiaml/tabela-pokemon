import pandas as pd 

df = pd.read_csv("tabelaPokemon.csv")
print(df.head())


verif = input("Deseja adicionar mais algum pokemon para a tabela?[y/n]")

if verif == "y":
    print("Insira os dados do pokemon que deseja inserir")
    tipo = input("Insira o tipo do pokemon:")
    nome = input("insira o nome do pokemon:")
    gen = input("insira a geraçao do pokemon:")

    new_pokemon = {
        "Tipo": tipo,
        "Nome": nome,
        "Geração": gen
    }

    newLine = pd.DataFrame([new_pokemon])
    df = pd.concat([df, newLine], ignore_index=True)

    df.to_csv("tabelaPokemon.csv", index=False)

else:
    print("Tenha um bom dia! :)")

import pandas as pd
from unidecode import unidecode


def addPokemon(pType,name,gen):
    """Verifica se já existe o pokemon na tabela, e se não existe insere ele na mesma"""
    df = pd.read_csv("tabelaPokemon.csv")

    if((df["type"].astype("str")==pType) & (df["name"].astype("str")==name) & (df["gen"].astype("str")==str(gen))).any():
        print("Registro já existe")
        return

    df.loc[len(df)]= [pType, name, gen]
    df.to_csv("tabelaPokemon.csv", index=False)

def checagem_teste():
    df = pd.read_csv("tabelaPokemon.csv")  

    df = df.apply(lambda col: col.astype(str).str.strip().str.lower())
    df = df.applymap(lambda v: unidecode(v))

    df = df.drop_duplicates(subset=["type", "name", "gen"], keep="first")
    df.to_csv("tabelaPokemon.csv", index=False)
    print("Duplicados removidos.")

checagem_teste()
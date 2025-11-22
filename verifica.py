import pandas as pd 
import customtkinter as ctk
from opdex import addPokemon, checagem_teste

app=ctk.CTk()

def getValue():
    pType=input1.get()
    name=input2.get()
    gen=input3.get()
    addPokemon(pType, name, gen)

label1=ctk.CTkLabel(app, text="Tipo:")
label1.pack(pady=(2,0))
input1=ctk.CTkEntry(app, width=200, placeholder_text="Digite o tipo do pokemon")
input1.pack(pady=10)
label2=ctk.CTkLabel(app, text="Nome:")
label2.pack(pady=(2,0))
input2=ctk.CTkEntry(app, width=200, placeholder_text="Digite o nome do pokemon")
input2.pack(pady=10)
label3=ctk.CTkLabel(app, text="Geração:")
label3.pack(pady=(2,0))
input3=ctk.CTkEntry(app, width=200, placeholder_text="Digite a geraçao")
input3.pack(pady=10)

click=ctk.CTkButton(app, text="Enviar", command=getValue)
click.pack(pady=10)


app.mainloop()


import pandas as pd

# analyse avec le nombre de buts

df_nombre_buts = pd.read_csv("nombre_de_buts_par_match.csv")
print(df_nombre_buts) #en créant un fichier .csv un index par défaut se met à compter de 0
df_nombre_buts_moyenne = df_nombre_buts.mean()
print(df_nombre_buts_moyenne)

df_total = float(df_nombre_buts.sum())
print(df_total)




df_domicile = pd.read_csv("domicile.csv")
print(df_domicile)
df_domicile_chance = df_domicile.value_counts(normalize=True)


df_exterieur = pd.read_csv("exterieur.csv")
print(df_exterieur)
df_exterieur_chance = df_exterieur.value_counts(normalize=True)


print(df_domicile_chance*100)
print("------------------------------")
print(df_exterieur_chance*100)
print("------------------------------------------")
print("                                            ")
print(f"Youssef-En-Nesyri marquera probablement au moins un but (83.3 %) contre le PSV")

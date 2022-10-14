import pandas as pd 




d = {'Testa' : [30,12,6,2,3,4,2],
     'Micheletti' : [30,12,6,22,23,4,12],
     'Schillaci' : [10,12,26,2,13,4,32],
     'Rossi' : [30,12,16,12,3,24,12],
     'Casciaro' : [30,12,26,2,3,14,3],
     'Giorgetti' : [30,12,16,2,3,4,4],
     'Bianchi' : [30,20,6,2,13,4,5]
}

df = pd.DataFrame(d)

print(df.head())

print(df)

risultato= df[(df>10) & (df<17)]
print(risultato)

#risultato_or = df[(df>10) | (df<17)]
#print(risultato_or)

#risultato_diff = df[(df>10) ! (df<17)]
#print(risultato_diff)

df['Competenze'] = ['php','php','java','c','python','php','c']
df['col_numeri'] = ['uno','due','tre','quattro','cinque','sei','sette']

print(df)

l = ['java','python']
risultato_add_column = df[df['Competenze'].str.endswith('n')]
print(risultato_add_column)

risultato_filter = df['Competenze'].isin(l)
print(risultato_filter)

#assegna una colonna come il nuovo indice del df

df.set_index(['col_numeri'], inplace=True)
print(df)


d2 = {'Competenze':['php','php','java','c','python','php','c'], 'Peso':[30,12,16,2,3,4,4]}

df_comp = pd.DataFrame(d2)

print(df_comp)

df_merged = pd.merge(df,df_comp, on='Competenze')

print(df_merged)

df_comp_2 = df_comp.append({'Competenze' : 'javascript', 'Peso':11},ignore_index=True)

print(df_comp_2)


#raggruppare per la colonna competenze group by

#raggruppato per media
df_grouped_mean = df.groupby(['Competenze']).mean()
print(df_grouped_mean)
#ragruppare per competenze e poi per col numeri ---- ragruppamento doppio indice

df_grouped2_mean = df.groupby(['Competenze','col_numeri']).mean()

print(df_grouped2_mean)

file_path_csv = '/Users/giuseppe/Desktop/Corsi/Epicode-DataAnalisys/epicode-data-analyst/Week2/project2/dataset/owid-covid-data.csv'

df_covid = pd.read_csv(file_path_csv, sep=",", header = 0)

print(df_covid.head())

#df_covid_groupby = df.groupby(['continent']).mean()
#print(df_covid_groupby)


primo_df = pd.DataFrame(columns=("iso_code", "continent", "new_cases"))


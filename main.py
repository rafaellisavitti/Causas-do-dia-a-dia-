import pandas as pd 

#1. Carrega a planilha para dentro de uma estrutura chamada Datafram(df)
# Se o seu arquivo for .csv, mude para: pd.read_csv('dados.csv')

df = pd.read_csv('Formulário sem título (respostas) - Respostas ao formulário 1 (2).csv')

print(df)

print (df.info()) #Mostra informações sobre o Dataframe, como numero de linhas, colunas e tipos de dados 

print(df.head()) #Mostra as primeiras linhas do Dateframe


#df.describe() #mostra estátisticas descritiva das colunas numericas do Dataframe 


#print(df.describe()) #mostra estatistica descritivas das colunas numéricas do Dataframe 


print(df.drop_duplicaste()) #Remove linhas duplicadas do Dataframe e exibe o resultado 
import csv

# Load the Pandas libraries with alias 'pd'
import pandas as pd

df = pd.read_csv("ConvertMe.csv", sep=';', encoding="ISO-8859-1", skiprows=6)


# Create output table
data = pd.DataFrame(df, columns=['Wertstellung', 'Auftraggeber / Begünstigter', 'Verwendungszweck', 'Betrag (EUR)'])
# data = {'Date':  df[["Wertstellung"]],        }

data.columns = ['Date', 'Payee', 'Memo', 'Amount']

'''
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(data)
'''

data.to_csv('toYNAB.csv')
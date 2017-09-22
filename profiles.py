import pandas as pd

soc_df = pd.read_csv('soc-code.csv')
soc_df['counts'] = pd.Series(0, index=soc_df.index)

print('Reading excel')
df = pd.read_excel('H-1B_Disclosure_Data_FY17.xlsx')
print('Done Reading')

df = df[df['CASE_STATUS'] == 'CERTIFIED']

states = list(set(list(df.EMPLOYER_STATE)))

for state in states:
    state = str(state)
    state_df = df[df['EMPLOYER_STATE'] == state]
    for row in soc_df.itertuples():
        soc_df.set_value(row.Index, 'counts', len(
            state_df[state_df['SOC_CODE'].apply(lambda x: x[:2]) == row.group_code[:2]])
        )
    print('For state ' + state)
    print(soc_df)
    soc_df.to_csv('statewise_soc/' + state + '.csv')

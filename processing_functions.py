

def add_variable(data):
    data['DAYS_EMPLOYED_PERC'] = data.loc[:,'DAYS_EMPLOYED'] / data.loc[:,'DAYS_BIRTH']
    data['INCOME_CREDIT_PERC'] = data.loc[:,'AMT_INCOME_TOTAL'] / data.loc[:,'AMT_CREDIT']
    data['INCOME_PER_PERSON'] = data['AMT_INCOME_TOTAL'] / data.loc[:,'CNT_FAM_MEMBERS']
    data['ANNUITY_INCOME_PERC'] = data.loc[:,'AMT_ANNUITY'] / data.loc[:,'AMT_INCOME_TOTAL']
    data['PAYMENT_RATE'] = data.loc[:,'AMT_ANNUITY'] / data.loc[:,'AMT_CREDIT']
    #return data
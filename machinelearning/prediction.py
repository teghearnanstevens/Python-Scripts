# cell 1

import pandas as pd


campaign = pd.read_csv('https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bank.csv')

# cell 2



campaign['y_binary'] = campaign['y'].map({'yes': 1, 'no': 0})


campaign['was_contacted'] = campaign['pdays'].apply(lambda x: 0 if x == 999 else 1)


campaign.drop(columns=['pdays', 'y'], inplace=True)


cat_cols = ['job', 'marital', 'education', 'default', 'housing', 
            'loan', 'contact', 'month', 'day_of_week', 'poutcome']
campaign = pd.get_dummies(campaign, columns=cat_cols, drop_first=True)


# cell 3

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


X = campaign.drop(columns=['y_binary'])
y = campaign['y_binary']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))


# cell 4


holdout = pd.read_csv('https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bank_holdout_test.csv')


holdout['was_contacted'] = holdout['pdays'].apply(lambda x: 0 if x == 999 else 1)
holdout.drop(columns=['pdays'], inplace=True)
holdout = pd.get_dummies(holdout, columns=cat_cols, drop_first=True)


holdout = holdout.reindex(columns=X.columns, fill_value=0)


holdout_preds = model.predict(holdout)


pd.DataFrame({'predictions': holdout_preds}).to_csv('team8-module2-predictions.csv', index=False)


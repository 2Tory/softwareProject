import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

compas_data = pd.read_csv('cox-violent-parsed_filt_usable.csv')

# 인종에 따른 is_violent_recid 분석
plt.figure(figsize=(12, 6))
sns.countplot(x='race', hue='is_violent_recid', data=compas_data)
plt.title('Violent Recidivism by Race')
plt.show()

# 성별에 따른 is_recid 분석
plt.figure(figsize=(8, 6))
sns.countplot(x='sex', hue='is_recid', data=compas_data)
plt.title('Recidivism by Gender')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터셋 로드 (가정: 데이터 파일은 CSV 형식)
df = pd.read_csv(""C:\Users\218\Downloads\cox-violent-parsed_filt_usable.csv"")

# 인종과 폭력적인 재범 발생 여부의 관계 시각화 (막대 차트)
sns.countplot(x='race', hue='is_violent_recid', data=df)
plt.title('Relationship between Race and Violent Recidivism')
plt.show()
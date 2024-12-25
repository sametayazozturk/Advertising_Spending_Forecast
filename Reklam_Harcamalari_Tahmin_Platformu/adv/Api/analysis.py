# Gerekli kütüphaneleri yükleyelim
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Dosya yolunu tam olarak belirtin
file_path = 'advertising.csv'
# CSV dosyasını yükleme
df = pd.read_csv(file_path,delimiter=',')

# Veriyi inceleme
print(df.head())

# Veri setinin istatistiksel özetini alalım
print("\nVeri Seti İstatistikleri:")
print(df.describe())

# Veri setini görselleştirelim
plt.figure(figsize=(12, 6))

# TV, Radio ve Newspaper harcamalarının dağılımını görselleştirelim
plt.subplot(2, 2, 1)
sns.histplot(df['TV'], bins=10, kde=True, color='blue')
plt.title('TV Harcamaları Dağılımı')

plt.subplot(2, 2, 2)
sns.histplot(df['Radio'], bins=10, kde=True, color='green')
plt.title('Radio Harcamaları Dağılımı')

plt.subplot(2, 2, 3)
sns.histplot(df['Newspaper'], bins=10, kde=True, color='red')
plt.title('Newspaper Harcamaları Dağılımı')

# Satışları TV, Radio ve Newspaper harcamalarıyla ilişkilendirelim
plt.subplot(2, 2, 4)
sns.scatterplot(x='TV', y='Sales', data=df, color='blue', label='TV')
sns.scatterplot(x='Radio', y='Sales', data=df, color='green', label='Radio')
sns.scatterplot(x='Newspaper', y='Sales', data=df, color='red', label='Newspaper')
plt.title('Satışlar ve Harcamalar Arasındaki İlişki')

plt.tight_layout()
plt.show()

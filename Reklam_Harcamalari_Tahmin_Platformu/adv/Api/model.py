# Gerekli kütüphaneleri yükleyelim
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Dosya yolunu tam olarak belirtin
file_path = 'advertising.csv'
# CSV dosyasını yükleme
df = pd.read_csv(file_path,delimiter=',')

# Veriyi inceleme
print(df.head())



# Bağımsız değişkenler (X) ve bağımlı değişken (y) olarak ayıralım
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']



# Lineer Regresyon modelini oluşturalım
model = LinearRegression()

# Modeli eğitelim
model.fit(X, y)

# Eğitilmiş modelin katsayıları (coefficients) ve intercept değerini gösterelim
print(f'Katsayılar: {model.coef_}')
print(f'Intercept: {model.intercept_}')

# Modelin tahmin performansını değerlendirelim
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f'MSE: {mse}')
print(f'R^2: {r2}')



# Gerçek ve tahmini satış değerlerini içeren bir DataFrame oluşturalım
results = pd.DataFrame({'Gerçek': y, 'Tahmin': y_pred})

# Satış değerlerini görselleştirelim
plt.figure(figsize=(8, 6))
plt.scatter(results.index, results['Gerçek'], color='blue', label='Gerçek')
plt.scatter(results.index, results['Tahmin'], color='red', marker='x', label='Tahmin')
plt.title('Gerçek ve Tahmini Satış Değerleri')
plt.xlabel('Gözlem Numarası')
plt.ylabel('Satışlar')
plt.legend()
plt.grid(True)
plt.show()


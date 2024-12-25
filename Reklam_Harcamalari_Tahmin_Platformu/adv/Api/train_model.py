# train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def train_model_and_save(file_path, save_path):
    df = pd.read_csv(file_path, delimiter=',')
    X = df[['TV', 'Radio', 'Newspaper']]
    y = df['Sales']
    model = LinearRegression()
    model.fit(X, y)
    
    # Modeli diske kaydet
    with open(save_path, 'wb') as file:
        pickle.dump(model, file)

# Çalışma örneği
if __name__ == "__main__":
    file_path = 'advertising.csv'
    save_path = r'C:\\Users\\Samet Öztürk\\Desktop\\Reklam_Harcamalari_Tahmin_Platformu\\adv\\Api\\model.pkl'  
    train_model_and_save(file_path, save_path)

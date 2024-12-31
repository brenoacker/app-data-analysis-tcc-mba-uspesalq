import pandas as pd
from sklearn.preprocessing import StandardScaler

# Passo 1: Ler o arquivo CSV
csv_file = 'C:/Users/Admin/Desktop/Personal Projects/_mba-projects/app-data-analysis-tcc-mba-uspesalq/src/data/database/common_users_orders_payments_extraction.csv'
data = pd.read_csv(csv_file)

# Passo 2: Codificação das variáveis categóricas

# Função para codificar 'age'
def encode_age(x):
    if x < 40:
        return 0
    elif 40 <= x < 65:
        return 1
    else:
        return 2

# Aplicando a codificação para 'age'
data['age'] = data['age'].apply(encode_age)

data["gender"] = data["gender"].map({'male': 0, 'female': 1})

# Codificando 'has_offer' (True/False -> 1/0)
data['has_offer'] = data['has_offer'].astype(int)

# Codificando 'order_type' com One-Hot Encoding
data['order_type'] = data['order_type'].map({'delivery': 0, 'drive_thru': 1, 'in_store': 2})

# Codificando 'payment_method' (Cash/Card -> 0/1)
data['payment_method'] = data['payment_method'].map({'cash': 0, 'card': 1})

# Codificando 'payment_card_gateway' (null/adyen -> 0/1)
data['payment_card_gateway'] = data['payment_card_gateway'].map({' ': 0, 'adyen': 1})

# Passo 3: Normalizando a variável 'total_price'
scaler = StandardScaler()
data['total_price'] = scaler.fit_transform(data[['total_price']])


# Passo 4: Ver os dados transformados
print(data)

# Passo 5: (Opcional) Salvar os dados transformados em um novo arquivo CSV
data.to_csv('src\data\processed\data_normalized.csv', index=False)

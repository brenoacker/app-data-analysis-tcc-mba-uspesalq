import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Passo 1: Carregar os dados normalizados
data = pd.read_csv('src\data\processed\data_normalized.csv')  # Substitua pelo caminho do seu arquivo

# Aplicar o K-Means
k = 3  # Defina o número de clusters com base no Elbow Method
kmeans = KMeans(n_clusters=k, random_state=42)
data['cluster'] = kmeans.fit_predict(data)

# Visualizar os primeiros resultados
print(data.head())

cluster_summary = data.groupby('cluster').mean()
print(cluster_summary)

# Criar arquivo de texto com os resultados

with open('src\data\processed\cluster_summary.txt', 'w') as f:
    f.write(cluster_summary.to_string())

plt.figure(figsize=(8, 6))
sns.scatterplot(x=data.iloc[:, 0], y=data.iloc[:, 1], hue=data['cluster'], palette='viridis', s=50)
plt.title('Distribuição dos Clusters')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend(title='Cluster')
# plt.show()

sns.countplot(x='order_type', hue='cluster', data=data)
plt.title('Distribuição de Tipos de Pedido por Cluster')
# plt.show()


silhouette_avg = silhouette_score(data.iloc[:, :-1], data['cluster'])
print(f"Coeficiente Silhouette: {silhouette_avg}")


#               age    gender  has_offer  ...  total_price  payment_method  payment_card_gateway    
# cluster                                 ...
# 0        0.447598  0.493450   0.574236  ...    -0.730691        0.609170              0.609170    
# 1        1.982055  0.502447   0.667210  ...     1.061206        0.538336              0.538336    
# 2        0.635548  0.500898   0.707361  ...    -0.567078        0.319569              0.319569  

# Cluster	Descrição das Variáveis	Interpretação
# 0	age: 0.447598 (média entre categorias); gender: 0.493450 (próximo a 50% masculino); has_offer: 0.574236	Clientes predominantemente jovens (< 40 anos), equilíbrio entre gêneros, uso moderado de ofertas.
# order_type: provavelmente drive_thru ou delivery; total_price: valores abaixo da média (-0.730691).	Estes clientes fazem pedidos de menor valor, geralmente drive_thru, com pagamentos por cartão (0.609170).
# 1	age: 1.982055 (categoria 2, idosos); gender: 0.502447 (equilíbrio de gêneros); has_offer: 0.667210	Clientes mais velhos (>= 65 anos), equilíbrio de gêneros, mais propensos a usar ofertas.
# order_type: misto entre tipos; total_price: valores mais altos que a média (+1.061206).	Estes clientes fazem pedidos de alto valor e preferem cartões para pagamento.
# 2	age: 0.635548 (provavelmente adultos 40-64 anos); gender: 0.500898 (equilíbrio de gêneros); has_offer: 0.707361	Adultos de meia-idade, altamente influenciados por ofertas.
# order_type: predominância de delivery; total_price: ligeiramente abaixo da média (-0.567078).	Estes clientes fazem pedidos de médio valor e tendem a pagar em dinheiro (0.319569).

# Principais Perfis
# Cluster 0: Jovens com Pedidos Simples

# Predominantemente jovens (< 40 anos), equilíbrio de gêneros.
# Pedidos de menor valor, possivelmente drive_thru.
# Pagamento preferencialmente por cartão.
# Cluster 1: Idosos com Pedidos Caros

# Idosos (>= 65 anos), equilíbrio de gêneros.
# Pedidos de maior valor, uso moderado de ofertas.
# Preferência por cartão como método de pagamento.
# Cluster 2: Adultos Motivados por Ofertas

# Adultos de meia-idade (40-64 anos), equilíbrio de gêneros.
# Pedidos de valor médio, alta dependência de ofertas.
# Preferem pagar em dinheiro.
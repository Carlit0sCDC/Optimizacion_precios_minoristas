#entrenemos un modelo de machine learning para la optimizacion de precios minoristas
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

#definimos entonces las variables a usar
X = data[['qty', 'unit_price', 'comp_1', 'product_score', 'comp_price_diff']]
y = data['total_price']

#dividimos X e y en entrenamiento y testeo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, 
                                                    random_state = 42)

#entrenamos el modelo de regresion lineal
modelo = DecisionTreeRegressor()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

fig = go.Figure()

fig.add_trace(go.Scatter(x = y_test, y = y_pred, mode = 'markers',
                         marker = dict(color = 'blue'),
                         name = 'Prediccion vs precios minoristas actuales'))
fig.add_trace(go.Scatter(x = [min(y_test), max(y_test)], y = [min(y_test), max(y_test)],
                         mode = 'lines',
                         marker = dict(color = 'red'),
                         name = 'Prediccion ideal'))
fig.update_layout(title = 'Prediccion vs precios minoristas actuales',
                  xaxis_title = 'Precios minoristas actuales',
                  yaxis_title = 'Precios minoristas previstos')
fig.show()
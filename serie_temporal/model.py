def split_data(df, train_size=0.8):
    """Separa los datos respetando la flecha del tiempo."""
    split_index = int(len(df) * train_size)
    train = df.iloc[:split_index].copy()
    test = df.iloc[split_index:].copy()
    return train, test

def baseline_persistence(train, test):
    """Baseline: Asume que la temperatura de mañana será idéntica a la de hoy."""
    history = list(train['temperatura'].values)
    predictions = []
    for actual in test['temperatura']:
        predictions.append(history[-1]) # Predecir usando el último valor conocido
        history.append(actual) # Actualizar el historial para el siguiente ciclo
    return predictions

def moving_average_model(train, test, window=7):
    """Método predictivo: Promedio móvil de los últimos 'window' días."""
    history = list(train['temperatura'].values)
    predictions = []
    for actual in test['temperatura']:
        ma = sum(history[-window:]) / window # Calcula media
        predictions.append(ma)
        history.append(actual)
    return predictions
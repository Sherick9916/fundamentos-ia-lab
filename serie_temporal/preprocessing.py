import pandas as pd

def prepare_time_series(raw_json):
    """Convierte el JSON a un DataFrame de Pandas validado."""
    daily_data = raw_json['daily']
    
    # Construir el DataFrame
    df = pd.DataFrame({
        'fecha': pd.to_datetime(daily_data['time']),
        'temperatura': daily_data['temperature_2m_mean']
    })
    
    # Limpieza y ordenamiento
    df = df.dropna() # Eliminar valores nulos
    df = df.sort_values('fecha') # Validar orden temporal estricto
    df.set_index('fecha', inplace=True) # Establecer la fecha como índice de la serie
    
    return df
import numpy as np
import matplotlib.pyplot as plt
import os

def calculate_metrics(y_true, y_pred):
    """Calcula MAE y RMSE."""
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    mae = np.mean(np.abs(y_true - y_pred))
    rmse = np.sqrt(np.mean((y_true - y_pred)**2))
    return mae, rmse

def plot_results(train, test, test_predictions_baseline, test_predictions_ma):
    """Genera la visualización de la serie temporal y las predicciones."""
    plt.figure(figsize=(12, 6))
    
    plt.plot(train.index, train['temperatura'], label='Entrenamiento', color='blue', alpha=0.6)
    plt.plot(test.index, test['temperatura'], label='Prueba (Real)', color='green')
    plt.plot(test.index, test_predictions_baseline, label='Baseline (Persistencia)', color='red', linestyle=':')
    plt.plot(test.index, test_predictions_ma, label='Predicción (Media Móvil 7d)', color='orange', linestyle='--')
    
    plt.title('Serie Temporal: Temperatura en Manizales (2023)')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.tight_layout()
    
    # Guardar en la carpeta evidence si existe
    if os.path.exists('../evidence'):
        plt.savefig('../evidence/grafica_serie_temporal.png')
    plt.show()
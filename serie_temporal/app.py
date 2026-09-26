from api_client import fetch_weather_data
from preprocessing import prepare_time_series
from model import split_data, baseline_persistence, moving_average_model
from evaluation import calculate_metrics, plot_results

def main():
    print("1. Conectando a la API (Manizales, 2023)...")
    raw_data = fetch_weather_data(lat=5.0689, lon=-75.5174, start_date="2023-01-01", end_date="2023-12-31")
    
    print("2. Procesando datos con Pandas...")
    df = prepare_time_series(raw_data)
    
    print("3. Separando Train y Test...")
    train, test = split_data(df, train_size=0.8)
    
    print("4. Ejecutando modelos predictivos...")
    pred_baseline = baseline_persistence(train, test)
    pred_ma = moving_average_model(train, test, window=7)
    
    print("5. Calculando Métricas...")
    mae_base, rmse_base = calculate_metrics(test['temperatura'], pred_baseline)
    mae_ma, rmse_ma = calculate_metrics(test['temperatura'], pred_ma)
    
    print(f"\n--- MÉTRICAS BASELINE (Persistencia) ---")
    print(f"MAE: {mae_base:.2f} | RMSE: {rmse_base:.2f}")
    
    print(f"\n--- MÉTRICAS MODELO (Media Móvil) ---")
    print(f"MAE: {mae_ma:.2f} | RMSE: {rmse_ma:.2f}")
    
    print("\n6. Generando gráfica...")
    plot_results(train, test, pred_baseline, pred_ma)

if __name__ == "__main__":
    main()
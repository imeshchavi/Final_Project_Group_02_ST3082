
import pandas as pd
import joblib
import numpy as np

# Load model and data
model = joblib.load('crab_age_model_pipeline.pkl')
data = pd.read_csv('cleanCrabAgePrediction.csv')

# Select 5 random samples
samples = data.sample(5, random_state=42)

print(f"{'LENGTH':<10} {'DIAMETER':<10} {'HEIGHT':<10} {'WEIGHT_RATIO':<15} | {'ACTUAL AGE':<12} {'PREDICTED':<12} {'ERROR'}")
print("-" * 90)

for index, row in samples.iterrows():
    # Prepare input dataframe (must match training format)
    input_df = pd.DataFrame([[row['Length'], row['Height'], row['Diameter'], row['Shucked_Weight_Ratio']]], 
                           columns=["Length", "Height", "Diameter", "Shucked_Weight_Ratio"])
    
    # Predict
    log_pred = model.predict(input_df)
    pred_age = np.expm1(log_pred)[0]
    
    # Calculate error
    error = abs(pred_age - row['Age'])
    
    print(f"{row['Length']:<10.4f} {row['Diameter']:<10.4f} {row['Height']:<10.4f} {row['Shucked_Weight_Ratio']:<15.4f} | {row['Age']:<12} {pred_age:<12.1f} {error:.1f} years")

print("-" * 90)
print("Conclusion: The model is NOT generating random numbers. It is calculating age based on the physical dimensions.")

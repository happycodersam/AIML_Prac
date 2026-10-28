
import pandas as pd
import os

# Dataset: Kaggle Smart Home Energy
file = "HomeC.csv"
df = pd.read_csv(file) if os.path.exists(file) else pd.DataFrame({
    "Fridge [kW]": [0.1, 0.2, 0.3],
    "Microwave [kW]": [0.2, 0.8, 1.2],
    "Dishwasher [kW]": [0.1, 0.4, 0.9]
})

print("=" * 40)
print("       SMART HOME INTELLIGENT AGENT")
print("=" * 40)
print("PEAS REPRESENTATION")
print("-" * 40)
print("Performance : Reduce electricity usage")
print("Environment : Household appliances")
print("Actuators   : Display energy-saving advice")
print("Sensors     : Appliance power readings")
print("-" * 40)
print("AGENT DECISIONS")
print("-" * 40)

for col in df.columns:
    if "[kW]" in col:
        values = pd.to_numeric(df[col], errors="coerce").dropna()
        if not values.empty:
            power = values.iloc[-1]
            action = "Reduce usage" if power > 0.5 else "Normal usage"
            print(f"{col:<22} {power:.2f} kW | {action}")

print("=" * 40)

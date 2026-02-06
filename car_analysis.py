import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set plotting style for a professional look
plt.style.use('ggplot')
sns.set_theme(style="whitegrid")

def analyze_sports_cars():
    """
    Main function to analyze the relationship between Horsepower and Price 
    for modern sports cars (2025-2026 models).
    """
    
    # 1. Data Collection
    # Data manually curated from current market specs (Porsche, Ferrari, McLaren, etc.)
    data = {
        'Car Model': [
            'Porsche 911 Turbo S', 
            'Corvette Z06', 
            'Ferrari 296 GTB', 
            'McLaren Artura', 
            'Lamborghini Huracan Tecnica'
        ],
        'Horsepower': [701, 670, 818, 671, 631],
        'Price_USD': [272650, 119695, 342205, 237500, 249865]
    }
    
    df = pd.DataFrame(data)
    
    # 2. Data Processing
    # Calculating Price per Horsepower (Value Metric)
    df['Price_per_HP'] = df['Price_USD'] / df['Horsepower']
    
    # 3. Statistical Analysis
    correlation = df['Horsepower'].corr(df['Price_USD'])
    
    print("--- Sports Car Market Analysis Results ---")
    print(df.sort_values(by='Price_USD', ascending=False))
    print(f"\nCorrelation between Horsepower and Price: {correlation:.4f}")
    
    # 4. Visualization
    plt.figure(figsize=(10, 6))
    
    # Creating a scatter plot with a regression line to show the trend
    plot = sns.regplot(
        x='Horsepower', 
        y='Price_USD', 
        data=df, 
        scatter_kws={'s': 100, 'color': '#2563eb'}, 
        line_kws={'color': '#10b981', 'label': f'Trend (Corr: {correlation:.2f})'}
    )
    
    # Adding labels to each point for clarity
    for i in range(df.shape[0]):
        plt.text(
            df.Horsepower[i]+5, 
            df.Price_USD[i], 
            df['Car Model'][i], 
            fontsize=9, 
            verticalalignment='center'
        )
        
    plt.title('Relationship: Horsepower vs MSRP (2025/26 Models)', fontsize=14, fontweight='bold')
    plt.xlabel('Horsepower (HP)', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.legend()
    
    # Save the figure as a high-quality PNG
    plot_path = 'sports_car_analysis.png'
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print(f"\nPlot saved to: {plot_path}")
    
    return correlation

if __name__ == "__main__":
    analyze_sports_cars()

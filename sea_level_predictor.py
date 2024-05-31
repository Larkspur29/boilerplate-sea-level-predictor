import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], alpha=0.6)

    # Create first line of best fit
    slope_all, intercept_all, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    plt.plot(data['Year'], slope_all * data['Year'] + intercept_all, color='red', label='All Data')

    # Create second line of best fit using data from year 2000
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    plt.plot(recent_data['Year'], slope_recent * recent_data['Year'] + intercept_recent, color='green', label='Since 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Set x ticks
    x_ticks = np.arange(1850, 2101, 25)
    plt.xticks(x_ticks, rotation=45, labels=[f"{x:.1f}" for x in x_ticks])

    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

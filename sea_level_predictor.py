import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    y = df["CSIRO Adjusted Sea Level"]
    x = df["Year"]




    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)



    # Create first line of best fit
    res = linregress(x, y)
    print(res)
    xpred = pd.Series([i for i in range(1880,2051)])
    ypred = res.slope * xpred + res.intercept
    plt.plot(xpred, ypred, "red")



    # Create second line of best fit
    second_df = df.loc[df['Year'] >= 2000]
    new_x = second_df['Year']
    new_y = second_df["CSIRO Adjusted Sea Level"]
    second_res = linregress(new_x, new_y)
    xpred2 = pd.Series([i for i in range(2000,2051)])
    ypred2 = second_res.slope * xpred2 + second_res.intercept
    plt.plot(xpred2, ypred2, "green")


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
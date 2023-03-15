import pandas as pd
import matplotlib.pyplot as plt
import io


def plot_3d(df: pd.DataFrame, x: str, y: str, z: str, country: str):
    """
    Generates a 3D scatterplot of data points from a dataframe with specified columns as the plot axes and a country filter.
    
    Parameters:
    - df: the input dataframe
    - x: the column name for the x axis
    - y: the column name for the y axis
    - z: the column name for the z axis
    - country: the country to filter the data by
    """
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs = df[x]
    ys = df[y]
    zs = df[z]

    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    ax.set_title(f"{country} Transactions Only")

    ax.scatter(xs, ys, zs)

    picture = io.BytesIO()
    plt.savefig(picture, format='png')
    
    return picture

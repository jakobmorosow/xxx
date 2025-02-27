import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Erstelle ein 3D-Plot für die Weltkarte
def plot_3d_world():
    # Erstelle Daten für eine Kugeloberfläche
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    # Erstelle ein 3D-Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot der Kugel
    ax.plot_surface(x, y, z, color='b', alpha=0.6)

    # Beschriftung
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Zeige die Plot-Oberfläche
    plt.title("3D-Weltmodell aus Zahlen")
    plt.show()

if __name__ == "__main__":
    plot_3d_world()

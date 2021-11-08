import numpy as np
import matplotlib.pyplot as plt

def plot_predictions(xtrain,y_true, y_pred):  
    f, ax = plt.subplots(3, 5)
    f.set_size_inches(10.5,7.5)
    for i in range(5):
        ax[0][i].imshow(np.reshape(xtrain[i], (96,96)),cmap="gray")
        ax[1][i].imshow(np.reshape(y_true[i], (96,96)),cmap="gray")
        ax[2][i].imshow(np.reshape(y_pred[i], (96,96)),cmap="gray")
    plt.tight_layout()
import matplotlib.pyplot as plt

def plot_img(image):
  f,ax=plt.subplots(1,5)
  f.set_size_inches(40,20)
  for i in range(0,5):
    ax[i].imshow(image[i].reshape(96,96),cmap='gray')
  plt.show()
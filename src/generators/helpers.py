from ipywidgets import interact, IntSlider
import matplotlib.pyplot as plt

def interactive_slicer(volume):
    @interact(
        x=IntSlider(min=0, max=volume.shape[0]-1, step=1, value=volume.shape[0]//2, 
                   description='X slice'),
        y=IntSlider(min=0, max=volume.shape[1]-1, step=1, value=volume.shape[1]//2,
                   description='Y slice'),
        z=IntSlider(min=0, max=volume.shape[2]-1, step=1, value=volume.shape[2]//2,
                   description='Z slice')
    )
    def show_slice(x, y, z):
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        axes[0].imshow(volume[x, :, :], cmap='gray', vmin=0, vmax=255)
        axes[0].set_title(f'Slice X={x}')
        
        axes[1].imshow(volume[:, y, :], cmap='gray', vmin=0, vmax=255)
        axes[1].set_title(f'Slice Y={y}')
        
        axes[2].imshow(volume[:, :, z], cmap='gray', vmin=0, vmax=255)
        axes[2].set_title(f'Slice Z={z}')
        
        plt.tight_layout()
        plt.show()
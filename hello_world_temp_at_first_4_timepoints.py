# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
import seaborn as sns
import xarray as xr
import sys

# %%
# Short Description:
# Make 4 plots that show temperature of world at first 4 timepoints in dataset
#  This resembles (0:00, 6:00, 12:00, 18:00 in my first sandbox dataset)

# %%
def figa(figs_plotted):
    figs_plotted += 1
    plt.figure(figs_plotted)
    return figs_plotted

# %%
#path="../datasets/c2w_training_data/data/hadgem_debiased/gen_sample_001.nc"
path="../datasets/c2w_training_data/data/hadgem_debiased/observation.nc"
ds = xr.open_dataset(path)
print('Second plot')
print('First plots done again, but smarter! \n plot temperature for different times of day!')


# %%

f, axarr = plt.subplots(2,2)
# use the created array to output your multiple images. In this case I have stacked 4 images vertically
kelcel_const = 273.15
im1 = (ds.t2m.isel(time=0) - kelcel_const).plot.imshow(ax=axarr[0][0],x='longitude', vmin=-40, vmax=40)
im2 = (ds.t2m.isel(time=1) - kelcel_const).plot.imshow(ax=axarr[0][1],x='longitude', vmin=-40, vmax=40)
im3 = (ds.t2m.isel(time=2) - kelcel_const).plot.imshow(ax=axarr[1][0],x='longitude', vmin=-40, vmax=40)
im4 = (ds.t2m.isel(time=3) - kelcel_const).plot.imshow(ax=axarr[1][1],x='longitude', vmin=-40, vmax=40)
#im2 = axarr[0][1].imshow(ds.isel(time=1).to_array()[0,:,:] - 273.3, vmin=-40, vmax=40)
axarr[0][0].title.set_text('Daytime = 0:00')
axarr[0][1].title.set_text('Daytime = 6:00')
axarr[1][0].title.set_text('Daytime = 12:00')
axarr[1][1].title.set_text('Daytime = 18:00')


# %%
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig('figs/Temperature_at_2m_in_C_in_2009-01-01_for_different_times_of_the_day_smarter_plotted.png')
plt.show()

# %%

print("script finished")



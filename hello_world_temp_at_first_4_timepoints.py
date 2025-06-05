# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('Qt5Agg')
import seaborn as sns
import xarray as xr
import sys

# %%
# Short Description:
# Goal: Analyze Jonathans Data
# Make 4 plots that show temperature of jonathans training data for  4 different sizes 
# for both observation and gen_sample data
#  

# %%
def figa(figs_plotted):
    figs_plotted += 1
    plt.figure(figs_plotted)
    return figs_plotted

# %%
path_sa="../datasets/c2w_training_data/data/hadgem_debiased/gen_sample_001.nc"
path_ob="../datasets/c2w_training_data/data/hadgem_debiased/observation.nc"
ds_ob = xr.open_dataset(path_ob)
ds_sa = xr.open_dataset(path_sa)
print('Second plot')
print('First plots done again, but smarter! \n plot temperature for different times of day!')


# %%

f, axarr = plt.subplots(2,2)
# use the created array to output your multiple images. In this case I have stacked 4 images vertically
kelcel_const = 273.15
im1 = (ds_sa.tas.isel(time=0) - kelcel_const).plot.imshow(ax=axarr[0][0],x='rlon', )
im2 = (ds_sa.psl.isel(time=0) - kelcel_const).plot.imshow(ax=axarr[0][1],x='rlon', )
im3 = (ds_sa.uas.isel(time=0) - kelcel_const).plot.imshow(ax=axarr[1][0],x='rlon', )
im4 = (ds_sa.vas.isel(time=0) - kelcel_const).plot.imshow(ax=axarr[1][1],x='rlon', )
#im2 = axarr[0][1].imshow(ds.isel(time=1).to_array()[0,:,:] - 273.3, vmin=-40, vmax=40)
axarr[0][0].title.set_text('tas (temp at sea level)')
axarr[0][1].title.set_text('psl (pressure at sea level)')
axarr[1][0].title.set_text('uas (zonal wind component)')
axarr[1][1].title.set_text('vas (meridional wind component)')
plt.suptitle('Sample data plotted for 4 different variables')

# %%
plt.figure(2)
f, axarr = plt.subplots(2,2)
# use the created array to output your multiple images. In this case I have stacked 4 images vertically
kelcel_const = 273.15
im1 = (ds_ob.tas.isel(time=0) - kelcel_const).plot.imshow(ax=axarr[0][0],x='rlon', )
im2 = (ds_ob.psl.isel(time=0) - kelcel_const).plot.imshow(ax=axarr[0][1],x='rlon', )
im3 = (ds_ob.uas.isel(time=0) - kelcel_const).plot.imshow(ax=axarr[1][0],x='rlon', )
im4 = (ds_ob.vas.isel(time=0) - kelcel_const).plot.imshow(ax=axarr[1][1],x='rlon', )
#im2 = axarr[0][1].imshow(ds.isel(time=1).to_array()[0,:,:] - 273.3, vmin=-40, vmax=40)
axarr[0][0].title.set_text('tas (temp at sea level)')
axarr[0][1].title.set_text('psl (pressure at sea level)')
axarr[1][0].title.set_text('uas (zonal wind component)')
axarr[1][1].title.set_text('vas (meridional wind component)')
plt.suptitle('Observation data plotted for 4 different variables')

# %%

#plt.savefig('figs/Temperature_at_2m_in_C_in_2009-01-01_for_different_times_of_the_day_smarter_plotted.png')
plt.show()

# %%

print("script finished")



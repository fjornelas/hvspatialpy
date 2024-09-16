## Documentation for Functions in `hvspatialpy.py`

### `_plot_intervals(ax1, freq, mean_ref, min_freq, max_freq, freq_trun=0.1)`

### Description
Plots the frequency intervals of the reference HVSR (Horizontal to Vertical Spectral Ratio).

### Parameters
- **ax1** (`matplotlib.axes.Axes`): The axis object on which to plot the intervals.
- **freq** (`numpy.ndarray`): Frequency values.
- **mean_ref** (`numpy.ndarray`): Mean HVSR reference values.
- **min_freq** (`list[float]`): List of minimum frequencies for intervals.
- **max_freq** (`list[float]`): List of maximum frequencies for intervals.
- **freq_trun** (`float`, optional): Frequency to truncate the HVSR mean curve. Default is `0.1`.

### Returns
None. This function displays a plot.

---

### `_update_colorbar(ax, cbar, scatter, correlation_type='lcss')`

### Description
Updates the colorbar with the latest scatter plot and label.

### Parameters
- **ax** (`matplotlib.axes.Axes`): The axis object associated with the colorbar.
- **cbar** (`matplotlib.colorbar.Colorbar`): The colorbar object to be updated.
- **scatter** (`matplotlib.collections.PathCollection`): The scatter plot object.
- **correlation_type** (`str`, optional): The type of correlation to be displayed in the colorbar label. Default is `'lcss'`.

### Returns
None. This function updates the colorbar.

---

### `_plot_site_image(ax2, df_site, correlation_type='lcss', frequency_interval=None)`

### Description
Plots site data on top of a topographic relief map using EPSG:4326 coordinates.

### Parameters
- **ax2** (`matplotlib.axes.Axes`): The axis object on which to plot the site data.
- **df_site** (`pandas.DataFrame`): DataFrame containing 'longitude', 'latitude', and 'correlation_value'.
- **correlation_type** (`str`, optional): Type of correlation value (used for colorbar label). Default is `'lcss'`.
- **frequency_interval** (`int`, optional): Optional frequency interval to filter the data.

### Returns
`matplotlib.figure.Figure` object: The figure used for plotting.

---

### `_update_dataframe(base_dir, site, num_peaks, min_freq, max_freq)`

### Description
Updates the frequency interval DataFrame with the given parameters.

### Parameters
- **base_dir** (`str`): Base directory path where the site and test files are stored.
- **site** (`int`): Site test number.
- **num_peaks** (`int`): Number of peaks within the HVSR curve.
- **min_freq** (`list[float]`): List of minimum frequencies of the intervals.
- **max_freq** (`list[float]`): List of maximum frequencies of the intervals.

### Returns
`pandas.DataFrame`: Updated DataFrame of the frequency intervals.

---

### `update_correlations(base_dir, site, xml_folder_name, unique_folder_name, ref_test_name, mean_file_name, unique_flag=True, auto_dist_calc_flag=True, freq_trun=0.1, dist_meas_df=None, loc_df_manual=None, correlation_type='lcss', frequency_interval=None, threshold=1.6, min_distance=1, global_constraint='sakoe_chiba', eps=0.75, sakoe_chiba_radius=10, dist_range_list=None)`

### Description
Updates the correlation plot when different input parameters change and provides interactive widgets to modify frequency intervals.

### Parameters
- **base_dir** (`str`): Base directory where all the tests are stored.
- **site** (`str`): Site name where the tests for that site are stored.
- **xml_folder_name** (`str`): Folder name where XML files are relative to site and tests.
- **unique_folder_name** (`str`): Unique path where files are stored.
- **ref_test_name** (`str`): Name of the reference test.
- **mean_file_name** (`str`): Filename used for the mean HVSR curve.
- **unique_flag** (`bool`, optional): Indicates if the folder scheme is unique. Default is `True`.
- **auto_dist_calc_flag** (`bool`, optional): Indicates whether to use XML files or CSV file for identifying locations. Default is `True`.
- **freq_trun** (`float`, optional): Frequency to truncate the HVSR mean curve. Default is `0.1`.
- **dist_meas_df** (`str`, optional): Path to the distance measured DataFrame (.csv). Default is `None`.
- **loc_df_manual** (`str`, optional): Path to the location DataFrame (.csv). Default is `None`.
- **correlation_type** (`str`, optional): Type of correlation used in the analysis. Default is `'lcss'`.
- **frequency_interval** (`int`, optional): Frequency interval to filter the data. Default is `None`.
- **threshold** (`float`, optional): Matching threshold used in 'lcss' correlation. Default is `1.6`.
- **min_distance** (`int`, optional): Minimum distance between peaks. Default is `1`.
- **global_constraint** (`str`, optional): Constraint type for correlation. Default is `'sakoe_chiba'`.
- **eps** (`float`, optional): Matching threshold used in 'lcss' correlation. Default is `0.75`.
- **sakoe_chiba_radius** (`int`, optional): Radius of warping window. Default is `10`.
- **dist_range_list** (`str`, optional): String of tuple list to evaluate different distance ranges. Default is `None`.

### Returns
- `pandas.DataFrame`: Frequency DataFrame.
- `pandas.DataFrame`: Correlation DataFrame.
- `matplotlib.figure.Figure`: The figure used in the analysis.


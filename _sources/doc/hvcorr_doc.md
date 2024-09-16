# hvspatialpy: Functions for Evaluating Spatial Variability

This module is part of `hvspatialpy`, a Python package designed for evaluating the spatial variability of sites using spatially distributed HVSR (Horizontal-to-Vertical Spectral Ratio) measurements.

**Author**: Francisco Javier Ornelas (jornela1@g.ucla.edu)  
**Copyright**: (c) 2024

## Functions

### `_find_peaks`

Find peaks in a 1D array.

#### Parameters
- **y** (`array`): The input data array.
- **threshold** (`float`): Minimum value for peaks. Default is `1.6`.
- **min_distance** (`int`): Minimum number of points between peaks. Default is `1`.

#### Returns
- **peaks** (`list`): Indices of the peaks in the array.

---

### `_find_troughs`

Find troughs (local minima) in a 1D array.

#### Parameters
- **y** (`array`): The input data array.

#### Returns
- **troughs** (`list`): Indices of the troughs in the array.

---

### `_find_nearest_trough`

Find the indices where a peak and two troughs are identified.

#### Parameters
- **y** (`array`): Input array.
- **threshold** (`float`): Minimum amplitude threshold. Default is `1.6`.
- **min_distance** (`int`): Minimum number of points between peaks. Default is `1`.

#### Returns
- **left_troughs** (`numpy.ndarray`): Indices of left troughs for each peak.
- **right_troughs** (`numpy.ndarray`): Indices of right troughs for each peak.
- **peaks** (`numpy.ndarray`): Indices of peaks.
- **troughs** (`list`): Indices of troughs.

---

### `_compute_dist`

Compute distance between two geographical points using the Haversine formula.

#### Parameters
- **lat_meas** (`float`): Latitude of the measured point.
- **lat_ref** (`float`): Latitude of the reference point.
- **long_meas** (`float`): Longitude of the measured point.
- **long_ref** (`float`): Longitude of the reference point.
- **r** (`float`): Radius of the Earth in kilometers. Default is `6373.0`.

#### Returns
- **distance** (`float`): Distance between the reference and measured point in meters.

---

### `_get_locations`

Retrieve location data from XML files and return a DataFrame with test names, latitudes, and longitudes.

#### Parameters
- **base_dir** (`str`): The base directory containing site-specific folders.
- **site** (`str`): The site number to navigate to.
- **xml_folder_name** (`str`): The folder name containing the XML files.

#### Returns
- **loc_df** (`pandas.DataFrame`): DataFrame with columns 'tests', 'latitude', and 'longitude'.

---

### `dist_from_vert_arr`

Compute distances from a reference location to all other locations.

#### Parameters
- **base_dir** (`str`): The base directory containing site-specific folders.
- **site** (`str`): The site number to navigate to.
- **xml_folder_name** (`str`): The folder name containing the XML files.

#### Returns
- **loc_df** (`pandas.DataFrame`): DataFrame with 'tests' and 'distance' columns.

---

### `create_frequency_dataframe`

Create a DataFrame with frequency data from directories and provide an interactive plot for manual adjustment.

#### Parameters
- **base_dir** (`str`): The base directory where the site directories are located.
- **site** (`str`): The specific site directory to process.
- **freq** (`list`): List of frequency values.
- **mean_arr** (`ndarray`): Array containing mean frequency values for identifying intervals.

#### Returns
- **freq_df** (`pandas.DataFrame`): DataFrame containing the site, test, and frequency intervals.

---

### `compute_correlations`

Evaluate the correlation of various spatially distributed HVSR curves at a site.

#### Parameters
- **base_dir** (`str`): The base directory where all the tests are stored.
- **site** (`str`): The site name where the tests are stored.
- **freq_df** (`pandas.DataFrame`): DataFrame with frequency interval information.
- **xml_folder_name** (`str`): The folder name containing the XML files.
- **unique_folder_name** (`str`): The unique path where files are stored.
- **ref_test_name** (`str`): Name of the reference test.
- **mean_file_name** (`str`): Filename used for the mean HVSR curve.
- **unique_flag** (`bool`): Indicates if the folder scheme is unique. Default is `True`.
- **auto_dist_calc_flag** (`bool`): Indicates whether to use XML files to identify test point locations. Default is `True`.
- **correlation_type** (`str`): Type of correlation used in the analysis. Default is `'lcss'`.
- **dist_meas_df** (`str`): Path to the distance measured DataFrame (.csv). Optional.
- **loc_df_manual** (`str`): Path to the location DataFrame (.csv). Optional.
- **global_constraint** (`str`): String indicating the use of a warping window or slope constraint. Default is `'sakoe_chiba'`.
- **eps** (`float`): Matching threshold for 'lcss' correlation. Default is `0.75`.
- **sakoe_chiba_radius** (`int`): Radius of warping window for 'lcss' and 'dtw'. Default is `10`.
- **dist_range_list** (`str`): String of tuple list for different distance ranges. Optional.

#### Returns
- **df_all** (`pandas.DataFrame`): DataFrame indicating correlation values, distances, and locations.

---

## Notes

- Ensure that all file paths and directory names are correctly specified when using these functions.
- For correlation calculations, the `scipy` and `tslearn` libraries are used, which may need to be installed separately.


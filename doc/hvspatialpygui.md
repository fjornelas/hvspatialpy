## `HVSpatialPYGui` Class Documentation

## Overview

The `HVSpatialPYGui` class provides a graphical user interface (GUI) to evaluate the spatial variability of a site using Horizontal-to-Vertical Spectral Ratio (HVSR) data. This class allows users to interactively adjust various parameters and visualize the results of spatial correlation analyses.

## Class Definition

## `HVSpatialPYGui`

Description:
- A Python graphical user interface (GUI) to evaluate the spatial variability of a site utilizing HVSR.

Parameters:
- **dist_range_list_widget**: `str`
  - String of tuple list to evaluate different distance ranges used in the study.
- **sakoe_chiba_radius_widget**: `int`
  - Radius of the warping window to allow horizontal shift between different points in a curve. Note: applicable only for 'lcss' and 'dtw'.
- **eps_widget**: `float`
  - Matching threshold used in 'lcss' correlation. Note: applicable only for 'lcss'.
- **global_constraint_widget**: `str`
  - String indicating whether to use Sakoe-Chiba radius or Itakura slope. Note: applicable only for 'lcss' and 'dtw'.
- **loc_df_manual_widget**: `str`
  - Path where the location dataframe (.csv) is stored, showing true locations of the test points. Note: only use if the auto flag is not working.
- **dist_meas_df_widget**: `str`
  - Path where the distance measured dataframe (.csv) is stored, showing distances from the reference. Note: only use if the auto flag is not working.
- **auto_dist_calc_flag_widget**: `boolean`
  - Indicates whether to use .xml files to identify locations of test points or a .csv file (False).
- **unique_flag_widget**: `boolean`
  - Indicates if the folder scheme is unique, meaning additional folders are needed for computation. Use `unique_folder_name` if this is true.
- **mean_file_name_widget**: `str`
  - Filename used for the mean HVSR curve.
- **ref_test_name_widget**: `str`
  - Name of the reference test.
- **unique_folder_name_widget**: `str`
  - Unique path where files are stored.
- **freq_df_widget**: `dataframe`
  - Dataframe where frequency interval information is stored.
- **base_dir_widget**: `str`
  - Base directory where all the tests are stored.
- **site_widget**: `str`
  - Site name where the tests for that site are stored.
- **xml_folder_name_widget**: `str`
  - Folder name where the XML files are relative to site and tests.
- **correlation_type_widget**: `str`
  - Type of correlation used in the analysis.

Returns:
- Frequency and correlation dataframes, and the figure used in the analysis.

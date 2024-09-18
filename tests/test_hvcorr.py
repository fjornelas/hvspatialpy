import pytest
import os
import numpy as np
import pandas as pd
from unittest.mock import patch
from hvspatialpy.hvcorr import (
    _find_peaks, _find_troughs, _find_nearest_trough, _compute_dist, _get_locations,
    dist_from_vert_arr, create_frequency_dataframe, compute_correlations
)


def test_find_peaks():
    y = np.array([0, 1, 0, 2, 0, 3, 0])
    expected_peaks = [3, 5]
    print(_find_peaks(y))
    assert _find_peaks(y) == expected_peaks


def test_find_troughs():
    y = np.array([3, 1, 2, 0, 1, 0, 1])
    expected_troughs = [1, 3, 5]
    assert _find_troughs(y) == expected_troughs


def test_find_nearest_trough():
    y = np.array([3, 1, 2, 0, 1, 0, 1])
    left_troughs, right_troughs, peaks, troughs = _find_nearest_trough(y)
    expected_left_troughs = [1]
    expected_right_troughs = [3]
    expected_peaks = [2]
    expected_troughs = [1, 3, 5]

    assert np.array_equal(left_troughs, expected_left_troughs)
    assert np.array_equal(right_troughs, expected_right_troughs)
    assert np.array_equal(peaks, expected_peaks)
    assert np.array_equal(troughs, expected_troughs)


def test_compute_dist():
    lat_meas, lat_ref, long_meas, long_ref = 34.05, 34.05, -118.25, -118.25
    expected_distance = 0.0
    assert _compute_dist(lat_meas, lat_ref, long_meas, long_ref) == pytest.approx(expected_distance)


def test_get_locations():
    # Define the path to the test data directory
    base_dir = os.path.join(os.path.dirname(__file__), '../examples/data')
    site = '7' 
    xml_folder_name = '7.0.0' 

    # Prepare the expected DataFrame
    expected_data = {
        'tests': ['test1', 'test2'],
        'latitude': [34.05, 35.05],
        'longitude': [-118.25, -117.25]
    }
    expected_df = pd.DataFrame(expected_data)

    # Call the function under test
    result_df = _get_locations(base_dir, site, xml_folder_name)

    # Assert the result DataFrame matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_dist_from_vert_arr():
    base_dir = os.path.join(os.path.dirname(__file__), '../examples/data')
    site = '7' 
    xml_folder_name = '7.0.0' 

    # Prepare test data
    test_data = {
        'tests': ['test1', 'test2'],
        'latitude': [34.05, 35.05],
        'longitude': [-118.25, -117.25]
    }
    loc_df = pd.DataFrame(test_data)

    # Mock the `_get_locations` function
    with patch('hvspatialpy.hvcorr._get_locations') as mock_get_locations:
        mock_get_locations.return_value = loc_df
        
        # Mock the `_compute_dist` function
        with patch('hvspatialpy.hvcorr._compute_dist') as mock_compute_dist:
            mock_compute_dist.return_value = 1000
            
            # Call the function under test
            result_df = dist_from_vert_arr(base_dir, site, xml_folder_name)

            # Prepare expected output
            expected_data = {
                'tests': ['test1', 'test2'],
                'latitude': [34.05, 35.05],
                'longitude': [-118.25, -117.25],
                'distance': [1000, 1000]
            }
            expected_df = pd.DataFrame(expected_data)

            # Assert the result DataFrame matches the expected DataFrame
            pd.testing.assert_frame_equal(result_df, expected_df)

def test_create_frequency_dataframe():
    base_dir = os.path.join(os.path.dirname(__file__), '../examples/data')
    site = '7' 
    freq = pd.read_csv(os.path.join(os.path.dirname(__file__), '../examples/data/7.0.0/Test_hvsr_mean.csv')['freq_Hz'] 
    mean_arr = pd.read_csv(os.path.join(os.path.dirname(__file__), '../examples/data/7.0.0/Test_hvsr_mean.csv')['HVSR mean'] 

    # Prepare expected output
    expected_data = {
        'site': ['site1'],
        'tests': ['test1'],
        'numPeaks': [2],
        'freq_int_0_min': [0.1],
        'freq_int_0_max': [0.2],
        'freq_int_1_min': [0.3],
        'freq_int_1_max': [0.4]
    }
    expected_df = pd.DataFrame(expected_data)

    # Mock the `create_frequency_dataframe` function
    with patch('hvspatialpy.hvcorr.create_frequency_dataframe') as mock_create_frequency_dataframe:
        mock_create_frequency_dataframe.return_value = expected_df
        
        # Call the function under test
        result_df = create_frequency_dataframe(base_dir, site, freq, mean_arr)
        
        # Assert the result DataFrame matches the expected DataFrame
        pd.testing.assert_frame_equal(result_df, expected_df)

def test_compute_correlations():
    
    base_dir = os.path.join(os.path.dirname(__file__), '../examples/data')
    site = '7' 
    freq_df = pd.DataFrame({
        'site': ['site1'],
        'tests': ['test1'],
        'numPeaks': [2],
        'freq_int_0_min': [0.1],
        'freq_int_0_max': [0.2],
        'freq_int_1_min': [0.3],
        'freq_int_1_max': [0.4]
    })
    xml_folder_name = 'xml'
    unique_folder_name = 'unique'
    ref_test_name = 'ref_test'
    mean_file_name = 'mean.csv'

    # Prepare expected output
    expected_data = {
        'tests': ['test1'],
        'freq_interval': [0],
        'distance_bin': [0],
        'correlation_value': [0]
    }
    expected_df = pd.DataFrame(expected_data)

    # Mock the `compute_correlations` function
    with patch('hvspatialpy.hvcorr.compute_correlations') as mock_compute_correlations:
        mock_compute_correlations.return_value = expected_df
        
        # Call the function under test
        result_df = compute_correlations(base_dir, site, freq_df, xml_folder_name, unique_folder_name,
                                         ref_test_name, mean_file_name)
        
        # Assert the result DataFrame matches the expected DataFrame
        pd.testing.assert_frame_equal(result_df, expected_df)

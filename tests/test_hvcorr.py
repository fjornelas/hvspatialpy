import pytest
import numpy as np
import pandas as pd
from hvspatialpy.hvcorr import (
    _find_peaks, _find_troughs, _find_nearest_trough, _compute_dist, _get_locations,
    dist_from_vert_arr, create_frequency_dataframe, compute_correlations
)


def test_find_peaks():
    y = np.array([0, 1, 0, 2, 0, 3, 0])
    expected_peaks = [1, 5]
    assert _find_peaks(y) == expected_peaks


def test_find_troughs():
    y = np.array([3, 1, 2, 0, 1, 0, 1])
    expected_troughs = [3, 5]
    assert _find_troughs(y) == expected_troughs


def test_find_nearest_trough():
    y = np.array([3, 1, 2, 0, 1, 0, 1])
    left_troughs, right_troughs, peaks, troughs = _find_nearest_trough(y)
    expected_left_troughs = [3, 5]
    expected_right_troughs = [5, 7]
    expected_peaks = [2, 5]
    expected_troughs = [3, 5]

    assert np.array_equal(left_troughs, expected_left_troughs)
    assert np.array_equal(right_troughs, expected_right_troughs)
    assert np.array_equal(peaks, expected_peaks)
    assert np.array_equal(troughs, expected_troughs)


def test_compute_dist():
    lat_meas, lat_ref, long_meas, long_ref = 34.05, 34.05, -118.25, -118.25
    expected_distance = 0.0
    assert _compute_dist(lat_meas, lat_ref, long_meas, long_ref) == pytest.approx(expected_distance)


def test_get_locations():
    # Mock the `_get_locations` function since it relies on file I/O
    base_dir = 'test_data'
    site = 'site1'
    xml_folder_name = 'xml'

    # Prepare test data
    test_data = {
        'tests': ['test1', 'test2'],
        'latitude': [34.05, 35.05],
        'longitude': [-118.25, -117.25]
    }

    # Create DataFrame
    expected_df = pd.DataFrame(test_data)

    # Assuming `_get_locations` is mocked and will return `expected_df`
    result_df = _get_locations(base_dir, site, xml_folder_name)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_dist_from_vert_arr():
    # Mock the `_get_locations` function used in `dist_from_vert_arr`
    base_dir = 'test_data'
    site = 'site1'
    xml_folder_name = 'xml'

    # Prepare test data
    test_data = {
        'tests': ['test1', 'test2'],
        'latitude': [34.05, 35.05],
        'longitude': [-118.25, -117.25]
    }

    # Mock location DataFrame
    loc_df = pd.DataFrame(test_data)

    # Mock the `_compute_dist` function
    def mock_compute_dist(lat_meas, lat_ref, long_meas, long_ref, r=6373.0):
        return 1000  # Mock distance value

    # Prepare expected output
    expected_data = {
        'tests': ['test1', 'test2'],
        'latitude': [34.05, 35.05],
        'longitude': [-118.25, -117.25],
        'distance': [1000, 1000]
    }
    expected_df = pd.DataFrame(expected_data)

    # Mock function call
    result_df = dist_from_vert_arr(base_dir, site, xml_folder_name)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_create_frequency_dataframe():
    # Test input data
    base_dir = 'test_data'
    site = 'site1'
    freq = [0.1, 0.2, 0.3, 0.4, 0.5]
    mean_arr = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

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
    result_df = create_frequency_dataframe(base_dir, site, freq, mean_arr)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_compute_correlations():
    # This function requires a more complex setup including mock files or valid data

    # Define parameters
    base_dir = 'test_data'
    site = 'site1'
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

    # Mock the `compute_correlations` function
    result_df = compute_correlations(base_dir, site, freq_df, xml_folder_name, unique_folder_name,
                                     ref_test_name, mean_file_name)

    # Prepare expected output
    expected_data = {
        'tests': ['test1'],
        'freq_interval': [0],
        'distance_bin': [0],
        'correlation_value': [0]
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result_df, expected_df)

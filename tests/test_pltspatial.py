import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from hvspatialpy.pltspatial import update_correlations, _update_dataframe, _plot_intervals, _update_colorbar, _plot_site_image
from unittest.mock import patch, MagicMock

@pytest.fixture
def setup_params():
    """Fixture to setup common parameters for the tests."""
    return {
        'base_dir': '/path/to/base_dir',
        'site': 'test_site',
        'xml_folder_name': 'xml_folder',
        'unique_folder_name': 'unique_folder',
        'ref_test_name': 'ref_test',
        'mean_file_name': 'mean_file.csv',
        'unique_flag': True,
        'auto_dist_calc_flag': True,
        'freq_trun': 0.1,
        'dist_meas_df': None,
        'loc_df_manual': None,
        'correlation_type': 'lcss',
        'frequency_interval': None,
        'threshold': 1.6,
        'min_distance': 1,
        'global_constraint': 'sakoe_chiba',
        'eps': 0.75,
        'sakoe_chiba_radius': 10,
        'dist_range_list': None
    }

@patch('hvspatialpy.pd.read_csv')
def test_update_correlations(mock_read_csv, setup_params):
    """Test the update_correlations function."""
    # Mock read_csv return value
    mock_read_csv.return_value = pd.DataFrame({
        0: [0.1, 0.2, 0.3],
        1: [1.0, 2.0, 3.0]
    })

    # Call the function
    params = setup_params
    df, df_all, fig = update_correlations(
        base_dir=params['base_dir'],
        site=params['site'],
        xml_folder_name=params['xml_folder_name'],
        unique_folder_name=params['unique_folder_name'],
        ref_test_name=params['ref_test_name'],
        mean_file_name=params['mean_file_name'],
        unique_flag=params['unique_flag'],
        auto_dist_calc_flag=params['auto_dist_calc_flag'],
        freq_trun=params['freq_trun'],
        dist_meas_df=params['dist_meas_df'],
        loc_df_manual=params['loc_df_manual'],
        correlation_type=params['correlation_type'],
        frequency_interval=params['frequency_interval'],
        threshold=params['threshold'],
        min_distance=params['min_distance'],
        global_constraint=params['global_constraint'],
        eps=params['eps'],
        sakoe_chiba_radius=params['sakoe_chiba_radius'],
        dist_range_list=params['dist_range_list']
    )

    # Check the outputs
    assert isinstance(df, pd.DataFrame)
    assert isinstance(df_all, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

def test_update_dataframe():
    """Test the _update_dataframe function."""
    # Create mock input data
    base_dir = '/path/to/base_dir'
    site = 'site1'
    num_peaks = 3
    min_freq = [0.1, 0.2, 0.3]
    max_freq = [0.15, 0.25, 0.35]

    # Call the function
    df = _update_dataframe(
        base_dir=base_dir,
        site=site,
        num_peaks=num_peaks,
        min_freq=min_freq,
        max_freq=max_freq
    )

    # Check the dataframe
    assert df.shape[0] == len(min_freq)
    assert 'site' in df.columns
    assert 'tests' in df.columns
    assert 'numPeaks' in df.columns
    for i in range(len(min_freq)):
        assert f'freq_int_{i}_min' in df.columns
        assert f'freq_int_{i}_max' in df.columns

@patch('hvspatialpy.plt.show')
def test_plot_intervals(mock_show):
    """Test the _plot_intervals function."""
    fig, ax1 = plt.subplots()
    freq = np.array([0.1, 0.2, 0.3])
    mean_ref = np.array([1.0, 2.0, 3.0])
    min_freq = [0.1]
    max_freq = [0.2]
    freq_trun = 0.05

    # Call the function
    _plot_intervals(ax1, freq, mean_ref, min_freq, max_freq, freq_trun)

    # Check that plot functions are called
    assert ax1.get_legend() is not None

@patch('hvspatialpy.plt.colorbar')
@patch('hvspatialpy.plt.gca')
def test_update_colorbar(mock_gca, mock_colorbar):
    """Test the _update_colorbar function."""
    fig, ax = plt.subplots()
    cbar = MagicMock()
    scatter = MagicMock()

    # Call the function
    _update_colorbar(ax, cbar, scatter, correlation_type='lcss')

    # Check that colorbar was called with correct parameters
    mock_colorbar.assert_called_once()

@patch('hvspatialpy.plt.show')
def test_plot_site_image(mock_show):
    """Test the _plot_site_image function."""
    fig, ax2 = plt.subplots()
    df_site = pd.DataFrame({
        'longitude': [1.0, 2.0, 3.0],
        'latitude': [4.0, 5.0, 6.0],
        'correlation_value': [0.1, 0.2, 0.3]
    })
    correlation_type = 'lcss'
    frequency_interval = None

    # Call the function
    _plot_site_image(ax2, df_site, correlation_type, frequency_interval)

    # Check that plot functions are called
    assert ax2.get_legend() is not None

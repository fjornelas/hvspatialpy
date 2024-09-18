import pytest
from unittest.mock import patch, MagicMock
import os
from hvspatialpy.hvspatialpygui import HVSpatialPYGui

def test_on_button_click(mock_savefig, mock_to_csv, mock_makedirs, mock_update_correlations):
    """
    Test the on_button_click method of HVSpatialPYGui.
    """
    # Create a mock object for the update_correlations function
    mock_update_correlations.return_value = (
        MagicMock(),  # Mock DataFrame for freq_int_df
        MagicMock(),  # Mock DataFrame for correlation_df
        MagicMock()  # Mock Figure for the plot
    )

    # Create an instance of HVSpatialPYGui
    gui = HVSpatialPYGui()

    # Set widget values
    gui.base_dir_widget.value = '/mock/base/dir'
    gui.site_widget.value = 'test_site'
    gui.xml_folder_name_widget.value = 'xml_folder'
    gui.unique_folder_name_widget.value = 'unique_folder'
    gui.ref_test_name_widget.value = 'ref_test'
    gui.mean_file_name_widget.value = 'mean_file.csv'
    gui.unique_flag_widget.value = True
    gui.auto_dist_calc_flag_widget.value = True
    gui.freq_trun_widget.value = 0.1
    gui.threshold_widget.value = 1.6
    gui.min_distance_widget.value = 1.0
    gui.correlation_type_widget.value = 'lcss'
    gui.frequency_interval_widget.value = 0
    gui.global_constraint_widget.value = 'sakoe_chiba'
    gui.eps_widget.value = 0.75
    gui.sakoe_chiba_radius_widget.value = 10
    gui.dist_range_list_widget.value = '[[0, 75], [75, 300], [300, 600], [600, 1000]]'
    gui.dist_meas_df_widget.value = '/mock/dist/meas/path.csv'
    gui.loc_df_manual_widget.value = '/mock/loc/path.csv'
    gui.save_dir_widget.value = '/mock/save/dir'

    # Mock button click event
    mock_button = MagicMock()
    gui.on_button_click(mock_button)

    # Assert update_correlations was called with the correct parameters
    mock_update_correlations.assert_called_once_with(
        base_dir='/mock/base/dir',
        site='test_site',
        xml_folder_name='xml_folder',
        unique_folder_name='unique_folder',
        ref_test_name='ref_test',
        mean_file_name='mean_file.csv',
        unique_flag=True,
        auto_dist_calc_flag=True,
        freq_trun=0.1,
        dist_meas_df='/mock/dist/meas/path.csv',
        loc_df_manual='/mock/loc/path.csv',
        correlation_type='lcss',
        frequency_interval=0,
        threshold=1.6,
        min_distance=1.0,
        global_constraint='sakoe_chiba',
        eps=0.75,
        sakoe_chiba_radius=10,
        dist_range_list='[[0, 75], [75, 300], [300, 600], [600, 1000]]'
    )

    # Assert os.makedirs was called to create the save directory
    mock_makedirs.assert_called_once_with('/mock/save/dir')

    # Assert DataFrames to_csv method was called with the correct file paths
    mock_to_csv.assert_any_call('/mock/save/dir/frequency_interval_df.csv', index=False)
    mock_to_csv.assert_any_call('/mock/save/dir/correlation_df.csv', index=False)

    # Assert Figure savefig method was called with the correct file path
    mock_savefig.assert_called_once_with('/mock/save/dir/spatial_figure.png', dpi=500)


def test_widget_initial_values():
    """
    Test the initial values of widgets in HVSpatialPYGui.
    """
    gui = HVSpatialPYGui()

    # Check initial widget values
    assert gui.base_dir_widget.value == 'C:/Users/Javier Ornelas/OneDrive/Documents/HVSRdata_Main/mHVSR Site Inv/VSPDB Data/CA Vertical Array Data/HVSRdata'
    assert gui.site_widget.value == '7'
    assert gui.xml_folder_name_widget.value == 'Raw_mseed_data'
    assert gui.unique_folder_name_widget.value == 'Text_File_data/Raw_ascii_PEG_HH'
    assert gui.ref_test_name_widget.value == '7.0.0'
    assert gui.mean_file_name_widget.value == 'Test_hvsr_mean.csv'
    assert gui.unique_flag_widget.value == True
    assert gui.auto_dist_calc_flag_widget.value == True
    assert gui.freq_trun_widget.value == 0.1
    assert gui.threshold_widget.value == 1.6
    assert gui.min_distance_widget.value == 1.0
    assert gui.correlation_type_widget.value == 'lcss'
    assert gui.global_constraint_widget.value == 'sakoe_chiba'
    assert gui.eps_widget.value == 0.75
    assert gui.dist_range_list_widget.value == '[[0, 75], [75, 300], [300, 600], [600, 1000]]'
    assert gui.frequency_interval_widget.value == 0
    assert gui.sakoe_chiba_radius_widget.value == 10
    assert gui.dist_meas_df_widget.value == 'C:/Users/Javier Ornelas/OneDrive/Documents/HVSRdata_Main/mHVSR Site Inv/VSPDB Data/CA Vertical Array Data - Afshari and Stewart/Site Peak Iden/Gaussian Pulse/Meta/site_ALL_distance_meas_from_vert_array.csv'
    assert gui.loc_df_manual_widget.value == 'C:/Users/Javier Ornelas/OneDrive/Documents/HVSRdata_Main/mHVSR Site Inv/VSPDB Data/CA Vertical Array Data - Afshari and Stewart/Site Peak Iden/modified_Latitude_and_Longitude_CA_Vert_Array_spatial_study.csv'
    assert gui.save_dir_widget.value == 'C:/Users/Javier Ornelas/OneDrive/Documents/HVSRdata_Main/Outputs'

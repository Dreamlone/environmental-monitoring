from pathlib import Path
from typing import Union

from matplotlib import pyplot as plt

import seaborn as sns
import pandas as pd

from emo.paths import eda_results_folder


def lammi_station(path_to_file: Path):
    """ Function for exploratory data analysis (EDA)

    Dataset structure:
    - 'Location' - nan. Unification needed
    - 'X and Y (coordinates)' - Contain nan
    - 'Coordinate system' - nan. Better use EPSG code and convert into WGS84
    - 'Other type' - better to assimilate into 'Environment type' column
    - 'Measured variables' - may convert them into list
    - 'Unit' - nans need to remove
    - 'Temporal extent' - Teuronjoki, Hämeenkoski probably not about the time
    - 'Starting year' - must be in datetime format
    - 'End year' - the same. It is better to create additional column
    - 'Temporal resolution' - better to use not words description. Unification needed
    - 'Data type' - define strict data types
    - 'Format' - format no needed.
    - 'Is the dataset well described' needed to be bool
    - 'Is the dataset regularly shared somewhere' - need updates
    - 'Where' - link to the dataset needed

    General comments:
    - Normalization needed
    """
    sheet_name = "Lammi"
    folder = eda_results_folder(sheet_name)
    df = pd.read_excel(path_to_file, sheet_name=sheet_name)

    print(f'Lammi station dataset exploration. Columns number: {len(list(df.columns))}')
    fig_size = (10, 7.0)
    fig, ax = plt.subplots(figsize=fig_size)
    sns.scatterplot(ax=ax, data=df[['X', 'Y', 'Environment type']], x="X", y="Y", hue="Environment type")
    plt.savefig(Path(folder, 'map.png'), dpi=300)
    plt.close()


def kilpisjarvi_station(path_to_file: Path):
    """ Function for exploratory data analysis (EDA)

    Dataset structure:
    - 'Location' - nan. Unification needed
    - 'X and Y, Coordinate system' - coordinate system and coordinates needed to be provided
    - 'Other type' - better to assimilate into 'Environment type' column
    - 'Measured variables' - may convert them into list. nan
    - 'Unit' - nans need to remove and ???
    - 'Spatial extent' - nan better to use Polygon or remove the whole column
    - 'Spatial resolution' - m for meters and cm - centimeters. Unification
    - 'Temporal resolution' - better to use not words description. Unification needed
    - 'Starting year' - must be in datetime format
    - 'End year' - the same. It is better to create additional column
    - 'Data type' - define strict data types
    - 'Format' - format no needed.
    - 'Is the dataset well described' needed to be bool
    - 'Is the dataset regularly shared somewhere' - need updates
    - 'Where' - link to the dataset needed

    General comments:
    - Normalization needed
    """
    sheet_name = "Kilpisjärvi"
    folder = eda_results_folder(sheet_name)
    df = pd.read_excel(path_to_file, sheet_name=sheet_name)


def tvarminne_station(path_to_file: Path):
    """ Function for exploratory data analysis (EDA)

    Dataset structure:
    - 'Station' - nan
    - 'Location, X and Y, Coordinate system' - coordinate system and coordinates needed to be provided
    - 'Environment type': nan
    - 'Other type' - better to assimilate into 'Environment type' column
    - 'Measured variables' - may convert them into list. nan
    - 'Unit' - nans need to remove
    - 'Spatial extent' - nan better to use Polygon or remove the whole column
    - 'Spatial resolution' - m for meters and cm - centimeters. Unification
    - 'Temporal resolution' - better to use not words description. Unification needed
    - 'Starting year' - must be in datetime format
    - 'End year' - the same. It is better to create additional column
    - 'Is the dataset well described' needed to be bool
    - 'Is the dataset regularly shared somewhere' - need updates
    - 'Where' - link to the dataset needed

    General comments:
    - Normalization needed
    """
    sheet_name = "Tvärminne"
    folder = eda_results_folder(sheet_name)
    df = pd.read_excel(path_to_file, sheet_name=sheet_name)

    print(f'Tvärminne station dataset exploration. Columns number: {len(list(df.columns))}')


class DataExplorer:

    method_by_name = {"Lammi": lammi_station,
                      "Kilpisjärvi": kilpisjarvi_station,
                      "Tvärminne": tvarminne_station}

    def __init__(self, path_to_file: Union[Path, str]):
        if isinstance(path_to_file, str):
            path_to_file = Path(path_to_file)

        self.path_to_file = path_to_file.resolve()

    def analyse(self, name: str):
        """ Apply appropriate analysis method """
        self.method_by_name[name](self.path_to_file)

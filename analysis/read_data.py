from pathlib import Path

from emo.main import DataExplorer
from emo.paths import get_data_path


def read_page(sheet_name: str):
    explorer = DataExplorer(Path(get_data_path(), 'data.xlsx'))
    explorer.analyse(sheet_name)


if __name__ == '__main__':
    read_page(sheet_name='Tvärminne')

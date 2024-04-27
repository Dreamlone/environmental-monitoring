from pathlib import Path


def get_project_path() -> Path:
    return Path(__file__).parent.parent


def get_data_path():
    return Path(get_project_path(), 'data')


def eda_results_folder(folder_name: str) -> Path:
    folder = Path(get_project_path(), 'results', folder_name)
    folder.mkdir(parents=True, exist_ok=True)
    return folder

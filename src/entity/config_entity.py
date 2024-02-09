from dataclasses import dataclass
from pathlib import Path
from src.utils.commonutils import read_yaml_file
from src.constants import CONFIG_FILE_PATH

configuration_details = read_yaml_file(file_path=CONFIG_FILE_PATH)

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path=configuration_details['data_ingestion']['root_dir']
    data_source_url: Path=configuration_details['data_ingestion']['source_url']
    downloaded_file_path: Path=configuration_details['data_ingestion']['downloaded_data_filepath']
    extracted_file_path: Path=configuration_details['data_ingestion']['extracted_data_filepath']
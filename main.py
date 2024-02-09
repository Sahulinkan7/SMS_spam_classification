from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig

dconfig=DataIngestionConfig()
di=DataIngestion(data_ingestion_config=dconfig)
di.download_data()

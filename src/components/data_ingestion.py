from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataIngestionConfig
import os,sys
import urllib.request as request

class DataIngestion:
    def __init__(self,data_ingestion_config : DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
            logging.info(f"Data Ingestion object created")
            os.makedirs(self.data_ingestion_config.root_dir,exist_ok=True)
        except Exception as e:
            logging.error(f"Creating data ingestion object failed due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def download_data(self):
        try:
            logging.info(f"Downloading data from source")
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.downloaded_file_path),exist_ok=True)
            logging.info(f"Download directory created")
            request.urlretrieve(url=self.data_ingestion_config.data_source_url,
                                filename=self.data_ingestion_config.downloaded_file_path)
            logging.info(f"Data downloaded successfully !")
            
        except Exception as e:
            logging.error(f"Downloading data failed due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
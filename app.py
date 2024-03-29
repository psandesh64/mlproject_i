from src.mlproject_i.logger import logging
from src.mlproject_i.exception import CustomException
import sys
from src.mlproject_i.components.data_ingestion import DataIngestion
from src.mlproject_i.components.data_ingestion import DataIngestionConfig


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

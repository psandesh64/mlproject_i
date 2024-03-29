from src.mlproject_i.logger import logging
from src.mlproject_i.exception import CustomException
import sys
from src.mlproject_i.components.data_ingestion import DataIngestion
from src.mlproject_i.components.data_ingestion import DataIngestionConfig
from src.mlproject_i.components.data_transformation import DataTransformationConfig, DataTransformation


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

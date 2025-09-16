from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.components.data_transformation import DataTransformation
from network_security.components.model_trainer import ModelTrainer
from network_security.entity.config_entity import DataIngestionConfig
from network_security.entity.config_entity import DataValidationConfig
from network_security.entity.config_entity import DataTransformationConfig
from network_security.entity.config_entity import TrainingPipelineConfig
from network_security.entity.config_entity import ModelTrainerConfig
import sys


if __name__=="__main__":
    try:
        logging.info("Initiating Data Ingestion")
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        dataingestion=DataIngestion(dataingestionconfig)
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info("Data Ingestion Completed")

        datavalidationconfig=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Inititate data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation complete")
        print(data_validation_artifact)

        datatransformationconfig=DataTransformationConfig(trainingpipelineconfig)
        datatransformation=DataTransformation(data_validation_artifact,datatransformationconfig)
        logging.info("Initiating data transformatin")
        data_transformation_artifact=datatransformation.initiate_data_transformation()
        print(data_transformation_artifact)
        print("Data transformation Completed")

        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config,data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        print(model_trainer_artifact)
        print("model training complete")




        
    except Exception as e:
        raise NetworkSecurityException(e,sys)

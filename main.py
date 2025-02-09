from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from text_summarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from text_summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from text_summarizer.logging import logger


STAGE_NAME= "Data Ingestion Stage"

try:
    logger.info(f"started>>>>{STAGE_NAME}<<<<started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation Stage"
try:
    logger.info(f"started>>>>{STAGE_NAME}<<<<started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f"started>>>>{STAGE_NAME}<<<<started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Training Stage"
try:
    logger.info(f"started>>>>{STAGE_NAME}<<<<started")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Evaluation Stage"
try:
    logger.info(f"started>>>>{STAGE_NAME}<<<<started")
    model_training = ModelEvaluationPipeline()
    model_training.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e
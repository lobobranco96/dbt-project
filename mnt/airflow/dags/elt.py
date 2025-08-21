import os
from datetime import datetime
import logging
from src.s3ingestor import UploadMinio
from src.extract import ExtractApi

from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator
from cosmos import DbtTaskGroup, ProfileConfig, ProjectConfig



# MinIO credentials
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
ENDPOINT_URL = os.getenv("ENDPOINT_URL") 

S3_CONFIG = {"access_key": ACCESS_KEY,
             "secret_key": SECRET_KEY,
             "endpoint_url": ENDPOINT_URL}

# Configuração do logger para monitoramento de logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

default_args = {
    "owner": "github/lobobranco96",
    "retries": 1,
    "retry_delay": 0
}
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    default_args=default_args,
    tags=["build a data source"],
)
def pipeline():

    init = EmptyOperator(task_id="inicio")
    finish = EmptyOperator(task_id="fim_pipeline")

    @task
    def api_to_minio():

        logger.info('Iniciando a coleta.')
        url = ""
        data = ExtractApi(url).extract()

        object_name = f'rawdata_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'  
        bucket_name = 'raw'
        minio = UploadMinio(S3_CONFIG)
        minio.upload(bucket_name, object_name, data)


    extract = api_to_minio()

    init >> extract >> finish
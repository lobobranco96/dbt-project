# dbt-project

utilizando: 
airflow(astronomer) -> orchestration
dbt -> transformation + data quality check
python -> script customizado para coleta e carregamento (csv > dw) // python astro sdk
datalake -> minio[armazenamento de dados csv]
dw -> armazenamento inicial com a tabela raw + formato scd type 2
metabase -> data visualization
prometheus + grafana -> observabilidade
docker -> container

docker
 ├── prometheus + grafana [observabilidade]
 ├── airflow (astronomer) [orquestração]
 ├── python [scripts customizados de coleta]
 ├── minio [datalake - CSV]
 ├── dw [raw, SCD Type 2]
 └── dbt [transformação+ SCD type2 + data quality]
 └── metabase [visualização de dados]

docker = localExecutor

docker[prometheus+grafana[airflow[python[api][minio] > dw[pastrosqk] > dbt[dataquality+[std>fact/dim]]] > metabase]]

implementação de principios solid


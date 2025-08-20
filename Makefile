# Makefile para gerenciamento de containers com Docker Compose

.PHONY: start_airflow start_observability start_visualization start_storage start_all_services stop restart

# Inicia o Airflow usando o Astro CLI
start_airflow:
	astro dev start

# Inicia os serviços de observabilidade (Prometheus, Grafana)
start_observability:
	docker compose -f services/observability.yaml up -d

# Inicia serviços de visualização
start_visualization:
	docker compose -f services/visualization.yaml up

# Inicia serviços de storage
start_storage:
	docker compose -f services/storage.yaml up

# Inicia todos os serviços
start_all_services:
	astro dev start
	docker compose -f services/observability.yaml up
	docker compose -f services/visualization.yaml up
	docker compose -f services/storage.yaml up

# Para os containers do Airflow e dos serviços de observabilidade
stop:
	docker compose -f services/observability.yaml down
	docker compose -f services/visualization.yaml down
	docker compose -f services/storage.yaml down
	astro dev stop

# Reinicia o Airflow e os serviços de observabilidade
restart: stop start_airflow start_observability start_visualization start_storage

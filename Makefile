# Makefile para gerenciamento de containers com Docker Compose

.PHONY: start_airflow start_observability stop


# Inicia o Airflow usando o Astro CLI
start_airflow: 
  astro dev start

# Inicia os serviços de observabilidade (Prometheus, Grafana)
start_observability:
	docker compose -f services/observability.yml up

# Para os containers do Airflow e dos serviços de observabilidade
stop:
	docker compose -f services/observability.yml down
  astro dev stop

# Reinicia o Airflow e os serviços de observabilidade
restart: stop start_airflow start_observability
.PHONY: help build up down restart logs stop ps shell clean

.DEFAULT_GOAL := help

COMPOSE_FILE := docker-compose.yml

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build the Docker images
	docker compose -f $(COMPOSE_FILE) build

up: ## Start the containers
	docker compose -f $(COMPOSE_FILE) up -d

up-build: ## Build and start the containers
	docker compose -f $(COMPOSE_FILE) up -d --build

down: ## Stop and remove containers
	docker compose -f $(COMPOSE_FILE) down

restart: ## Restart the containers
	docker compose -f $(COMPOSE_FILE) restart

stop: ## Stop the containers without removing them
	docker compose -f $(COMPOSE_FILE) stop

logs: ## Show logs from all containers
	docker compose -f $(COMPOSE_FILE) logs -f

logs-api: ## Show logs only from the API container
	docker compose -f $(COMPOSE_FILE) logs -f api

ps: ## Show status of containers
	docker compose -f $(COMPOSE_FILE) ps

shell: ## Open a shell in the API container
	docker compose -f $(COMPOSE_FILE) exec api /bin/bash

clean: ## Stop containers and remove volumes
	docker compose -f $(COMPOSE_FILE) down -v

clean-all: clean ## Remove containers, volumes, and images
	docker compose -f $(COMPOSE_FILE) down -v --rmi all


# Makefile pour Advent of code

# Configuration 
PYTHON = python
PYTHEST = pytest
SRC_DIR = src
TEST_DIR = tests

# Cible par défaut
.PHONY : help
help:
	@echo "Commandes disponibles :"
	@echo " make test			- Lancer tous les tests"
	@echo " make run DAY=n			- Executer le script pour un jour specifique"
	@echo " make clean			- Nettoyer les fichiers temporaires"
	@echo " make deps			- Installer les dépendances"
	@echo " make venv			- Activer l'enrironnement virtuel python"


.PHONY : test
test:
	$(PYTHEST) $(TEST_DIR)

# Exécuter un jour spécifique
.PHONY : run
run:
	@if [ -z "$(DAY)"]; then \
		echo "Précisez le jour avec DAY=n (ex: make run DAY=1)" \
		exit 1; \
	fi
	$(PYTHON) $(SRC_DIR)/day$(DAY).py

# Nettoyer les fichiers temporaires
.PHONY: clean
clean :
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.log" -delete


# Installer les dépendances
.PHONY: deps
deps:
	$(PYTHON) -m pip install -r requirements.txt

# activer l'environnement virtuel
.PHONY: venv
venv :
	(\
		source venv/Scripts/activate; \
	)
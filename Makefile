.PHONY: help install lint format clean run authorship

# Default target
help:
	@echo "Available commands:"
	@echo "  make install     - Install project dependencies"
	@echo "  make lint        - Run flake8 linting"
	@echo "  make format      - Format code with black (requires black)"
	@echo "  make clean       - Remove Python cache files"
	@echo "  make run         - Run all exercise files"
	@echo "  make authorship  - Run book authorship example"

# Install dependencies
install:
	pip install flake8 black

# Run linting
lint:
	flake8 .

# Format code (requires black)
format:
	black .

# Clean Python cache files
clean:
	find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name ".DS_Store" -delete

# Run all exercise files
run:
	@echo "Running contracts.py..."
	@python oop_refresher/contracts.py || true
	@echo "\nRunning book_authorship.py..."
	@python oop_refresher/book_authorship.py || true

# Run book authorship example
authorship:
	@python oop_refresher/book_authorship.py


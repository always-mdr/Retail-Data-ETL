.PHONY: setup run clean dashboard

setup:
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt
	mkdir -p data

run:
	./venv/bin/python main_pipeline.py

dashboard:
	./venv/bin/streamlit run src/dashboard.py

clean:
	rm -rf data/*
	rm -rf venv

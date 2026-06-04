install:
	pip install -r requirements.txt

test:
	pytest -q

e2e:
	python3 scripts/run_all_experiments.py

e2e-srsran:
	python3 scripts/generate_srsran_config_stub.py

e2e-oai:
	python3 scripts/generate_oai_config_stub.py

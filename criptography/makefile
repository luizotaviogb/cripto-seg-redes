

execute: install
	python3 app.py

execute.desktop: install
	python3 criptographyDesktop.py

execute.web: install
	python3 criptographyWeb.py
	firefox -new-tab 'http://127.0.0.1:5000/'

install:
	pip install -r requirements.txt
	chmod +x criptographyDesktop.py
	chmod +x criptographyDesktop.py
	chmod +x app.py

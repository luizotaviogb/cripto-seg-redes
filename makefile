

execute: install
	./app.py

execute.desktop: install
	./criptographyDesktop.py

execute.web: install
	./criptographyWeb.py
	firefox -new-tab 'http://127.0.0.1:5000/'

install:
	pip install -r requirements.txt
	chmod +x criptographyDesktop.py
	chmod +x criptographyDesktop.py
	chmod +x app.py

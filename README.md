Übersicht

Dieses Projekt ist das Backend einer Scrum Board Anwendung, entwickelt mit Django und Django REST Framework. Es bietet APIs für das Management von Aufgaben (Todos) und Kontakten (Contacts).

Inhaltsverzeichnis
    Technologien
    Installation
        Voraussetzungen
        Schritte
    Umgebungsvariablen
    APIs
        Authentifizierung
        Todo API
        Kontakt API
    Nutzung
    Tests
    Beitrag
    Lizenz

Technologien
Django
Django REST Framework
SQLite (Standard)
Docker (optional)

Installation
Voraussetzungen
Python 3.8 oder höher
Pipenv oder Virtualenv (empfohlen)
Git
SQLite (Standard) oder ein anderes konfiguriertes Datenbanksystem

Schritte
Repository klonen:
git clone https://github.com/IhrGitHubBenutzername/scrum_board_backend.git
cd scrum_board_backend

Virtuelle Umgebung erstellen und aktivieren:
python -m venv venv
source venv/bin/activate # Auf Windows: venv\Scripts\activate

Abhängigkeiten installieren:
pip install -r requirements.txt

Datenbank migrieren:
python manage.py migrate

Erstellen Sie einen Superuser:
python manage.py createsuperuser

Server starten:
python manage.py runserver

Umgebungsvariablen
Erstellen Sie eine .env-Datei in Ihrem Projektverzeichnis mit folgenden Variablen:

makefile
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=127.0.0.1,localhost

Weitere Konfigurationen finden Sie in scrum_board_backend/settings.py.
APIs
Authentifizierung

    Login: POST /api-token-auth/
        Anfrage:

        json

{
"username": "username",
"password": "password"
}

Antwort:

json
        {
          "token": "your-token",
          "user_id": 1,
          "email": "user@example.com"
        }

Todo API
    Abrufen aller Todos: GET /todos/
    Abrufen eines Todo: GET /todos/{id}/
    Erstellen eines Todo: POST /todos/
    Aktualisieren eines Todo: PUT /todos/{id}/
    Löschen eines Todo: DELETE /todos/{id}/

Kontakt API
    Abrufen aller Kontakte: GET /contacts/
    Abrufen eines Kontakts: GET /contacts/{id}/
    Erstellen eines Kontakts: POST /contacts/
    Aktualisieren eines Kontakts: PUT /contacts/{id}/
    Löschen eines Kontakts: DELETE /contacts/{id}/

Nutzung
    Starten Sie den Entwicklungsserver:
    python manage.py runserver

    Öffnen Sie im Browser http://127.0.0.1:8000/admin/ und melden Sie sich mit den Superuser Zugangsdaten an.
    Verwenden Sie http://127.0.0.1:8000/api/ für API-Aufrufe.

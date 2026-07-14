# Bérkalkulátor alkalmazás

Ez egy modern, felhőalapú bérkalkulátor alkalmazás, amely a bruttó bérből számolja ki a nettó összeget. A projekt célja a teljes körű webes fejlesztési és DevOps folyamatok demonstrálása, a frontendtől a felhőalapú backendig.

## 🚀 Technológiai Stack

- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Backend:** Python (Flask)
- **Felhő:** Microsoft Azure Static Web Apps
- **DevOps:** GitHub Actions (Automated CI/CD Pipeline)

## 🛠 Projekt jellemzők

- **Serverless Backend:** A számítási logika egy dedikált, skálázható Python API-n fut.
- **CI/CD Integráció:** Minden `git push` automatikusan elindítja a tesztelési és telepítési folyamatot a GitHub Actions-on keresztül.
- **SSL/TLS:** Ingyenes, automatizált HTTPS titkosítás.
- **Domain:** Egyedi domain (www.itnest.hu) integráció.

## 📦 Telepítés (Fejlesztői környezet)

1. Klónozd a repót:
   ```bash
   git clone [https://github.com/dgera90/berkalk2.git](https://github.com/dgera90/berkalk2.git)

    Telepítsd a függőségeket:
    Bash

    cd api
    pip install -r requirements.txt

    Futtasd a helyi szervert a teszteléshez.

📈 Tervezett fejlesztések

    [ ] Cafeteria számítási modul

    [ ] Adókedvezmények (családi, első házasok) hozzáadása

    [ ] Eredmények exportálása PDF-be

Készült: 2026

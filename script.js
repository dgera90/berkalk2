// 1. Kiszámoljuk az aktuális hónapot GLOBÁLISAN, hogy minden függvény lássa!
const aktualisHonap = new Date().getMonth() + 1; 

// 2. Az oldal betöltésekor beállítja a legördülő menüt az aktuális hónapra
window.onload = function() {
    document.getElementById('honap').value = aktualisHonap;
};

// 3. A fő kalkulációs logika
async function kalkulacio() {
    // Adatok begyűjtése az űrlapról
    const adat = {
        oraber: parseInt(document.getElementById('oraber').value) || 0,
        honap: parseInt(document.getElementById('honap').value) || 1,
        delutanos_muszak: parseInt(document.getElementById('delutanos_muszak').value) || 0,
        hetkoznapi_tulora: parseInt(document.getElementById('hetkoznapi_tulora').value) || 0,
        hetvegi_tulora: parseInt(document.getElementById('hetvegi_tulora').value) || 0,
        gyerekek_szama: parseInt(document.getElementById('gyerekek_szama').value) || 0
    };

    try {
        // Kérés küldése az Azure Functions (Python) végpontra (LOKÁLIS TESZTHEZ)
        const valasz = await fetch('/api/kalkulal', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(adat)
        });

        const eredmeny = await valasz.json();

        // Eredmény megjelenítése a weboldalon
        document.getElementById('brutto').innerText = eredmeny.brutto.toLocaleString('hu-HU');
        document.getElementById('netto').innerText = eredmeny.netto.toLocaleString('hu-HU');
        document.getElementById('eredmeny').style.display = 'block';

    } catch (hiba) {
        alert("Hiba történt a szerverrel való kommunikáció során!");
        console.error(hiba);
    }
}

// 4. Mindent visszaállít az alapértelmezett értékekre
function torles() {
    document.getElementById('oraber').value = 0;
    
    // Most már hibátlanul működik, mert az aktualisHonap legfelül lett definiálva!
    document.getElementById('honap').value = aktualisHonap; 
    
    document.getElementById('delutanos_muszak').value = 0;
    document.getElementById('hetkoznapi_tulora').value = 0;
    document.getElementById('hetvegi_tulora').value = 0;
    document.getElementById('gyerekek_szama').value = 0;
    
    // Eredmény doboz elrejtése
    document.getElementById('eredmeny').style.display = 'none';
}

// 5. Csak az eredményt rejti el, hogy lehessen finomhangolni a számokat
function ujSzamolas() {
    document.getElementById('eredmeny').style.display = 'none';
    
    // Fókuszba teszi az első mezőt (Órabér), hogy azonnal lehessen gépelni
    document.getElementById('oraber').focus();
}
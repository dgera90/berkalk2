import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="kalkulal", auth_level=func.AuthLevel.ANONYMOUS)
def kalkulal(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        
        # Bemeneti adatok
        oraber = req_body.get('oraber', 0)
        honap = req_body.get('honap', 1)
        delutanos_muszak = req_body.get('delutanos_muszak', 0)
        hetkoznapi_tulora = req_body.get('hetkoznapi_tulora', 0)
        hetvegi_tulora = req_body.get('hetvegi_tulora', 0)
        gyerek = req_body.get('gyerekek_szama', 0)
        
        # 1. Munkanapok meghatározása (egyszerűsített havi munkanap szótár 2026-ra)
        munkanapok_szama = {
            1: 21, 2: 20, 3: 22, 4: 21, 5: 20, 6: 22,
            7: 23, 8: 20, 9: 22, 10: 21, 11: 21, 12: 21
        }
        munkanap = munkanapok_szama.get(honap, 21)
        
        # 2. Bruttó elemek kiszámítása
        alapber = munkanap * 8 * oraber
        
        # ÚJ LOGIKA: Délutános műszakpótlék (15%)
        # Csak akkor jár, ha a délutános műszakok száma eléri a havi munkanapok legalább 30%-át
        if delutanos_muszak >= (munkanap * 0.30):
            delutanos_potlek = delutanos_muszak * 8 * (oraber * 0.15)
        else:
            delutanos_potlek = 0
            
        hetkoznapi_tuloradij = hetkoznapi_tulora * (oraber * 1.50) # 50% pótlék
        hetvegi_tuloradij = hetvegi_tulora * (oraber * 2.0)        # 100% pótlék
        
        brutto = alapber + delutanos_potlek + hetkoznapi_tuloradij + hetvegi_tuloradij
        
        # 3. Adók és járulékok (15% SZJA, 18.5% TB)
        szja = brutto * 0.15
        tb = brutto * 0.185
        
        # 4. Családi adókedvezmény (a fizetendő SZJA-t és TB-t csökkenti)
        kedvezmeny_keret = 0
        if gyerek == 1:
            kedvezmeny_keret = 20000
        elif gyerek == 2:
            kedvezmeny_keret = 80000
        elif gyerek >= 3:
            kedvezmeny_keret = gyerek * 100000
            
        osszes_ado = szja + tb
        fizetendo_ado = max(0, osszes_ado - kedvezmeny_keret)
        
        netto = brutto - fizetendo_ado

        # Válasz összeállítása JSON formátumban
        import json
        valasz = {
            "brutto": int(brutto),
            "netto": int(netto)
        }
        
        return func.HttpResponse(
            body=json.dumps(valasz),
            mimetype="application/json",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"Hiba a feldolgozás során: {e}")
        return func.HttpResponse("Hibás adatformátum", status_code=400)

import requests
import pandas as pd

# Funzione per recuperare le coordinate geografiche dalle città passate nella lista Listacitta

# Inserire nella lista le città di cui si vogliono ottenere i dati meteo

ListaCitta=["Parma","Milano","Bologna"]

def geocode_city(city_name, count=1, language="it"):

    url = "https://geocoding-api.open-meteo.com/v1/search"
    l=[]
    for city in city_name:
        
        params = {"name": city, "count": count, "language": language}
        r = requests.get(url, params=params)
        js = r.json() or {}
        results = js.get("results") or []
        
        if not results:
            raise ValueError(f"Impossibile trovare coordinate per '{city}'.")
        #results è una lista di json di cui prendo il primo
        first = results[0]
        # fare il print della variabile first per vedere i metadati che ritorna la chiamata api
        #print(first)
        d={
            "name_resolved": first.get("name"),
            "latitude": first.get("latitude"),
            "longitude": first.get("longitude"),
        }
        l.append(d)
    return l

# Inserire nella lista     
l=geocode_city(ListaCitta)

#l è una lista di dictionary, ogni dictionary corrisponde ad una delle città inserite nel parametro

# Esempio di chiamata a open meteo. Selezionare il tipo di chiamata ("daily" o "hourly" a seconda che voglio dati giornalieri o orari)
#Scegliere il range temporale interessato e i dati da estrarre


TipoChiamata="daily"


#Non cambiare queste due variabili
FrequenzaOraria="hourly"
FrequenzaGiornaliera="daily"


#Selezionare il range temporale
DataInizio="2026-01-01"
DataFine="2026-01-02"

#Selezionare i metadati da estrarre per l'estrazione oraria e giornaliera
VariabiliGiornaliere=[
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "windspeed_10m_max",
        "sunshine_duration",
        "showers_sum",
    ]
VariabiliOrarie=["snowfall"]

#a seconda di quello che passo a tipochiamata valorizzo VariabiliDichiamata con i metadati che voglio estrarre
VariabiliDiChiamata=VariabiliGiornaliere if TipoChiamata=="daily" else VariabiliOrarie


def fetch_openmeteo_series(lat, lon, frequency, variables, start_date, end_date, timezone):

    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "timezone": timezone,
        "start_date": start_date,
        frequency:variables,
        "end_date": end_date,
    }


    r = requests.get(base_url, params=params)
    js = r.json() or {}
    # La chiamata prende come parametro daily o hourly a seconda dei dati che voglio estrarre
    block = js.get(frequency) or {}
    #print(block)

    

    return block

df=pd.DataFrame({})
#x assumerà il valore di ogni dictionary corrispondente ad una città
for x in l:
    json=fetch_openmeteo_series(x["latitude"],x["longitude"],TipoChiamata,VariabiliDiChiamata,DataInizio,DataFine,"Europe/Rome")

    meteodictionary=dict(json)
    dfparziale=pd.DataFrame(meteodictionary)
    dfparziale["City"]=x["name_resolved"]
    
    df=pd.concat([df,dfparziale],axis=0)
    
df=df.set_index("time")
df.to_csv("EstrazioneMeteo",sep=";")


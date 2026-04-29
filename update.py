import datetime
import random
import json

# Configurazione Giorno
oggi = datetime.datetime.now().weekday()
nomi_giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
nome_oggi = nomi_giorni[oggi]

# --- DATABASE ALLENAMENTI (Progressione 8-12 rep con 10kg) ---
allenamenti = {
    0: { # LUNEDI: Spinta & Addome Sup
        "titolo": "Upper Body (Spinta) & Addome Sup.",
        "calorie": "320 - 380 kcal",
        "esercizi": [
            {"nome": "Push-up Classici (Focus: Petto Esterno)", "set": "4 x Max", "dritta": "Discesa in 3s. Se ne fai +20, metti un peso sulla schiena.", "yt": "push+up+form"},
            {"nome": "Squeeze Press (Focus: Petto Interno)", "set": "3 x 8-12", "dritta": "Usa 8-10kg. Schiaccia i manubri tra loro con forza.", "yt": "dumbbell+squeeze+press"},
            {"nome": "Arnold Press (Spalle Ant/Mid)", "set": "4 x 8-10", "dritta": "Carico progressivo. Ruota i polsi in spinta.", "yt": "arnold+press+form"},
            {"nome": "Alzate Laterali (Spalla Centrale)", "set": "3 x 12-15", "dritta": "Usa 4-6kg. Fermo di 2 secondi in alto.", "yt": "lateral+raises+dumbbells"},
            {"nome": "Skullcrusher a terra (Tricipiti)", "set": "3 x 10-12", "dritta": "Gomiti immobili. Punta al soffitto.", "yt": "skull+crushers+dumbbells"},
            {"nome": "Crunch Zavorrato (Addome Sup)", "set": "3 x 15-20", "dritta": "Tieni un manubrio sul petto. Contrai forte.", "yt": "weighted+crunch"}
        ]
    },
    2: { # MERCOLEDI: Lower Body & Polpacci
        "titolo": "Lower Body, Polpacci & Lombari",
        "calorie": "400 - 480 kcal",
        "esercizi": [
            {"nome": "Squat Bulgaro (Coscia Ant/Glutei)", "set": "4 x 8-10 per gamba", "dritta": "Usa 10kg per mano. Schiena dritta, scendi profondo.", "yt": "bulgarian+split+squat"},
            {"nome": "Stacchi Rumeni / RDL (Coscia Post)", "set": "4 x 10-12", "dritta": "Senti tirare dietro la coscia. Manubri vicini alle gambe.", "yt": "romanian+deadlift+dumbbells"},
            {"nome": "Affondi Posteriori Alternati", "set": "3 x 12 per gamba", "dritta": "Passo lungo all'indietro. Ginocchio sfiora terra.", "yt": "reverse+lunges+dumbbells"},
            {"nome": "Calf Raise su gradino (Polpacci)", "set": "4 x 20", "dritta": "Usa un peso in mano. Massima escursione.", "yt": "calf+raise+step"},
            {"nome": "Superwoman (Schiena Inf/Lombari)", "set": "3 x 15", "dritta": "Solleva petto e gambe insieme. Tieni 2s.", "yt": "superman+exercise"}
        ]
    },
    3: { # GIOVEDI: Trazione & Addome Inf
        "titolo": "Upper Body (Trazione) & Addome Inf.",
        "calorie": "300 - 350 kcal",
        "esercizi": [
            {"nome": "Rematore Singolo (Schiena Mid/Up)", "set": "4 x 8-10 per lato", "dritta": "Usa 10kg. Tira il gomito verso l'anca.", "yt": "one+arm+dumbbell+row"},
            {"nome": "Dumbbell Pullover (Schiena Up/Petto)", "set": "3 x 12", "dritta": "Braccia quasi tese. Senti allungare il dorsale.", "yt": "dumbbell+pullover"},
            {"nome": "Alzate a 90° (Spalla Posteriore)", "set": "3 x 12-15", "dritta": "Usa 4-6kg. Busto parallelo a terra.", "yt": "rear+delt+fly+dumbbells"},
            {"nome": "Curl Bicipiti Alternato", "set": "4 x 10-12", "dritta": "Senza oscillare. Contrai il bicipite in cima.", "yt": "bicep+curls+form"},
            {"nome": "Leg Raises a terra (Addome Inf)", "set": "4 x 15", "dritta": "Gambe tese. Non inarcare la schiena lombare.", "yt": "leg+raises+form"}
        ]
    },
    4: { # VENERDI: Full Body & Circuito
        "titolo": "Full Body & Circuito Metabolico",
        "calorie": "450 - 550 kcal",
        "esercizi": [
            {"nome": "Thruster (Gambe + Spalle)", "set": "4 x 12", "dritta": "Squat e spinta sopra la testa in un solo movimento.", "yt": "dumbbell+thrusters"},
            {"nome": "Push-up Declinati (Piedi su sedia)", "set": "3 x Max", "dritta": "Sposta il focus sulla parte alta del petto.", "yt": "decline+push+up"},
            {"nome": "Affondi Laterali (Cosce)", "set": "3 x 10 per gamba", "dritta": "Mantieni la gamba opposta tesa.", "yt": "side+lunges+form"},
            {"nome": "Rematore Doppio (Schiena)", "set": "3 x 12", "dritta": "Tira entrambi i manubri verso l'ombelico.", "yt": "bent+over+dumbbell+row"}
        ]
    }
}

# --- GENERAZIONE HTML ---
html_esercizi = ""
if oggi in [1, 5, 6]: # Giorni di riposo
    titolo_scheda = "Giorno di Recupero Attivo 🔋"
    calorie_scheda = "Passeggiata o stretching leggero"
    html_esercizi = "<div class='card' style='text-align:center;'><h2>Tempo di Recupero!</h2><p>I muscoli hanno bisogno di riposo per crescere. Ci vediamo alla prossima sessione!</p></div>"
else:
    dati = allenamenti[oggi]
    titolo_scheda = dati["titolo"]
    calorie_scheda = f"Stima dispendio: {dati['calorie']}"
    for es in dati["esercizi"]:
        yt_link = f"https://www.youtube.com/results?search_query={es['yt']}"
        html_esercizi += f"""
        <div class="card">
            <h2>{es['nome']}</h2>
            <div class="badge">{es['set']}</div>
            <p><strong>💡 Focus:</strong> {es['dritta']}</p>
            <a href="{yt_link}" target="_blank" class="yt-link">▶️ Guarda Esecuzione</a>
        </div>
        """
    if oggi == 4: # Finisher del venerdì
        f = random.choice(["3 Minuti di Burpees", "Plank Challenge (3 min)", "Jumping Jacks continui"])
        html_esercizi += f"<div class='card finisher'><h2>🔥 FINISHER: {f}</h2></div>"

# Template HTML completo (CSS, JS, PWA)
full_html = f"""
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>HomeFit Automata</title>
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#121212">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <style>
        :root {{ --bg: #121212; --text: #ffffff; --card: #1e1e1e; --accent: #00d2ff; }}
        .light-mode {{ --bg: #f5f5f7; --text: #1d1d1f; --card: #ffffff; --accent: #0071e3; }}
        body {{ font-family: -apple-system, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 20px 20px 100px; transition: 0.3s; }}
        .header {{ text-align: center; margin-bottom: 30px; }}
        .header h1 {{ font-size: 1.8rem; color: var(--accent); margin: 0; }}
        .card {{ background: var(--card); padding: 20px; border-radius: 18px; margin-bottom: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
        .badge {{ display: inline-block; background: var(--accent); color: #fff; padding: 5px 12px; border-radius: 8px; font-weight: bold; margin-bottom: 10px; }}
        .yt-link {{ display: block; margin-top: 15px; color: var(--accent); text-decoration: none; font-weight: bold; font-size: 0.9rem; }}
        .sticky-timer {{ position: fixed; bottom: 0; left: 0; width: 100%; background: var(--card); padding: 15px; display: flex; justify-content: space-around; align-items: center; border-top: 1px solid #333; }}
        .timer-val {{ font-size: 2rem; font-weight: bold; color: var(--accent); font-family: monospace; }}
        .finisher {{ border: 2px solid #ff3b30; }}
        button {{ background: var(--card); color: var(--text); border: 1px solid var(--accent); padding: 10px 15px; border-radius: 10px; cursor: pointer; font-weight: bold; }}
    </style>
</head>
<body>
    <div id="content">
        <div class="header">
            <h1>{nome_oggi}: {titolo_scheda}</h1>
            <p>{calorie_scheda}</p>
        </div>
        <div style="display:flex; gap:10px; justify-content:center; margin-bottom:20px;">
            <button onclick="document.body.classList.toggle('light-mode')">☀️ Garden Mode</button>
            <button onclick="savePDF()">💾 Salva PDF</button>
        </div>
        {html_esercizi}
    </div>

    <div class="sticky-timer">
        <button onclick="startTimer(45)">45s</button>
        <div class="timer-val" id="time">00</div>
        <button onclick="startTimer(60)">60s</button>
    </div>

    <script>
        function savePDF() {{
            const element = document.getElementById('content');
            html2pdf().from(element).save('Allenamento_{nome_oggi}.pdf');
        }}
        let t;
        function startTimer(s) {{
            clearInterval(t); let time = s;
            document.getElementById('time').innerText = time;
            t = setInterval(() => {{
                time--; document.getElementById('time').innerText = time < 10 ? '0'+time : time;
                if(time <= 0) {{ clearInterval(t); document.getElementById('time').innerText = 'GO!'; }}
            }}, 1000);
        }}
        if('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js');
    </script>
</body>
</html>
"""

# Scrittura File
with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
with open("manifest.json", "w") as f: json.dump({"name":"HomeFit","short_name":"HomeFit","start_url":"index.html","display":"standalone","background_color":"#121212","theme_color":"#121212","icons":[{"src":"https://cdn-icons-png.flaticon.com/512/2964/2964096.png","sizes":"512x512","type":"image/png"}]}, f)
with open("sw.js", "w") as f: f.write("self.addEventListener('fetch', function(event) {});")

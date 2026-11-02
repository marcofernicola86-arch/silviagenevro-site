# Genera le illustrazioni del sito (SVG) nella palette del logo.
import os, sys
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

BLU = "#013260"
BLU2 = "#0b4f86"
ACQUA = "#2befc0"
ACQUA_T = "#bff7e8"
VERDE = "#94ff83"
VERDE_T = "#dcffd4"
TEAL = "#0a7565"
MENTA = "#eef9f5"
CREMA = "#fbf7f0"
PELLE = "#f2c9a9"


def figura(x, y, s=1.0, corpo=BLU, capelli=BLU, pelle=PELLE, stola=None):
    """Figura seduta in meditazione, stile piatto. (x,y) = punto a terra al centro."""
    g = f'<g transform="translate({x} {y}) scale({s})">'
    # gambe incrociate
    g += f'<path d="M-44 0 Q-40 -20 -14 -22 L14 -22 Q40 -20 44 0 Q22 6 0 4 Q-22 6 -44 0Z" fill="{corpo}"/>'
    # busto
    g += f'<path d="M-19 -24 L-15 -66 Q0 -74 15 -66 L19 -24 Q0 -18 -19 -24Z" fill="{corpo}"/>'
    if stola:
        g += f'<path d="M-15 -66 Q0 -74 15 -66 L10 -46 Q0 -52 -10 -46Z" fill="{stola}"/>'
    # braccia appoggiate sulle ginocchia
    g += f'<path d="M-16 -62 Q-34 -44 -32 -20" stroke="{corpo}" stroke-width="9" fill="none" stroke-linecap="round"/>'
    g += f'<path d="M16 -62 Q34 -44 32 -20" stroke="{corpo}" stroke-width="9" fill="none" stroke-linecap="round"/>'
    g += f'<circle cx="-32" cy="-19" r="4.5" fill="{pelle}"/><circle cx="32" cy="-19" r="4.5" fill="{pelle}"/>'
    # collo e testa
    g += f'<rect x="-4" y="-76" width="8" height="10" rx="3" fill="{pelle}"/>'
    g += f'<circle cx="0" cy="-86" r="12" fill="{pelle}"/>'
    # capelli con chignon
    g += f'<path d="M-12.5 -86 Q-13 -100 0 -100 Q13 -100 12.5 -86 Q8 -94 0 -94 Q-8 -94 -12.5 -86Z" fill="{capelli}"/>'
    g += f'<circle cx="0" cy="-103" r="6" fill="{capelli}"/>'
    g += "</g>"
    return g


def figura_in_piedi(x, y, s=1.0, corpo=BLU, capelli=BLU, pelle=PELLE, gambe=BLU):
    g = f'<g transform="translate({x} {y}) scale({s})">'
    g += f'<path d="M-9 0 L-7 -48 L7 -48 L9 0 L3 0 L0 -36 L-3 0Z" fill="{gambe}"/>'
    g += f'<path d="M-16 -46 L-13 -96 Q0 -104 13 -96 L16 -46 Q0 -42 -16 -46Z" fill="{corpo}"/>'
    g += f'<rect x="-4" y="-106" width="8" height="10" rx="3" fill="{pelle}"/>'
    g += f'<circle cx="0" cy="-116" r="11" fill="{pelle}"/>'
    g += f'<path d="M-11.5 -116 Q-12 -129 0 -129 Q12 -129 11.5 -116 Q7 -123 0 -123 Q-7 -123 -11.5 -116Z" fill="{capelli}"/>'
    g += "</g>"
    return g


def manager_uomo(x, y, s=1.0, giacca=BLU2, cravatta=ACQUA, capelli=BLU, pelle=PELLE):
    """Uomo in giacca e cravatta, in piedi."""
    g = f'<g transform="translate({x} {y}) scale({s})">'
    g += f'<path d="M-9 0 L-8 -48 L8 -48 L9 0 L3 0 L0 -36 L-3 0Z" fill="{BLU}"/>'          # pantaloni
    g += f'<path d="M-17 -46 L-14 -96 Q0 -103 14 -96 L17 -46 Q0 -42 -17 -46Z" fill="{giacca}"/>'  # giacca
    g += f'<path d="M-6 -98 L0 -84 L6 -98Z" fill="#ffffff"/>'                                # camicia
    g += f'<path d="M-6 -98 L-11 -80 L-2 -90Z M6 -98 L11 -80 L2 -90Z" fill="{BLU}" opacity=".35"/>'  # revers
    g += f'<path d="M-2.4 -94 L2.4 -94 L3.6 -70 L0 -64 L-3.6 -70Z" fill="{cravatta}"/>'      # cravatta
    g += f'<path d="M-3 -97 L3 -97 L2.4 -92 L-2.4 -92Z" fill="{cravatta}"/>'                 # nodo
    g += f'<rect x="-4" y="-106" width="8" height="10" rx="3" fill="{pelle}"/>'
    g += f'<circle cx="0" cy="-116" r="11" fill="{pelle}"/>'
    g += f'<path d="M-11.5 -114 Q-13 -130 0 -130 Q13 -130 11.5 -114 Q9 -123 0 -124 Q-9 -123 -11.5 -114Z" fill="{capelli}"/>'
    g += "</g>"
    return g


def manager_donna(x, y, s=1.0, tailleur=ACQUA, camicetta="#ffffff", capelli=BLU, pelle=PELLE, pettinatura="lunghi"):
    """Donna in tailleur con gonna, in piedi, capelli raccolti."""
    g = f'<g transform="translate({x} {y}) scale({s})">'
    g += f'<path d="M-6 0 L-5 -30 L-1 -30 L-2 0Z M2 0 L1 -30 L5 -30 L6 0Z" fill="{pelle}"/>'   # gambe
    g += f'<path d="M-8 0 L-3 -3 L-1 0Z M8 0 L3 -3 L1 0Z" fill="{BLU}"/>'                       # scarpe
    g += f'<path d="M-14 -28 L-12 -54 L12 -54 L14 -28Z" fill="{tailleur}"/>'                    # gonna
    g += f'<path d="M-15 -52 L-13 -96 Q0 -103 13 -96 L15 -52 Q0 -48 -15 -52Z" fill="{tailleur}"/>'  # giacca
    g += f'<path d="M-5 -98 L0 -84 L5 -98Z" fill="{camicetta}"/>'                            # scollo
    g += f'<path d="M-5 -98 L-10 -78 L-1 -88Z M5 -98 L10 -78 L1 -88Z" fill="{BLU}" opacity=".3"/>'  # revers
    g += f'<circle cx="0" cy="-72" r="1.6" fill="{BLU}" opacity=".5"/><circle cx="0" cy="-62" r="1.6" fill="{BLU}" opacity=".5"/>'
    if pettinatura == "lunghi":   # capelli lunghi sciolti sulle spalle (dietro al viso)
        g += f'<path d="M-14 -116 Q-15 -132 0 -132 Q15 -132 14 -116 L16 -88 Q8 -84 6 -92 L-6 -92 Q-8 -84 -16 -88Z" fill="{capelli}"/>'
    else:                          # caschetto corto
        g += f'<path d="M-14 -114 Q-15 -132 0 -132 Q15 -132 14 -114 L14 -104 Q10 -101 9 -106 L-9 -106 Q-10 -101 -14 -104Z" fill="{capelli}"/>'
    g += f'<rect x="-4" y="-106" width="8" height="10" rx="3" fill="{pelle}"/>'
    g += f'<circle cx="0" cy="-116" r="11" fill="{pelle}"/>'
    if pettinatura == "lunghi":   # frangia di lato
        g += f'<path d="M-11.5 -116 Q-12 -129 0 -129 Q12 -129 11.5 -118 Q4 -126 -4 -122 Q-8 -120 -11.5 -116Z" fill="{capelli}"/>'
    else:                          # frangia dritta del caschetto
        g += f'<path d="M-11.5 -114 Q-12 -129 0 -129 Q12 -129 11.5 -114 L10 -118 L-10 -118Z" fill="{capelli}"/>'
    g += "</g>"
    return g


def svg(w, h, body, titolo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{titolo}">'
            f'<title>{titolo}</title>{body}</svg>\n')


def salva(nome, contenuto):
    with open(os.path.join(OUT, nome), "w") as f:
        f.write(contenuto)


W, H = 600, 340

# 1. MBSR – percorsi di gruppo: tre figure su una collina, grande sole
b = f'<rect width="{W}" height="{H}" fill="{MENTA}"/>'
b += f'<circle cx="420" cy="120" r="88" fill="{ACQUA_T}"/>'
b += f'<path d="M0 240 Q150 190 300 220 T600 205 V340 H0Z" fill="{ACQUA}" opacity=".55"/>'
b += f'<path d="M0 300 Q200 270 380 292 T600 286 V340 H0Z" fill="{TEAL}" opacity=".9"/>'
b += figura(165, 300, 1.25, corpo=BLU, capelli=BLU)
b += figura(300, 292, 1.4, corpo=BLU2, capelli=BLU, stola=ACQUA)
b += figura(435, 302, 1.25, corpo=TEAL, capelli="#5a3b2a", stola=VERDE)
salva("corso-gruppo.svg", svg(W, H, b, "Tre persone meditano insieme su una collina"))

# 2. ADHD: figura con un filo che da groviglio diventa onda calma
b = f'<rect width="{W}" height="{H}" fill="{VERDE_T}"/>'
b += f'<circle cx="130" cy="110" r="70" fill="#ffffff" opacity=".7"/>'
b += (f'<path d="M60 150 C90 90 140 190 170 120 S220 80 200 150 S150 170 190 110 '
      f'C240 60 260 140 300 120 S380 110 420 118 S520 126 560 120" '
      f'stroke="{BLU}" stroke-width="3.5" fill="none" stroke-linecap="round"/>')
b += f'<path d="M0 295 Q300 265 600 295 V340 H0Z" fill="{VERDE}" opacity=".9"/>'
b += figura(300, 300, 1.55, corpo=TEAL, capelli=BLU, stola=VERDE)
salva("corso-adhd.svg", svg(W, H, b, "Una persona medita mentre un filo aggrovigliato diventa un'onda calma"))

# 3. Aziende: persone in piedi con nuvoletta di dialogo (richiamo al logo)
b = f'<rect width="{W}" height="{H}" fill="{MENTA}"/>'
b += f'<g transform="translate(300 25) scale(1.05) translate(-330 -40)"><path d="M250 70 C250 30 330 22 360 50 C400 40 430 80 410 105 C420 140 360 150 340 128 C310 150 255 135 262 110 L240 128 L250 100Z" fill="{ACQUA}" opacity=".85"/>'
b += f'<path d="M318 78 C318 64 334 64 336 76 C338 64 354 64 354 78 C354 94 336 104 336 104 C336 104 318 94 318 78Z" fill="none" stroke="{BLU}" stroke-width="3"/></g>'
b += f'<rect x="0" y="305" width="{W}" height="35" fill="{TEAL}"/>'
b += manager_uomo(150, 305, 1.45, giacca=BLU2, cravatta=ACQUA)
b += manager_donna(235, 305, 1.5, tailleur=ACQUA, capelli="#5a3b2a", pettinatura="lunghi")
b += manager_uomo(370, 305, 1.5, giacca=BLU, cravatta=VERDE, capelli="#3a2a20")
b += manager_donna(455, 305, 1.42, tailleur=VERDE, capelli=BLU, pettinatura="caschetto")
salva("corso-aziende.svg", svg(W, H, b, "Due uomini in giacca e cravatta e due donne in tailleur, uniti da una nuvoletta di dialogo con un cuore"))

# 4. Sessioni individuali: una figura, grande cerchio, piccola pianta
b = f'<rect width="{W}" height="{H}" fill="{CREMA}"/>'
b += f'<circle cx="300" cy="150" r="135" fill="{VERDE_T}"/>'
b += f'<circle cx="300" cy="150" r="96" fill="{ACQUA_T}"/>'
b += f'<path d="M0 298 H600 V340 H0Z" fill="{VERDE}" opacity=".7"/>'
b += figura(300, 300, 1.6, corpo=BLU, capelli=BLU, stola=ACQUA)
b += f'<path d="M480 298 Q482 248 492 222 M490 258 Q514 240 520 214 M486 272 Q462 254 456 232" stroke="{TEAL}" stroke-width="4" fill="none" stroke-linecap="round"/>'
b += f'<path d="M466 298 L470 276 H510 L514 298Z" fill="{BLU2}"/>'
salva("corso-individuale.svg", svg(W, H, b, "Una persona medita da sola davanti a un grande cerchio"))

# ===== Icone benefici (cerchio con simbolo) =====
def icona(nome, simbolo, titolo, sfondo=ACQUA_T):
    b = f'<circle cx="60" cy="60" r="56" fill="{sfondo}"/>' + simbolo
    salva(nome, svg(120, 120, b, titolo))

icona("icona-respiro.svg",
      f'<path d="M24 52 Q44 40 60 52 T96 52" stroke="{BLU}" stroke-width="5" fill="none" stroke-linecap="round"/>'
      f'<path d="M30 70 Q48 58 64 70 T96 70" stroke="{TEAL}" stroke-width="5" fill="none" stroke-linecap="round"/>'
      f'<path d="M24 86 Q40 76 56 86" stroke="{BLU}" stroke-width="5" fill="none" stroke-linecap="round" opacity=".6"/>', "Respiro")
icona("icona-calma.svg",
      f'<path d="M60 92 C40 80 30 64 36 44 C48 52 56 62 60 74 C64 62 72 52 84 44 C90 64 80 80 60 92Z" fill="{TEAL}"/>'
      f'<path d="M60 92 C52 72 52 52 60 30 C68 52 68 72 60 92Z" fill="{BLU}"/>', "Calma", VERDE_T)
icona("icona-emozioni.svg",
      f'<path d="M60 94 C60 94 26 74 26 50 C26 36 44 28 60 44 C76 28 94 36 94 50 C94 74 60 94 60 94Z" fill="none" stroke="{BLU}" stroke-width="5"/>'
      f'<path d="M60 80 C60 80 40 68 40 54 C40 46 52 42 60 52 C68 42 80 46 80 54 C80 68 60 80 60 80Z" fill="{ACQUA}"/>', "Emozioni")
icona("icona-sonno.svg",
      f'<path d="M74 30 A32 32 0 1 0 90 74 A26 26 0 1 1 74 30Z" fill="{BLU}"/>'
      f'<circle cx="84" cy="36" r="4" fill="{TEAL}"/><circle cx="94" cy="52" r="3" fill="{TEAL}"/>', "Sonno", VERDE_T)
icona("icona-attenzione.svg",
      f'<circle cx="60" cy="60" r="32" fill="none" stroke="{BLU}" stroke-width="5"/>'
      f'<circle cx="60" cy="60" r="18" fill="none" stroke="{TEAL}" stroke-width="5"/>'
      f'<circle cx="60" cy="60" r="6" fill="{BLU}"/>', "Attenzione")
icona("icona-gentilezza.svg",
      f'<path d="M30 74 Q30 58 46 58 L60 66 L74 58 Q90 58 90 74 Q76 92 60 92 Q44 92 30 74Z" fill="{TEAL}"/>'
      f'<path d="M60 52 C60 52 46 44 46 34 C46 28 54 26 60 33 C66 26 74 28 74 34 C74 44 60 52 60 52Z" fill="{BLU}"/>', "Gentilezza", VERDE_T)
print("ok")


# ===== Copertina blog: "Svegliarsi dal pilota automatico" =====
import math

def ingranaggio(cx, cy, r, denti, colore, foro=MENTA, rot=0):
    """Ruota dentata semplice."""
    pts = []
    n = denti * 4
    for i in range(n):
        a = math.radians(rot) + 2 * math.pi * i / n
        rr = r + 9 if (i % 4) in (1, 2) else r
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    g = f'<polygon points="{" ".join(pts)}" fill="{colore}"/>'
    g += f'<circle cx="{cx}" cy="{cy}" r="{r * .38:.1f}" fill="{foro}"/>'
    return g

GRIGIO = "#9fb1c2"
GRIGIO_S = "#7f93a8"
b = f'<rect width="{W}" height="{H}" fill="{MENTA}"/>'
# metà sinistra: il "pilota automatico" (ingranaggi grigi, nastro trasportatore, figura grigia)
b += f'<rect width="300" height="{H}" fill="#e6ecf1"/>'
b += ingranaggio(58, 52, 28, 9, GRIGIO, "#e6ecf1", 8)
b += ingranaggio(112, 70, 16, 7, GRIGIO_S, "#e6ecf1", 20)
b += ingranaggio(250, 50, 24, 8, GRIGIO, "#e6ecf1", 0)
b += f'<rect x="20" y="268" width="280" height="14" rx="7" fill="{GRIGIO_S}"/>'
for x in range(40, 300, 40):
    b += f'<circle cx="{x}" cy="275" r="4" fill="#e6ecf1"/>'
b += figura_in_piedi(105, 268, 1.25, corpo=GRIGIO_S, capelli=GRIGIO_S, pelle="#c9d3dc", gambe="#6c7f93")
b += figura_in_piedi(200, 268, 1.25, corpo=GRIGIO, capelli=GRIGIO_S, pelle="#c9d3dc", gambe="#6c7f93")
# metà destra: la presenza (sole, prato, fiore, figura a colori che si ferma e respira)
b += f'<circle cx="470" cy="105" r="62" fill="{ACQUA_T}"/>'
b += f'<path d="M300 280 Q450 250 600 272 V340 H300Z" fill="{VERDE}" opacity=".85"/>'
b += f'<rect x="0" y="282" width="300" height="58" fill="#d5dee6"/>'
# respiro: onde leggere che escono dalla figura
b += f'<path d="M418 128 Q440 116 462 128 T506 128" stroke="{TEAL}" stroke-width="3.5" fill="none" stroke-linecap="round" opacity=".8"/>'
b += f'<path d="M426 108 Q446 98 466 108 T506 108" stroke="{BLU}" stroke-width="3" fill="none" stroke-linecap="round" opacity=".55"/>'
b += figura_in_piedi(400, 276, 1.35, corpo=ACQUA, capelli=BLU)
# fiore con cuore, che la figura guarda
b += f'<path d="M500 276 Q498 248 504 228" stroke="{TEAL}" stroke-width="4" fill="none" stroke-linecap="round"/>'
b += f'<path d="M502 252 Q520 242 526 230 Q508 232 502 252Z" fill="{TEAL}"/>'
b += f'<path d="M504 220 C504 220 488 210 488 199 C488 192 497 189 504 197 C511 189 520 192 520 199 C520 210 504 220 504 220Z" fill="{BLU}"/>'
# soglia tra i due mondi: passi tratteggiati
b += f'<path d="M282 262 Q320 250 356 262" stroke="{BLU}" stroke-width="3" fill="none" stroke-dasharray="2 9" stroke-linecap="round"/>'
salva("blog-pilota-automatico.svg", svg(W, H, b, "Da un lato ingranaggi e persone grigie in automatico, dall'altro una persona a colori che si ferma, respira e guarda un fiore"))


# ===== Copertina blog: "MBSR: la Mindfulness che ridisegna il cervello e la vita" – fiore di loto =====
def petalo(cx, cy, h, w, angolo, colore, opacita=1):
    """Petalo a goccia con la base in (cx, cy), ruotato di 'angolo' gradi."""
    d = f"M0 0 C{w} {-h*0.35} {w*0.55} {-h*0.85} 0 {-h} C{-w*0.55} {-h*0.85} {-w} {-h*0.35} 0 0Z"
    return (f'<path d="{d}" fill="{colore}" opacity="{opacita}" '
            f'transform="translate({cx} {cy}) rotate({angolo})"/>')

CX, CY = 300, 232
b = f'<rect width="{W}" height="{H}" fill="{MENTA}"/>'
# sole / luna dietro al fiore
b += f'<circle cx="{CX}" cy="150" r="118" fill="{VERDE_T}"/>'
b += f'<circle cx="{CX}" cy="150" r="84" fill="#ffffff" opacity=".65"/>'
# acqua
b += f'<rect x="0" y="{CY}" width="{W}" height="{H-CY}" fill="{ACQUA_T}"/>'
b += f'<path d="M0 {CY} Q150 {CY-8} 300 {CY} T600 {CY} V{CY+6} H0Z" fill="{ACQUA}" opacity=".35"/>'
# cerchi sull'acqua (onde concentriche)
for rx, op in ((150, .55), (215, .35), (280, .22)):
    b += f'<ellipse cx="{CX}" cy="{CY+30}" rx="{rx}" ry="{rx*0.1:.0f}" fill="none" stroke="{TEAL}" stroke-width="2.5" opacity="{op}"/>'
# foglie di loto galleggianti
b += f'<ellipse cx="135" cy="{CY+48}" rx="62" ry="13" fill="{TEAL}"/><path d="M135 {CY+48} L190 {CY+40} L188 {CY+50}Z" fill="{ACQUA_T}"/>'
b += f'<ellipse cx="472" cy="{CY+60}" rx="52" ry="11" fill="{TEAL}" opacity=".85"/><path d="M472 {CY+60} L420 {CY+53} L422 {CY+63}Z" fill="{ACQUA_T}"/>'
# fiore di loto: petali esterni, intermedi e centrali
b += petalo(CX, CY+10, 92, 30, -72, BLU2)
b += petalo(CX, CY+10, 92, 30, 72, BLU2)
b += petalo(CX, CY+8, 112, 34, -46, TEAL)
b += petalo(CX, CY+8, 112, 34, 46, TEAL)
b += petalo(CX, CY+6, 128, 36, -22, ACQUA)
b += petalo(CX, CY+6, 128, 36, 22, ACQUA)
b += petalo(CX, CY+4, 138, 38, 0, VERDE)
# venature leggere sul petalo centrale e cuore del fiore
b += f'<path d="M{CX} {CY-4} L{CX} {CY-112}" stroke="{TEAL}" stroke-width="2" opacity=".5"/>'
b += f'<ellipse cx="{CX}" cy="{CY+8}" rx="46" ry="10" fill="{BLU}"/>'
# otto piccoli cerchi: le otto settimane del percorso
for i in range(8):
    x = CX - 105 + i * 30
    b += f'<circle cx="{x}" cy="{CY+84}" r="5.5" fill="{BLU}" opacity="{0.35 + i*0.08:.2f}"/>'
salva("blog-mbsr-loto.svg", svg(W, H, b, "Un fiore di loto stilizzato si apre sull'acqua davanti a un grande cerchio; sotto, otto piccoli cerchi come le otto settimane del percorso"))

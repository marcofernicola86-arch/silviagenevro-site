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


def figura_in_piedi(x, y, s=1.0, corpo=BLU, capelli=BLU, pelle=PELLE):
    g = f'<g transform="translate({x} {y}) scale({s})">'
    g += f'<path d="M-9 0 L-7 -48 L7 -48 L9 0 L3 0 L0 -36 L-3 0Z" fill="{BLU}"/>'
    g += f'<path d="M-16 -46 L-13 -96 Q0 -104 13 -96 L16 -46 Q0 -42 -16 -46Z" fill="{corpo}"/>'
    g += f'<rect x="-4" y="-106" width="8" height="10" rx="3" fill="{pelle}"/>'
    g += f'<circle cx="0" cy="-116" r="11" fill="{pelle}"/>'
    g += f'<path d="M-11.5 -116 Q-12 -129 0 -129 Q12 -129 11.5 -116 Q7 -123 0 -123 Q-7 -123 -11.5 -116Z" fill="{capelli}"/>'
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
b += figura_in_piedi(150, 305, 1.45, corpo=BLU2)
b += figura_in_piedi(235, 305, 1.55, corpo=ACQUA, capelli="#5a3b2a")
b += figura_in_piedi(370, 305, 1.5, corpo=BLU)
b += figura_in_piedi(455, 305, 1.42, corpo=VERDE, capelli=BLU)
salva("corso-aziende.svg", svg(W, H, b, "Colleghi in piedi uniti da una nuvoletta di dialogo con un cuore"))

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

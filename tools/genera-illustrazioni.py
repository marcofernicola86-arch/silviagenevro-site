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

# 5. Mindset e soft skills: un cervello simpatico che si allena (fascia e manubri)
def scintilla(cx, cy, r, colore):
    return (f'<path d="M{cx} {cy-r} Q{cx+r*.18} {cy-r*.18} {cx+r} {cy} Q{cx+r*.18} {cy+r*.18} {cx} {cy+r} '
            f'Q{cx-r*.18} {cy+r*.18} {cx-r} {cy} Q{cx-r*.18} {cy-r*.18} {cx} {cy-r}Z" fill="{colore}"/>')
def manubrio(cx, cy, ang):
    return (f'<g transform="rotate({ang} {cx} {cy})">'
            f'<rect x="{cx-22}" y="{cy-5}" width="44" height="10" rx="5" fill="{BLU}"/>'
            f'<rect x="{cx-40}" y="{cy-22}" width="20" height="44" rx="8" fill="{TEAL}" stroke="{BLU}" stroke-width="3"/>'
            f'<rect x="{cx+20}" y="{cy-22}" width="20" height="44" rx="8" fill="{TEAL}" stroke="{BLU}" stroke-width="3"/></g>')
b = f'<rect width="{W}" height="{H}" fill="{MENTA}"/>'
b += f'<circle cx="300" cy="168" r="140" fill="{VERDE_T}"/>'
b += f'<circle cx="300" cy="168" r="104" fill="{ACQUA_T}"/>'
b += f'<path d="M0 300 Q300 278 600 300 V340 H0Z" fill="{TEAL}" opacity=".85"/>'
# gambette
b += f'<path d="M278 236 V286 H266 M322 236 V286 H334" stroke="{BLU}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
# braccia alzate verso i manubri
b += f'<path d="M218 168 Q188 140 180 96" stroke="{BLU}" stroke-width="6" fill="none" stroke-linecap="round"/>'
b += f'<path d="M382 168 Q412 140 420 96" stroke="{BLU}" stroke-width="6" fill="none" stroke-linecap="round"/>'
b += manubrio(180, 80, -15) + manubrio(420, 80, 15)
# sagoma morbida del cervello
lobi = [(236,176,40),(250,136,40),(286,112,42),(326,116,42),(358,140,38),(366,180,36),(336,212,38),(292,218,40),(254,208,38),(300,168,62)]
b += "".join(f'<circle cx="{x}" cy="{y}" r="{r+4}" fill="{BLU}"/>' for x, y, r in lobi)
b += "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{ACQUA}"/>' for x, y, r in lobi)
# riflesso di luce e qualche piega
b += f'<path d="M258 118 Q276 100 300 104" stroke="#ffffff" stroke-width="6" fill="none" stroke-linecap="round" opacity=".7"/>'
b += f'<path d="M302 84 Q296 106 304 126" stroke="{BLU}" stroke-width="4" fill="none" stroke-linecap="round" opacity=".75"/>'
b += f'<path d="M230 196 Q246 186 244 170 M372 168 Q356 176 360 196 M346 226 Q350 212 364 208" stroke="{BLU}" stroke-width="4" fill="none" stroke-linecap="round" opacity=".75"/>'
# fascia sportiva
b += f'<path d="M222 140 Q300 112 378 140 L374 158 Q300 132 226 158Z" fill="{VERDE}" stroke="{BLU}" stroke-width="3.5" stroke-linejoin="round"/>'
# visetto
b += f'<circle cx="276" cy="184" r="10" fill="{BLU}"/><circle cx="324" cy="184" r="10" fill="{BLU}"/>'
b += f'<circle cx="279" cy="181" r="2.6" fill="#ffffff"/><circle cx="327" cy="181" r="2.6" fill="#ffffff"/>'
b += f'<path d="M290 198 Q300 208 310 198" stroke="{BLU}" stroke-width="4" fill="none" stroke-linecap="round"/>'
b += f'<ellipse cx="258" cy="200" rx="9" ry="5" fill="#ffb3c4" opacity=".95"/><ellipse cx="342" cy="200" rx="9" ry="5" fill="#ffb3c4" opacity=".95"/>'
# scintille
b += scintilla(150, 150, 14, VERDE) + scintilla(456, 160, 14, VERDE) + scintilla(470, 236, 9, TEAL)
b += scintilla(132, 232, 9, TEAL) + scintilla(300, 40, 9, TEAL)
salva("corso-mindset.svg", svg(W, H, b, "Un cervello sorridente con la fascia sportiva che solleva due manubri"))

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


# ===== Icone della pagina "Mindfulness in azienda" (diverse da quelle della home) =====
icona("icona-dialogo.svg",
      f'<path d="M24 34 h44 a8 8 0 0 1 8 8 v18 a8 8 0 0 1 -8 8 h-26 l-12 10 v-10 h-6 a8 8 0 0 1 -8 -8 v-18 a8 8 0 0 1 8 -8Z" fill="{BLU}"/>'
      f'<path d="M58 54 h30 a8 8 0 0 1 8 8 v14 a8 8 0 0 1 -8 8 h-4 v9 l-11 -9 h-15 a8 8 0 0 1 -8 -8 v-14 a8 8 0 0 1 8 -8Z" fill="{TEAL}"/>'
      f'<circle cx="34" cy="51" r="3.2" fill="#fff"/><circle cx="46" cy="51" r="3.2" fill="#fff"/><circle cx="58" cy="51" r="3.2" fill="#fff"/>', "Comunicazione")
icona("icona-ascolto.svg",
      f'<path d="M64 26 C46 26 36 40 36 54 C36 64 42 68 46 74 C50 80 46 92 58 94 C66 95 70 88 70 82" fill="none" stroke="{BLU}" stroke-width="7" stroke-linecap="round"/>'
      f'<path d="M50 54 C50 44 56 38 64 38 C72 38 78 44 78 52 C78 60 70 62 68 68" fill="none" stroke="{TEAL}" stroke-width="6" stroke-linecap="round"/>'
      f'<path d="M86 40 q8 14 0 28 M94 34 q12 20 0 40" fill="none" stroke="{TEAL}" stroke-width="4" stroke-linecap="round" opacity=".7"/>', "Ascolto", VERDE_T)
icona("icona-squadra.svg",
      f'<circle cx="60" cy="40" r="10" fill="{BLU}"/><path d="M42 74 a18 18 0 0 1 36 0Z" fill="{BLU}"/>'
      f'<circle cx="34" cy="52" r="8" fill="{TEAL}"/><path d="M20 82 a14 14 0 0 1 28 0Z" fill="{TEAL}"/>'
      f'<circle cx="86" cy="52" r="8" fill="{TEAL}"/><path d="M72 82 a14 14 0 0 1 28 0Z" fill="{TEAL}"/>'
      f'<path d="M30 92 Q60 104 90 92" fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"/>', "Squadra")
icona("icona-empatia.svg",
      f'<path d="M48 88 C48 88 22 72 22 54 C22 44 36 38 48 50 C60 38 74 44 74 54 C74 72 48 88 48 88Z" fill="{TEAL}"/>'
      f'<path d="M74 84 C74 84 52 70 52 55 C52 47 64 42 74 52 C84 42 96 47 96 55 C96 70 74 84 74 84Z" fill="{BLU}" opacity=".92"/>', "Empatia", VERDE_T)
icona("icona-equilibrio.svg",
      f'<ellipse cx="60" cy="88" rx="30" ry="9" fill="{BLU}"/>'
      f'<ellipse cx="60" cy="70" rx="22" ry="8" fill="{TEAL}"/>'
      f'<ellipse cx="60" cy="55" rx="15" ry="6.5" fill="{BLU}" opacity=".85"/>'
      f'<path d="M60 47 C52 38 52 28 60 22 C68 28 68 38 60 47Z" fill="{TEAL}"/>', "Equilibrio")
icona("icona-maschere.svg",
      f'<path d="M24 34 Q44 26 62 34 L60 60 Q56 80 43 82 Q30 80 26 60Z" fill="{BLU}"/>'
      f'<path d="M34 50 q4 -4 8 0 M48 50 q4 -4 8 0" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>'
      f'<path d="M36 64 Q43 72 50 64" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>'
      f'<path d="M58 42 Q76 34 96 42 L94 68 Q90 88 77 90 Q64 88 60 68Z" fill="{TEAL}"/>'
      f'<path d="M68 58 q4 3 8 0 M82 58 q4 3 8 0" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>'
      f'<circle cx="77" cy="76" r="4" fill="#fff"/>', "Tecniche teatrali", VERDE_T)


# ===== Icone della pagina "Percorso Mindfulness per ADHD" =====
icona("icona-filo-attenzione.svg",
      f'<path d="M22 70 C22 50 44 46 44 62 C44 76 26 74 30 58 C34 42 58 42 56 60 C54 74 38 72 44 58 C50 46 66 52 64 62 C62 70 70 62 98 62" fill="none" stroke="{BLU}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>'
      f'<circle cx="96" cy="60" r="6" fill="{TEAL}"/>', "Attenzione")
icona("icona-pausa.svg",
      f'<circle cx="60" cy="60" r="30" fill="none" stroke="{BLU}" stroke-width="5"/>'
      f'<rect x="48" y="45" width="8" height="30" rx="3" fill="{TEAL}"/><rect x="64" y="45" width="8" height="30" rx="3" fill="{TEAL}"/>', "Pausa", VERDE_T)
icona("icona-onda.svg",
      f'<path d="M20 72 C32 52 44 52 52 66 C60 80 72 80 80 62 C86 50 94 48 100 52" fill="none" stroke="{BLU}" stroke-width="6" stroke-linecap="round"/>'
      f'<path d="M20 86 C36 78 52 90 68 84 S92 78 100 82" fill="none" stroke="{TEAL}" stroke-width="5" stroke-linecap="round" opacity=".8"/>'
      f'<circle cx="76" cy="36" r="9" fill="{TEAL}"/>', "Emozioni")
icona("icona-bussola.svg",
      f'<circle cx="60" cy="60" r="32" fill="none" stroke="{BLU}" stroke-width="5"/>'
      f'<path d="M60 34 L68 60 L60 86 L52 60Z" fill="{TEAL}"/><path d="M60 34 L68 60 L52 60Z" fill="{BLU}"/>'
      f'<circle cx="60" cy="60" r="4" fill="#fff"/>', "Orientamento")
icona("icona-sole.svg",
      f'<circle cx="60" cy="60" r="16" fill="{TEAL}"/>'
      + ''.join(f'<path d="M{60+26*__import__("math").cos(a):.1f} {60+26*__import__("math").sin(a):.1f} L{60+36*__import__("math").cos(a):.1f} {60+36*__import__("math").sin(a):.1f}" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>' for a in [i*0.7854 for i in range(8)]),
      "Fiducia in sé", VERDE_T)
icona("icona-corpo.svg",
      f'<circle cx="60" cy="34" r="9" fill="{BLU}"/>'
      f'<path d="M60 46 C50 46 44 54 44 62 L44 70 M60 46 C70 46 76 54 76 62 L76 70" fill="none" stroke="{BLU}" stroke-width="6" stroke-linecap="round"/>'
      f'<path d="M60 46 L60 76 M60 76 L48 94 M60 76 L72 94" fill="none" stroke="{BLU}" stroke-width="6" stroke-linecap="round"/>'
      f'<path d="M30 58 q-6 8 0 16 M90 58 q6 8 0 16" fill="none" stroke="{TEAL}" stroke-width="4" stroke-linecap="round"/>', "Corpo e respiro")


# ===== I 7 pilastri della Mindfulness (Jon Kabat-Zinn) – pagina MBSR =====
icona("pilastro-non-giudizio.svg",   # occhio aperto e sereno
      f'<path d="M22 60 Q60 28 98 60 Q60 92 22 60Z" fill="none" stroke="{BLU}" stroke-width="5" stroke-linejoin="round"/>'
      f'<circle cx="60" cy="60" r="12" fill="{TEAL}"/><circle cx="60" cy="60" r="4.5" fill="#fff"/>', "Non giudizio")
icona("pilastro-pazienza.svg",       # clessidra
      f'<path d="M40 28 H80 M40 92 H80" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>'
      f'<path d="M44 30 C44 50 58 54 60 60 C62 66 76 70 76 90 M76 30 C76 50 62 54 60 60 C58 66 44 70 44 90" fill="none" stroke="{BLU}" stroke-width="4.5" stroke-linecap="round"/>'
      f'<path d="M50 84 Q60 72 70 84Z" fill="{TEAL}"/><path d="M52 40 H68 Q62 50 60 52 Q58 50 52 40Z" fill="{TEAL}" opacity=".6"/>', "Pazienza", VERDE_T)
icona("pilastro-mente-principiante.svg",  # germoglio
      f'<path d="M60 92 V58" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>'
      f'<path d="M60 64 C46 64 36 54 36 40 C50 40 60 50 60 64Z" fill="{TEAL}"/>'
      f'<path d="M60 56 C60 42 70 32 86 32 C86 46 76 56 60 56Z" fill="{BLU}"/>'
      f'<path d="M40 92 H80" stroke="{TEAL}" stroke-width="4" stroke-linecap="round"/>', "Mente del principiante")
icona("pilastro-fiducia.svg",        # mani che sostengono un cuore
      f'<path d="M24 66 Q30 88 60 90 Q90 88 96 66 Q84 74 72 72 L60 80 L48 72 Q36 74 24 66Z" fill="{TEAL}"/>'
      f'<path d="M60 64 C60 64 42 54 42 42 C42 34 52 30 60 39 C68 30 78 34 78 42 C78 54 60 64 60 64Z" fill="{BLU}"/>', "Fiducia", VERDE_T)
icona("pilastro-non-cercare.svg",    # foglia che galleggia sull'acqua, senza sforzo
      f'<path d="M22 74 Q36 66 50 74 T78 74 T98 72" fill="none" stroke="{TEAL}" stroke-width="4.5" stroke-linecap="round"/>'
      f'<path d="M22 88 Q38 80 54 88 T86 88" fill="none" stroke="{TEAL}" stroke-width="3.5" stroke-linecap="round" opacity=".6"/>'
      f'<path d="M40 64 C46 44 70 38 86 44 C80 62 58 70 40 64Z" fill="{BLU}"/><path d="M42 63 C56 56 68 50 84 45" stroke="#fff" stroke-width="2.2" fill="none"/>', "Non cercare risultati")
icona("pilastro-accettazione.svg",   # braccia aperte che accolgono
      f'<circle cx="60" cy="38" r="9" fill="{BLU}"/>'
      f'<path d="M60 50 V80 M60 80 L50 96 M60 80 L70 96" stroke="{BLU}" stroke-width="5.5" stroke-linecap="round" fill="none"/>'
      f'<path d="M60 56 Q44 54 30 40 M60 56 Q76 54 90 40" stroke="{TEAL}" stroke-width="5.5" stroke-linecap="round" fill="none"/>', "Accettazione", VERDE_T)
icona("pilastro-lasciar-andare.svg", # mano aperta e foglia che vola via
      f'<path d="M28 84 Q44 92 64 86 L86 76 Q92 72 88 68 Q84 66 78 70 L66 74" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
      f'<path d="M28 84 L30 70 Q46 64 64 74" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
      f'<path d="M58 50 C62 34 78 26 92 30 C88 46 72 54 58 50Z" fill="{TEAL}"/>'
      f'<path d="M46 56 q4 -6 10 -6" stroke="{TEAL}" stroke-width="3" fill="none" stroke-linecap="round" stroke-dasharray="2 5"/>', "Lasciar andare")


# ===== Icone della pagina "Sessioni individuali" =====
icona("sessione-centratura.svg",     # cerchi concentrici morbidi attorno a un punto
      f'<circle cx="60" cy="60" r="30" fill="none" stroke="{TEAL}" stroke-width="3.5" opacity=".55"/>'
      f'<circle cx="60" cy="60" r="19" fill="none" stroke="{BLU}" stroke-width="4"/>'
      f'<circle cx="60" cy="60" r="7" fill="{TEAL}"/>', "Centratura")
icona("sessione-quotidiano.svg",     # tazza fumante: la presenza nelle piccole cose
      f'<path d="M34 54 H78 V70 A18 18 0 0 1 60 88 H52 A18 18 0 0 1 34 70Z" fill="{BLU}"/>'
      f'<path d="M78 58 Q92 58 92 68 Q92 78 78 76" fill="none" stroke="{BLU}" stroke-width="5"/>'
      f'<path d="M46 46 q-6 -8 0 -14 M58 46 q-6 -8 0 -14 M70 46 q-6 -8 0 -14" fill="none" stroke="{TEAL}" stroke-width="3.5" stroke-linecap="round"/>', "Presenza nel quotidiano", VERDE_T)
icona("sessione-nuvola-sole.svg",    # nuvola che lascia passare il sole: stress ed emozioni
      f'<circle cx="74" cy="44" r="14" fill="{TEAL}"/>'
      f'<path d="M30 82 H82 A14 14 0 0 0 80 54 A18 18 0 0 0 46 56 A13 13 0 0 0 30 82Z" fill="{BLU}"/>', "Stress ed emozioni")
icona("sessione-mano-cuore.svg",     # cuore accolto da una mano a coppa: autocompassione
      f'<path d="M60 66 C60 66 42 55 42 43 C42 35 52 31 60 40 C68 31 78 35 78 43 C78 55 60 66 60 66Z" fill="{TEAL}"/>'
      f'<path d="M30 66 Q34 86 60 86 Q86 86 90 66 Q82 74 70 74 L50 74 Q38 74 30 66Z" fill="{BLU}"/>', "Autocompassione", VERDE_T)
icona("sessione-sentiero.svg",       # sentiero che sale verso un sole: il cambiamento
      f'<circle cx="80" cy="36" r="9" fill="{TEAL}"/>'
      f'<path d="M36 94 C44 78 74 78 66 64 C60 54 44 56 54 44" fill="none" stroke="{BLU}" stroke-width="6" stroke-linecap="round"/>'
      f'<path d="M36 94 C44 78 74 78 66 64 C60 54 44 56 54 44" fill="none" stroke="#fff" stroke-width="1.6" stroke-dasharray="3 6" stroke-linecap="round"/>', "Cambiamento personale")


# =====================================================================
# ===== ILLUSTRAZIONI GRANDI – STILE "CARTOON" (come il cervello) =====
# Contorno blu spesso, alone tondo dietro, scintille, collina petrolio,
# personaggi simpatici con visetto e guance rosa.
# =====================================================================
import math
CONT = BLU          # colore del contorno
GUANCE = "#ffb3c4"
SW = 3.5            # spessore del contorno (prima della scala)

def _c(sw=SW):
    return f'stroke="{CONT}" stroke-width="{sw}" stroke-linejoin="round"'

def sfondo_cartoon(cx=300, cy=160, r=140, fondo=MENTA, collina=True):
    b = f'<rect width="{W}" height="{H}" fill="{fondo}"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{VERDE_T}"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{r*0.74:.0f}" fill="{ACQUA_T}"/>'
    return b

def collina_cartoon(y=300, colore=TEAL):
    return f'<path d="M0 {y} Q300 {y-22} 600 {y} V340 H0Z" fill="{colore}" opacity=".85"/>'

def viso(cy, aperti=False, r=1.0, dx=0):
    """Visetto: occhi (chiusi = meditazione, aperti = con riflesso), sorriso, guance."""
    g = ""
    ex, ey = 11 * r, cy
    if aperti == "assonnato":       # occhi a lineetta e bocca dritta: il "pilota automatico"
        for sx in (-1, 1):
            x = dx + sx * ex
            g += f'<path d="M{x-5*r:.1f} {ey+1:.1f} H{x+5*r:.1f}" stroke="{CONT}" stroke-width="3" stroke-linecap="round"/>'
        g += f'<path d="M{dx-4*r:.1f} {cy+11*r:.1f} H{dx+4*r:.1f}" stroke="{CONT}" stroke-width="3" stroke-linecap="round"/>'
        return g
    if aperti:
        for sx in (-1, 1):
            g += f'<circle cx="{dx+sx*ex:.1f}" cy="{ey:.1f}" r="{5*r:.1f}" fill="{CONT}"/>'
            g += f'<circle cx="{dx+sx*ex+1.6*r:.1f}" cy="{ey-1.8*r:.1f}" r="{1.7*r:.1f}" fill="#ffffff"/>'
    else:
        for sx in (-1, 1):
            x = dx + sx * ex
            g += f'<path d="M{x-5*r:.1f} {ey:.1f} Q{x:.1f} {ey+5*r:.1f} {x+5*r:.1f} {ey:.1f}" stroke="{CONT}" stroke-width="3" fill="none" stroke-linecap="round"/>'
    g += f'<path d="M{dx-5*r:.1f} {cy+9*r:.1f} Q{dx:.1f} {cy+14*r:.1f} {dx+5*r:.1f} {cy+9*r:.1f}" stroke="{CONT}" stroke-width="3" fill="none" stroke-linecap="round"/>'
    for sx in (-1, 1):
        g += f'<ellipse cx="{dx+sx*19*r:.1f}" cy="{cy+7*r:.1f}" rx="{5.5*r:.1f}" ry="{3.4*r:.1f}" fill="{GUANCE}" opacity=".95"/>'
    return g

def testa(cy, capelli, pettinatura, pelle=PELLE, aperti=False, R=27):
    g = ""
    if pettinatura == "lunghi":      # capelli lunghi, dietro la testa
        g += f'<path d="M{-R-4} {cy} Q{-R-6} {cy-R-8} 0 {cy-R-8} Q{R+6} {cy-R-8} {R+4} {cy} L{R+6} {cy+R+6} Q{R-6} {cy+R+10} {R-10} {cy+R} H{-R+10} Q{-R+6} {cy+R+10} {-R-6} {cy+R+6}Z" fill="{capelli}" {_c()}/>'
    if pettinatura == "chignon":
        g += f'<circle cx="0" cy="{cy-R-6}" r="11" fill="{capelli}" {_c()}/>'
    g += f'<circle cx="0" cy="{cy}" r="{R}" fill="{pelle}" {_c()}/>'
    if pettinatura in ("chignon", "lunghi"):
        g += f'<path d="M{-R} {cy-2} Q{-R-1} {cy-R-2} 0 {cy-R-2} Q{R+1} {cy-R-2} {R} {cy-2} Q{R*0.6:.0f} {cy-R*0.55:.0f} 4 {cy-R*0.62:.0f} Q{-R*0.6:.0f} {cy-R*0.55:.0f} {-R} {cy-2}Z" fill="{capelli}" {_c()}/>'
    elif pettinatura == "caschetto":
        g += f'<path d="M{-R-3} {cy+10} Q{-R-5} {cy-R-4} 0 {cy-R-4} Q{R+5} {cy-R-4} {R+3} {cy+10} L{R-4} {cy+10} L{R-6} {cy-R*0.45:.0f} H{-R+6} L{-R+4} {cy+10}Z" fill="{capelli}" {_c()}/>'
    else:                             # corti (uomo)
        g += f'<path d="M{-R} {cy-4} Q{-R-1} {cy-R-4} 0 {cy-R-4} Q{R+1} {cy-R-4} {R} {cy-4} Q{R*0.7:.0f} {cy-R*0.6:.0f} {R*0.2:.0f} {cy-R*0.6:.0f} Q{-R*0.5:.0f} {cy-R*0.62:.0f} {-R} {cy-4}Z" fill="{capelli}" {_c()}/>'
    g += viso(cy + 3, aperti)
    return g

def meditante(x, y, s=1.0, corpo=BLU2, capelli=BLU, stola=ACQUA, pettinatura="chignon", pelle=PELLE, aperti=False):
    """Personaggio seduto in meditazione. (x, y) = punto a terra al centro."""
    g = f'<g transform="translate({x} {y}) scale({s})">'
    g += f'<path d="M-50 -2 Q-50 -30 -18 -32 H18 Q50 -30 50 -2 Q26 6 0 4 Q-26 6 -50 -2Z" fill="{corpo}" {_c()}/>'   # gambe incrociate
    g += f'<path d="M-27 -28 Q-30 -76 0 -78 Q30 -76 27 -28 Q0 -22 -27 -28Z" fill="{corpo}" {_c()}/>'            # busto
    if stola:
        g += f'<path d="M-20 -70 Q0 -82 20 -70 L13 -52 Q0 -58 -13 -52Z" fill="{stola}" {_c()}/>'
    for sx in (-1, 1):                                                                                          # braccia
        g += f'<path d="M{sx*22} -68 Q{sx*42} -50 {sx*38} -26" stroke="{CONT}" stroke-width="15" fill="none" stroke-linecap="round"/>'
        g += f'<path d="M{sx*22} -68 Q{sx*42} -50 {sx*38} -26" stroke="{corpo}" stroke-width="8" fill="none" stroke-linecap="round"/>'
        g += f'<circle cx="{sx*38}" cy="-24" r="7" fill="{pelle}" {_c()}/>'
    g += testa(-106, capelli, pettinatura, pelle, aperti)
    g += "</g>"
    return g

def in_piedi(x, y, s=1.0, abito=BLU2, capelli=BLU, pettinatura="corti", cravatta=None, gonna=False, pelle=PELLE, gambe=BLU, aperti=True):
    """Personaggio in piedi (giacca/tailleur). (x, y) = punto a terra al centro."""
    g = f'<g transform="translate({x} {y}) scale({s})">'
    if gonna:
        g += f'<rect x="-13" y="-34" width="9" height="34" rx="4" fill="{pelle}" {_c()}/><rect x="4" y="-34" width="9" height="34" rx="4" fill="{pelle}" {_c()}/>'
        g += f'<path d="M-24 -30 L-20 -58 H20 L24 -30Z" fill="{abito}" {_c()}/>'
    else:
        g += f'<rect x="-16" y="-44" width="14" height="44" rx="6" fill="{gambe}" {_c()}/><rect x="2" y="-44" width="14" height="44" rx="6" fill="{gambe}" {_c()}/>'
    g += f'<path d="M-26 -40 Q-28 -92 0 -94 Q28 -92 26 -40 Q0 -34 -26 -40Z" fill="{abito}" {_c()}/>'            # giacca
    g += f'<path d="M-9 -92 L0 -76 L9 -92Z" fill="#ffffff" {_c(2.5)}/>'                        # colletto
    if cravatta:
        g += f'<path d="M-3.5 -86 H3.5 L5 -62 L0 -56 L-5 -62Z" fill="{cravatta}" {_c(2.5)}/>'
    else:
        g += f'<circle cx="0" cy="-64" r="2.4" fill="{CONT}"/><circle cx="0" cy="-52" r="2.4" fill="{CONT}"/>'
    for sx in (-1, 1):                                                                                          # braccia lungo i fianchi
        g += f'<path d="M{sx*22} -84 Q{sx*32} -66 {sx*30} -46" stroke="{CONT}" stroke-width="14" fill="none" stroke-linecap="round"/>'
        g += f'<path d="M{sx*22} -84 Q{sx*32} -66 {sx*30} -46" stroke="{abito}" stroke-width="7" fill="none" stroke-linecap="round"/>'
        g += f'<circle cx="{sx*30}" cy="-44" r="6.5" fill="{pelle}" {_c()}/>'
    g += testa(-122, capelli, pettinatura, pelle, aperti, R=26)
    g += "</g>"
    return g

def scintille(lista):
    return "".join(scintilla(x, y, r, c) for x, y, r, c in lista)

SCINTILLE = [(130, 120, 14, VERDE), (470, 120, 14, VERDE), (100, 220, 9, TEAL), (500, 226, 9, TEAL), (300, 30, 9, TEAL)]

# 1. MBSR – percorsi di gruppo: tre amici che meditano sulla collina
b = sfondo_cartoon(300, 170, 150)
b += collina_cartoon(300)
b += meditante(170, 298, 0.82, corpo=BLU2, capelli=BLU, stola=ACQUA, pettinatura="caschetto")
b += meditante(430, 298, 0.82, corpo=TEAL, capelli="#5a3b2a", stola=VERDE, pettinatura="corti")
b += meditante(300, 300, 0.95, corpo=BLU, capelli="#3a2a20", stola=VERDE, pettinatura="chignon")
b += scintille([(90, 110, 14, VERDE), (510, 110, 14, VERDE), (70, 220, 9, TEAL), (530, 220, 9, TEAL), (300, 28, 9, TEAL)])
salva("corso-gruppo.svg", svg(W, H, b, "Tre personaggi sorridenti meditano insieme su una collina"))

# 2. ADHD: un filo aggrovigliato sopra la testa che diventa un'onda calma
b = sfondo_cartoon(300, 170, 145, fondo=VERDE_T)
b += collina_cartoon(302, VERDE)
b += (f'<path d="M48 126 C78 66 128 166 158 96 S208 56 188 126 S138 146 178 86 '
      f'C228 36 248 116 288 96 S368 86 408 94 S508 102 552 96" '
      f'stroke="#ffffff" stroke-width="10" fill="none" stroke-linecap="round"/>')
b += (f'<path d="M48 126 C78 66 128 166 158 96 S208 56 188 126 S138 146 178 86 '
      f'C228 36 248 116 288 96 S368 86 408 94 S508 102 552 96" '
      f'stroke="{CONT}" stroke-width="4" fill="none" stroke-linecap="round"/>')
b += meditante(300, 300, 1.05, corpo=TEAL, capelli=BLU, stola=VERDE, pettinatura="chignon")
b += scintille([(110, 200, 13, TEAL), (490, 190, 13, TEAL), (470, 260, 8, BLU2), (130, 266, 8, BLU2)])
salva("corso-adhd.svg", svg(W, H, b, "Un personaggio sorridente medita mentre sopra di lui un filo aggrovigliato diventa un'onda calma"))

# 3. Aziende: quattro colleghi sorridenti e una nuvoletta con il cuore
b = sfondo_cartoon(300, 150, 150)
b += collina_cartoon(306)
b += (f'<path d="M250 70 C250 30 330 22 360 50 C400 40 430 80 410 105 C420 140 360 150 340 128 '
      f'C310 150 255 135 262 110 L240 128 L250 100Z" fill="{ACQUA}" {_c()} transform="translate(-30 -28)"/>')
b += (f'<path d="M318 78 C318 64 334 64 336 76 C338 64 354 64 354 78 C354 94 336 104 336 104 '
      f'C336 104 318 94 318 78Z" fill="{GUANCE}" {_c(3)} transform="translate(-30 -28)"/>')
b += in_piedi(140, 300, 0.92, abito=BLU2, capelli=BLU, pettinatura="corti", cravatta=ACQUA)
b += in_piedi(240, 300, 0.95, abito=ACQUA, capelli="#5a3b2a", pettinatura="lunghi", gonna=True)
b += in_piedi(360, 300, 0.95, abito=BLU, capelli="#3a2a20", pettinatura="corti", cravatta=VERDE)
b += in_piedi(460, 300, 0.92, abito=VERDE, capelli=BLU, pettinatura="caschetto", gonna=True)
b += scintille([(60, 120, 13, VERDE), (540, 110, 13, VERDE), (520, 200, 8, TEAL), (80, 210, 8, TEAL)])
salva("corso-aziende.svg", svg(W, H, b, "Due colleghi in giacca e cravatta e due colleghe in tailleur, sorridenti, sotto una nuvoletta con un cuore"))

# 4. Sessioni individuali: un personaggio nel suo alone, con una piantina
b = sfondo_cartoon(300, 160, 140, fondo=CREMA)
b += collina_cartoon(302, VERDE)
b += meditante(290, 300, 1.08, corpo=BLU, capelli=BLU, stola=ACQUA, pettinatura="chignon")
b += f'<path d="M478 266 Q480 222 490 198 M488 232 Q512 214 518 190 M484 246 Q460 228 454 206" stroke="{CONT}" stroke-width="9" fill="none" stroke-linecap="round"/>'
b += f'<path d="M478 266 Q480 222 490 198 M488 232 Q512 214 518 190 M484 246 Q460 228 454 206" stroke="{TEAL}" stroke-width="4" fill="none" stroke-linecap="round"/>'
b += f'<path d="M460 296 L465 264 H505 L510 296Z" fill="{BLU2}" {_c()}/>'
b += scintille([(110, 120, 14, VERDE), (470, 110, 12, TEAL), (120, 230, 9, TEAL), (300, 26, 9, TEAL)])
salva("corso-individuale.svg", svg(W, H, b, "Un personaggio sorridente medita da solo dentro un grande alone, accanto a una piantina"))

# 5. Workshop e retreat: montagne, sole, tenda e due amici che meditano
b = f'<rect width="{W}" height="{H}" fill="{CREMA}"/>'
b += f'<circle cx="440" cy="84" r="40" fill="{VERDE}" {_c()}/>'
b += f'<path d="M-20 250 L120 110 L210 190 L300 96 L420 214 L500 150 L620 250Z" fill="{ACQUA}" {_c()}/>'
b += f'<path d="M120 110 L148 138 L132 134 L120 148 L108 136 L92 138Z M300 96 L328 124 L312 120 L300 134 L288 122 L272 124Z" fill="#ffffff" {_c(2.5)}/>'
b += f'<path d="M-20 270 L90 180 L190 244 L330 160 L470 254 L560 206 L620 270Z" fill="{TEAL}" {_c()}/>'
b += f'<path d="M-10 268 Q300 240 610 268 V350 H-10Z" fill="{VERDE}" {_c()}/>'
b += f'<path d="M444 300 L490 226 L536 300Z" fill="{BLU2}" {_c()}/><path d="M490 226 L476 300 H504Z" fill="{ACQUA_T}" {_c(2.5)}/>'
b += f'<path d="M490 226 V210" stroke="{CONT}" stroke-width="3.5" stroke-linecap="round"/>'
for x, h in [(56, 50), (94, 38)]:
    b += f'<rect x="{x-4}" y="282" width="8" height="12" fill="{BLU2}" {_c(2.5)}/><path d="M{x} {282-h} L{x+18} 284 H{x-18}Z" fill="{TEAL}" {_c()}/>'
b += meditante(220, 310, 0.9, corpo=BLU, capelli=BLU, stola=ACQUA, pettinatura="chignon")
b += meditante(345, 310, 0.9, corpo=BLU2, capelli="#5a3b2a", stola=VERDE, pettinatura="corti")
b += scintille([(200, 50, 10, TEAL), (540, 150, 9, BLU2), (380, 40, 7, TEAL)])
salva("corso-retreat.svg", svg(W, H, b, "Due personaggi sorridenti meditano su un prato tra le montagne, accanto a una tenda"))

# 6. Blog "Svegliarsi dal pilota automatico": a sinistra ingranaggi grigi e un personaggio assonnato,
#    a destra un personaggio sveglio e sorridente che si ferma davanti a un fiore
GR, GR2, GR_F = "#9fb1c2", "#7f93a8", "#e6ecf1"
def ruota(cx, cy, r, denti, colore, rot=0):
    pts = []
    n = denti * 4
    for i in range(n):
        a = math.radians(rot) + 2 * math.pi * i / n
        rr = r + 9 if (i % 4) in (1, 2) else r
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return (f'<polygon points="{" ".join(pts)}" fill="{colore}" stroke="{GR2}" stroke-width="3" stroke-linejoin="round"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*.38:.1f}" fill="{GR_F}" stroke="{GR2}" stroke-width="3"/>')
b = f'<rect width="{W}" height="{H}" fill="{MENTA}"/>'
b += f'<rect width="300" height="{H}" fill="{GR_F}"/>'
b += ruota(62, 56, 28, 9, GR, 8) + ruota(118, 78, 16, 7, "#b9c7d4", 20) + ruota(248, 54, 24, 8, GR, 0)
b += f'<rect x="14" y="290" width="286" height="16" rx="8" fill="{GR2}" stroke="#6c7f93" stroke-width="3"/>'
for x in range(36, 300, 38):
    b += f'<circle cx="{x}" cy="298" r="4" fill="{GR_F}"/>'
# personaggio "in automatico": grigio, occhi a lineetta
g = in_piedi(150, 290, 0.95, abito=GR, capelli=GR2, pettinatura="corti", pelle="#d3dbe3", gambe=GR2, aperti="assonnato")
b += g
# a destra: alone, prato, fiore, personaggio a colori
b += f'<circle cx="450" cy="150" r="120" fill="{VERDE_T}"/><circle cx="450" cy="150" r="88" fill="{ACQUA_T}"/>'
b += f'<path d="M300 300 Q450 278 600 296 V340 H300Z" fill="{TEAL}" opacity=".85"/>'
b += in_piedi(420, 300, 0.98, abito=ACQUA, capelli=BLU, pettinatura="chignon", gonna=True)
b += f'<path d="M520 298 Q516 262 524 232" stroke="{CONT}" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M520 298 Q516 262 524 232" stroke="{TEAL}" stroke-width="4" fill="none" stroke-linecap="round"/>'
b += f'<path d="M521 266 Q542 256 550 240 Q530 240 521 266Z" fill="{TEAL}" {_c()}/>'
for a in range(0, 360, 60):
    r_ = math.radians(a)
    b += f'<circle cx="{524+15*math.cos(r_):.1f}" cy="{222+15*math.sin(r_):.1f}" r="10" fill="{VERDE}" {_c(3)}/>'
b += f'<circle cx="524" cy="222" r="9" fill="#ffd36b" {_c(3)}/>'
b += f'<path d="M282 280 Q320 266 356 280" stroke="{CONT}" stroke-width="3" fill="none" stroke-dasharray="2 9" stroke-linecap="round"/>'
b += scintille([(360, 70, 12, VERDE), (560, 100, 12, VERDE), (580, 200, 8, TEAL)])
salva("blog-pilota-automatico.svg", svg(W, H, b, "A sinistra ingranaggi grigi e un personaggio grigio in automatico, a destra un personaggio sorridente a colori che si ferma davanti a un fiore"))

# 7. Blog "MBSR: la Mindfulness che ridisegna il cervello": un fiore di loto sorridente sull'acqua
def petalo_c(cx, cy, h, w, angolo, colore):
    d = f"M0 0 C{w} {-h*0.35} {w*0.55} {-h*0.85} 0 {-h} C{-w*0.55} {-h*0.85} {-w} {-h*0.35} 0 0Z"
    return f'<path d="{d}" fill="{colore}" {_c()} transform="translate({cx} {cy}) rotate({angolo})"/>'
CX, CY = 300, 236
b = sfondo_cartoon(300, 150, 132)
b += f'<rect x="0" y="{CY}" width="{W}" height="{H-CY}" fill="{ACQUA_T}"/>'
b += f'<path d="M0 {CY} Q150 {CY-8} 300 {CY} T600 {CY}" stroke="{CONT}" stroke-width="3" fill="none"/>'
for rx, op in ((150, .6), (215, .4)):
    b += f'<ellipse cx="{CX}" cy="{CY+30}" rx="{rx}" ry="{rx*0.1:.0f}" fill="none" stroke="{TEAL}" stroke-width="3" opacity="{op}"/>'
b += f'<ellipse cx="120" cy="{CY+50}" rx="60" ry="14" fill="{TEAL}" {_c()}/>'
b += f'<ellipse cx="480" cy="{CY+58}" rx="50" ry="12" fill="{TEAL}" {_c()}/>'
b += petalo_c(CX, CY+10, 88, 30, -72, BLU2) + petalo_c(CX, CY+10, 88, 30, 72, BLU2)
b += petalo_c(CX, CY+8, 108, 34, -46, TEAL) + petalo_c(CX, CY+8, 108, 34, 46, TEAL)
b += petalo_c(CX, CY+6, 124, 36, -22, ACQUA) + petalo_c(CX, CY+6, 124, 36, 22, ACQUA)
b += petalo_c(CX, CY+4, 136, 40, 0, VERDE)
b += viso(CY - 62, aperti=True, r=1.3, dx=CX)
b += f'<ellipse cx="{CX}" cy="{CY+8}" rx="46" ry="10" fill="{BLU}" {_c()}/>'
for i in range(8):
    b += f'<circle cx="{CX-105+i*30}" cy="{CY+84}" r="6" fill="{VERDE}" {_c(2.5)}/>'
b += scintille([(110, 90, 14, VERDE), (490, 90, 14, VERDE), (150, 190, 8, TEAL), (450, 190, 8, TEAL), (300, 20, 8, TEAL)])
salva("blog-mbsr-loto.svg", svg(W, H, b, "Un fiore di loto sorridente si apre sull'acqua davanti a un grande alone; sotto, otto piccoli cerchi come le otto settimane del percorso"))

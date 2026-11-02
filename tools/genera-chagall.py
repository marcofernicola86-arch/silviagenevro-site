# Illustrazioni "alla Chagall" nella palette del logo: cielo blu notte, figure che fluttuano,
# villaggio storto, luna grande, contorni mossi come pennellate (filtri SVG).
import os, sys, math, random

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

BLU = "#013260"
BLU2 = "#0b4f86"
BLU3 = "#1d6aa8"
ACQUA = "#2befc0"
ACQUA_T = "#bff7e8"
VERDE = "#94ff83"
VERDE_T = "#dcffd4"
TEAL = "#0a7565"
PELLE = "#f2c9a9"
LUNA = "#fbf7e4"

W, H = 600, 340

FILTRI = """
<defs>
  <!-- contorni mossi, come dipinti a mano -->
  <filter id="pennello" x="-5%" y="-5%" width="110%" height="110%">
    <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="5" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <!-- grana della tela -->
  <filter id="tela" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3" result="g"/>
    <feColorMatrix in="g" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .09 0"/>
  </filter>
  <!-- velature del cielo -->
  <filter id="velatura">
    <feTurbulence type="fractalNoise" baseFrequency="0.008 0.02" numOctaves="3" seed="11"/>
    <feColorMatrix type="matrix" values="0 0 0 0 .17  0 0 0 0 .94  0 0 0 0 .75  0 0 0 .28 -.05"/>
  </filter>
  <radialGradient id="alone" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="#ffffff" stop-opacity=".55"/>
    <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
  </radialGradient>
</defs>
"""


def cielo():
    # sfondo più grande del quadro: le pennellate mosse non lasciano bordi vuoti
    b = f'<rect x="-30" y="-30" width="{W+60}" height="{H+60}" fill="{BLU}"/>'
    b += f'<rect x="-30" y="-30" width="{W+60}" height="{H+60}" filter="url(#velatura)"/>'
    # pennellate di blu più chiaro
    b += f'<path d="M-20 120 C120 60 260 150 380 90 S560 40 640 90 L640 150 C520 110 420 190 300 160 S80 170 -20 190Z" fill="{BLU2}" opacity=".55"/>'
    b += f'<path d="M-20 40 C100 10 200 70 330 30 S520 0 640 30 L640 60 C500 40 400 90 280 70 S60 80 -20 80Z" fill="{BLU3}" opacity=".35"/>'
    return b


def stelle(seed, n=18):
    random.seed(seed)
    b = ""
    for _ in range(n):
        x, y = random.uniform(10, W - 10), random.uniform(8, 170)
        r = random.uniform(1.2, 2.6)
        b += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="{LUNA}" opacity="{random.uniform(.5, .95):.2f}"/>'
    return b


def luna(cx, cy, r):
    b = f'<circle cx="{cx}" cy="{cy}" r="{r*1.9:.0f}" fill="url(#alone)"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{LUNA}"/>'
    b += f'<circle cx="{cx + r*0.35:.0f}" cy="{cy - r*0.2:.0f}" r="{r*0.92:.0f}" fill="{ACQUA_T}" opacity=".55"/>'
    return b


def casetta(x, y, w, h, colore, tetto, angolo=0, finestra=LUNA):
    """Casetta storta da villaggio."""
    g = f'<g transform="translate({x} {y}) rotate({angolo})">'
    g += f'<rect x="{-w/2}" y="{-h}" width="{w}" height="{h}" fill="{colore}"/>'
    g += f'<path d="M{-w/2-4} {-h} L0 {-h-w*0.55} L{w/2+4} {-h}Z" fill="{tetto}"/>'
    g += f'<rect x="{-w*0.18}" y="{-h*0.62}" width="{w*0.36}" height="{h*0.32}" fill="{finestra}" opacity=".9"/>'
    g += "</g>"
    return g


def villaggio(seed, y=340):
    random.seed(seed)
    b = f'<path d="M-40 {y-34} C120 {y-60} 220 {y-30} 320 {y-48} S520 {y-62} 640 {y-40} L640 {y+30} L-40 {y+30}Z" fill="{TEAL}"/>'
    xs = [40, 95, 150, 215, 270, 395, 455, 515, 570]
    cols = [(BLU2, ACQUA), (ACQUA, BLU), (VERDE, TEAL), (BLU3, VERDE), (ACQUA_T, BLU2),
            (VERDE, BLU), (BLU2, ACQUA), (ACQUA, TEAL), (VERDE_T, BLU2)]
    for x, (c, t) in zip(xs, cols):
        w = random.uniform(28, 40)
        h = random.uniform(26, 42)
        b += casetta(x, y - 30 - random.uniform(0, 14), w, h, c, t, random.uniform(-9, 9))
    return b


def figura_volante(x, y, s, angolo, vestito, scialle, capelli=BLU, pelle=PELLE, braccio_teso=False):
    """Figura che fluttua in meditazione, inclinata, con uno scialle che ondeggia (tipico di Chagall)."""
    g = f'<g transform="translate({x} {y}) rotate({angolo}) scale({s})">'
    # scialle al vento
    g += f'<path d="M-6 -60 C-40 -70 -70 -50 -96 -64 C-80 -44 -50 -40 -16 -44Z" fill="{scialle}"/>'
    # gambe incrociate
    g += f'<path d="M-42 0 Q-38 -20 -12 -22 L12 -22 Q38 -20 42 0 Q20 7 0 5 Q-20 7 -42 0Z" fill="{vestito}"/>'
    # busto
    g += f'<path d="M-18 -24 L-14 -64 Q0 -72 14 -64 L18 -24 Q0 -18 -18 -24Z" fill="{vestito}"/>'
    # braccia
    if braccio_teso:
        g += f'<path d="M14 -60 Q40 -78 62 -92" stroke="{vestito}" stroke-width="8" fill="none" stroke-linecap="round"/>'
        g += f'<circle cx="64" cy="-94" r="4.5" fill="{pelle}"/>'
    else:
        g += f'<path d="M15 -60 Q32 -42 30 -20" stroke="{vestito}" stroke-width="8" fill="none" stroke-linecap="round"/>'
        g += f'<circle cx="30" cy="-19" r="4.3" fill="{pelle}"/>'
    g += f'<path d="M-15 -60 Q-32 -42 -30 -20" stroke="{vestito}" stroke-width="8" fill="none" stroke-linecap="round"/>'
    g += f'<circle cx="-30" cy="-19" r="4.3" fill="{pelle}"/>'
    # testa con chignon
    g += f'<rect x="-4" y="-74" width="8" height="10" rx="3" fill="{pelle}"/>'
    g += f'<circle cx="0" cy="-84" r="11.5" fill="{pelle}"/>'
    g += f'<path d="M-12 -84 Q-12.5 -98 0 -98 Q12.5 -98 12 -84 Q8 -92 0 -92 Q-8 -92 -12 -84Z" fill="{capelli}"/>'
    g += f'<circle cx="0" cy="-101" r="5.5" fill="{capelli}"/>'
    # guance rosate, occhi chiusi (piccole curve)
    g += f'<path d="M-6 -84 q2.5 2 5 0 M1.5 -84 q2.5 2 5 0" stroke="{BLU}" stroke-width="1.3" fill="none"/>'
    g += "</g>"
    return g


def mazzo_fiori(x, y, s=1.0, angolo=0):
    g = f'<g transform="translate({x} {y}) rotate({angolo}) scale({s})">'
    for dx, dy, c in ((-10, -26, ACQUA), (8, -30, VERDE), (0, -40, LUNA), (-16, -40, VERDE_T), (14, -44, ACQUA)):
        g += f'<circle cx="{dx}" cy="{dy}" r="9" fill="{c}"/><circle cx="{dx}" cy="{dy}" r="3" fill="{BLU}"/>'
    g += f'<path d="M-6 -18 L0 10 L6 -18" stroke="{TEAL}" stroke-width="4" fill="none"/>'
    g += "</g>"
    return g


def uccellino(x, y, s=1.0, colore=ACQUA):
    g = f'<g transform="translate({x} {y}) scale({s})">'
    g += f'<path d="M0 0 C12 -14 30 -10 36 0 C30 8 12 10 0 0Z" fill="{colore}"/>'
    g += f'<path d="M14 -4 C18 -24 34 -26 38 -18 C30 -14 24 -8 20 -2Z" fill="{VERDE}"/>'
    g += f'<circle cx="31" cy="-2" r="1.8" fill="{BLU}"/><path d="M36 0 L44 -1 L36 3Z" fill="{LUNA}"/>'
    g += "</g>"
    return g


def svg(body, titolo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{titolo}">'
            f'<title>{titolo}</title>{FILTRI}<g filter="url(#pennello)">{body}</g>'
            f'<rect width="{W}" height="{H}" filter="url(#tela)"/></svg>\n')


def salva(nome, body, titolo):
    with open(os.path.join(OUT, nome), "w") as f:
        f.write(svg(body, titolo))


# ===== Prova: percorsi di gruppo MBSR =====
b = cielo() + stelle(4) + luna(470, 78, 46)
b += villaggio(2)
b += figura_volante(170, 170, 1.0, -14, BLU2, ACQUA)
b += figura_volante(300, 140, 1.12, 6, ACQUA, VERDE, capelli=BLU)
b += figura_volante(425, 205, 0.95, 18, VERDE, ACQUA_T, capelli="#5a3b2a")
b += mazzo_fiori(78, 118, 1.0, -18)
b += uccellino(530, 160, 1.0)
salva("chagall-gruppo.svg", b, "Tre persone fluttuano in meditazione nel cielo blu notte sopra un piccolo villaggio, con la luna, fiori e un uccellino")
print("ok")

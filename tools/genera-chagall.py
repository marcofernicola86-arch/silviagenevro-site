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


def figura_volante(x, y, s, angolo, vestito, scialle, capelli=BLU, pelle=PELLE, braccio_teso=False, genere="f", barba=False):
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
    g += testa_capelli(genere, capelli, barba)
    # guance rosate, occhi chiusi (piccole curve)
    g += f'<path d="M-6 -84 q2.5 2 5 0 M1.5 -84 q2.5 2 5 0" stroke="{BLU}" stroke-width="1.3" fill="none"/>'
    g += "</g>"
    return g


def testa_capelli(genere, capelli, barba=False):
    """Capelli: chignon per le donne, taglio corto (ed eventuale barba) per gli uomini."""
    if genere == "f":
        return (f'<path d="M-12 -84 Q-12.5 -98 0 -98 Q12.5 -98 12 -84 Q8 -92 0 -92 Q-8 -92 -12 -84Z" fill="{capelli}"/>'
                f'<circle cx="0" cy="-101" r="5.5" fill="{capelli}"/>')
    g = f'<path d="M-12.5 -82 Q-14 -99 0 -99 Q14 -99 12.5 -82 Q10 -91 0 -92 Q-10 -91 -12.5 -82Z" fill="{capelli}"/>'
    if barba:
        g += f'<path d="M-11 -82 Q-10 -70 0 -69 Q10 -70 11 -82 Q6 -76 0 -77 Q-6 -76 -11 -82Z" fill="{capelli}"/>'
    return g


def figura_in_volo(x, y, s, angolo, vestito, capelli=BLU, pelle=PELLE, genere="f", barba=False, gambe=None):
    """Figura distesa che vola (come gli innamorati di Chagall), braccia aperte."""
    gambe = gambe or BLU
    g = f'<g transform="translate({x} {y}) rotate({angolo}) scale({s})">'
    g += f'<path d="M-8 -6 L-30 22 L-22 26 L-2 4Z M8 -6 L22 26 L30 22 L10 -4Z" fill="{gambe}"/>'
    g += f'<path d="M-15 -8 L-13 -52 Q0 -60 13 -52 L15 -8 Q0 -2 -15 -8Z" fill="{vestito}"/>'
    if genere == "f":
        g += f'<path d="M-15 -14 Q0 -4 15 -14 L22 6 Q0 14 -22 6Z" fill="{vestito}"/>'
    g += f'<path d="M-12 -48 Q-34 -58 -50 -52" stroke="{vestito}" stroke-width="7" fill="none" stroke-linecap="round"/>'
    g += f'<path d="M12 -48 Q34 -58 50 -52" stroke="{vestito}" stroke-width="7" fill="none" stroke-linecap="round"/>'
    g += f'<circle cx="-52" cy="-52" r="4.2" fill="{pelle}"/><circle cx="52" cy="-52" r="4.2" fill="{pelle}"/>'
    g += f'<g transform="translate(0 22)"><rect x="-4" y="-84" width="8" height="10" rx="3" fill="{pelle}"/>'
    g += f'<circle cx="0" cy="-94" r="11" fill="{pelle}"/>'
    g += f'<g transform="translate(0 -10)">{testa_capelli(genere, capelli, barba)}</g>'
    g += f'<path d="M-6 -94 q2.5 2 5 0 M1.5 -94 q2.5 2 5 0" stroke="{BLU}" stroke-width="1.3" fill="none"/></g>'
    g += "</g>"
    return g


def prato_fiorito(seed, y=340):
    """Collina con fiori stilizzati al posto del villaggio."""
    random.seed(seed)
    b = f'<path d="M-40 {y-40} C120 {y-66} 220 {y-34} 320 {y-54} S520 {y-70} 640 {y-46} L640 {y+30} L-40 {y+30}Z" fill="{TEAL}"/>'
    teste = [ACQUA, VERDE, LUNA, ACQUA_T, VERDE_T, BLU3]
    for i in range(26):
        x = -10 + i * 24 + random.uniform(-8, 8)
        base = y - 26 + random.uniform(-10, 14)
        h = random.uniform(26, 58)
        c = random.choice(teste)
        lean = random.uniform(-10, 10)
        b += f'<path d="M{x:.0f} {base:.0f} Q{x+lean/2:.0f} {base-h/2:.0f} {x+lean:.0f} {base-h:.0f}" stroke="{VERDE}" stroke-width="2.6" fill="none"/>'
        tx, ty = x + lean, base - h
        tipo = i % 3
        if tipo == 0:   # margherita
            for k in range(6):
                a_ = k * math.pi / 3
                b += f'<ellipse cx="{tx + 7*math.cos(a_):.1f}" cy="{ty + 7*math.sin(a_):.1f}" rx="5" ry="3" fill="{c}" transform="rotate({math.degrees(a_):.0f} {tx + 7*math.cos(a_):.1f} {ty + 7*math.sin(a_):.1f})"/>'
            b += f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="3.6" fill="{BLU}"/>'
        elif tipo == 1:  # tulipano
            b += f'<path d="M{tx-8:.1f} {ty:.1f} Q{tx-9:.1f} {ty-14:.1f} {tx-4:.1f} {ty-16:.1f} L{tx:.1f} {ty-9:.1f} L{tx+4:.1f} {ty-16:.1f} Q{tx+9:.1f} {ty-14:.1f} {tx+8:.1f} {ty:.1f} Q{tx:.1f} {ty+6:.1f} {tx-8:.1f} {ty:.1f}Z" fill="{c}"/>'
        else:            # fiore tondo
            b += f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="8" fill="{c}"/><circle cx="{tx:.1f}" cy="{ty:.1f}" r="3" fill="{TEAL}"/>'
        if i % 4 == 0:
            b += f'<path d="M{x:.0f} {base-h*0.4:.0f} q-12 -6 -16 -16 q12 2 16 16Z" fill="{VERDE}"/>'
    return b


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


# ===== 1. Percorsi di gruppo MBSR =====
b = cielo() + stelle(4) + luna(470, 78, 46)
b += prato_fiorito(2)
b += figura_volante(165, 172, 1.0, -14, BLU2, ACQUA, genere="f")
b += figura_volante(300, 140, 1.12, 6, ACQUA, VERDE, capelli="#3a2a20", genere="m", barba=True)
b += figura_volante(428, 205, 0.95, 18, VERDE, ACQUA_T, capelli="#5a3b2a", genere="f")
b += mazzo_fiori(70, 118, 1.0, -18)
b += uccellino(530, 160, 1.0)
salva("chagall-gruppo.svg", b, "Una donna, un uomo e una donna fluttuano in meditazione nel cielo blu notte sopra un prato fiorito, con la luna e un uccellino")

# ===== 2. ADHD: il filo aggrovigliato che diventa una scia di stelle =====
b = cielo() + stelle(9, 12) + luna(95, 70, 34)
b += prato_fiorito(5)
b += (f'<path d="M120 210 C150 150 190 250 220 180 S260 120 240 200 S200 230 250 160 '
      f'C300 100 320 170 360 140" stroke="{LUNA}" stroke-width="3.5" fill="none" stroke-linecap="round" opacity=".9"/>')
for k, (sx, sy) in enumerate([(390, 128), (420, 114), (452, 104), (486, 98), (520, 96), (556, 98)]):
    r = 3 + k * 0.6
    b += f'<path d="M{sx} {sy-r*2} L{sx+r*0.6:.1f} {sy-r*0.6:.1f} L{sx+r*2} {sy} L{sx+r*0.6:.1f} {sy+r*0.6:.1f} L{sx} {sy+r*2} L{sx-r*0.6:.1f} {sy+r*0.6:.1f} L{sx-r*2} {sy} L{sx-r*0.6:.1f} {sy-r*0.6:.1f}Z" fill="{VERDE if k%2 else ACQUA}"/>'
b += figura_volante(200, 262, 0.95, -8, TEAL, VERDE, genere="m")
b += figura_volante(380, 236, 0.98, 12, ACQUA, ACQUA_T, capelli="#5a3b2a", genere="f")
salva("chagall-adhd.svg", b, "Un uomo e una donna fluttuano in meditazione mentre un filo aggrovigliato si scioglie in una scia di stelle")

# ===== 3. Aziende: colleghi che si tengono per mano in volo =====
b = cielo() + stelle(12, 14) + luna(520, 66, 36)
b += prato_fiorito(8)
b += f'<path d="M226 118 C226 84 296 76 322 102 C356 92 382 128 364 150 C372 180 320 188 302 168 C276 188 230 174 236 152 L216 168 L226 142Z" fill="{ACQUA}" opacity=".9"/>'
b += f'<path d="M286 120 C286 108 300 108 302 118 C304 108 318 108 318 120 C318 134 302 142 302 142 C302 142 286 134 286 120Z" fill="none" stroke="{BLU}" stroke-width="3"/>'
b += figura_in_volo(110, 222, 1.0, -10, BLU2, genere="f")
b += figura_in_volo(212, 236, 1.0, 4, VERDE, capelli="#3a2a20", genere="m", barba=True)
b += figura_in_volo(316, 228, 1.0, -6, ACQUA, capelli="#5a3b2a", genere="f")
b += figura_in_volo(420, 214, 1.0, 10, TEAL, genere="m")
salva("chagall-aziende.svg", b, "Due donne e due uomini volano tenendosi per mano sotto una nuvoletta di dialogo con un cuore")

# ===== 4. Sessioni individuali: Silvia e una persona, una di fronte all'altra, davanti alla luna =====
b = cielo() + stelle(15, 16) + luna(300, 118, 70)
b += prato_fiorito(11)
b += figura_volante(220, 236, 1.08, -8, BLU2, ACQUA, genere="f")
b += figura_volante(384, 240, 1.04, 8, VERDE, ACQUA_T, capelli="#3a2a20", genere="m")
b += uccellino(282, 210, 0.9, ACQUA)
salva("chagall-individuale.svg", b, "Una donna e un uomo meditano uno di fronte all'altra, sospesi davanti a una grande luna")

# ===== 5. Pilota automatico: figure grigie tra gli ingranaggi, due figure a colori si staccano e volano =====
GR, GR2, GRP = "#8ea2b6", "#6f8399", "#c9d3dc"
def ingranaggio(cx, cy, r, denti, colore, rot=0):
    pts = []
    for i_ in range(denti * 4):
        a_ = math.radians(rot) + 2 * math.pi * i_ / (denti * 4)
        rr = r + 8 if (i_ % 4) in (1, 2) else r
        pts.append(f"{cx + rr*math.cos(a_):.1f},{cy + rr*math.sin(a_):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{colore}"/><circle cx="{cx}" cy="{cy}" r="{r*.38:.1f}" fill="{BLU}"/>'
b = cielo() + stelle(21, 14) + luna(512, 70, 38)
b += prato_fiorito(14)
b += ingranaggio(70, 262, 30, 9, GR2, 10) + ingranaggio(128, 236, 20, 7, GR, 0) + ingranaggio(56, 196, 16, 6, GR, 20)
b += f'<rect x="20" y="300" width="230" height="12" rx="6" fill="{GR2}"/>'
b += figura_volante(168, 296, 0.8, 0, GR, GR2, capelli=GR2, pelle=GRP, genere="m")
b += figura_volante(250, 296, 0.8, 0, GR2, GR, capelli=GR2, pelle=GRP, genere="f")
b += f'<path d="M282 246 Q320 190 356 170" stroke="{LUNA}" stroke-width="3" fill="none" stroke-dasharray="2 9" stroke-linecap="round"/>'
b += figura_in_volo(400, 150, 1.0, -18, ACQUA, genere="f")
b += figura_in_volo(486, 176, 1.0, -8, VERDE, capelli="#3a2a20", genere="m", barba=True)
b += mazzo_fiori(560, 230, 0.9, 12)
salva("chagall-pilota-automatico.svg", b, "A terra figure grigie tra ingranaggi su un nastro; una donna e un uomo a colori si staccano e volano verso la luna")

# ===== 6. Loto MBSR: un grande loto che galleggia nel cielo, con una donna e un uomo in meditazione =====
def petalo(cx, cy, h, w, angolo, colore):
    d = f"M0 0 C{w} {-h*0.35} {w*0.55} {-h*0.85} 0 {-h} C{-w*0.55} {-h*0.85} {-w} {-h*0.35} 0 0Z"
    return f'<path d="{d}" fill="{colore}" transform="translate({cx} {cy}) rotate({angolo})"/>'
b = cielo() + stelle(30, 18) + luna(110, 72, 40)
b += prato_fiorito(17)
LX, LY = 330, 206
for (h, w, a_, c) in ((96, 32, -74, BLU3), (96, 32, 74, BLU3), (116, 36, -48, TEAL), (116, 36, 48, TEAL),
                      (132, 38, -23, ACQUA), (132, 38, 23, ACQUA), (142, 40, 0, VERDE)):
    b += petalo(LX, LY, h, w, a_, c)
b += f'<ellipse cx="{LX}" cy="{LY+4}" rx="62" ry="12" fill="{BLU2}"/>'
for k in range(8):
    b += f'<circle cx="{LX-105+k*30}" cy="{LY+34}" r="5" fill="{LUNA}" opacity="{0.35 + k*0.08:.2f}"/>'
b += figura_volante(176, 190, 0.82, -12, BLU2, ACQUA, genere="f")
b += figura_volante(486, 186, 0.82, 12, ACQUA, VERDE, capelli="#3a2a20", genere="m")
salva("chagall-loto.svg", b, "Un grande fiore di loto galleggia nel cielo notturno tra una donna e un uomo in meditazione; sotto, otto piccole lune per le otto settimane")
print("ok")

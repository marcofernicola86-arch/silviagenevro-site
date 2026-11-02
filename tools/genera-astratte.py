# Illustrazioni astratte ricavate dal logo: macchie morbide acqua e verde e un filo blu
# continuo che disegna un cuore. Niente figure: forme semplici, coerenti con l'identità di Silvia.
import os, sys, math, random

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

BLU = "#013260"
ACQUA = "#2befc0"
ACQUA_T = "#bff7e8"
VERDE = "#94ff83"
VERDE_T = "#dcffd4"
TEAL = "#0a7565"
FONDO = "#f4fbf8"
W, H = 600, 340


def macchia(cx, cy, r, seed, punti=9, irregolarita=0.13):
    """Forma organica chiusa, come le macchie del logo (spline di Catmull-Rom → Bézier)."""
    random.seed(seed)
    pts = []
    for i in range(punti):
        a = 2 * math.pi * i / punti + random.uniform(-0.12, 0.12)
        rr = r * (1 + random.uniform(-irregolarita, irregolarita))
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    n = len(pts)
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d + "Z"


def cuore(cx, cy, s):
    """Cuore a filo come nel logo: parte e torna al punto (cx, cy), la punta in basso del cuore."""
    return (f"C{cx - 22*s:.1f} {cy - 12*s:.1f} {cx - 46*s:.1f} {cy - 28*s:.1f} {cx - 36*s:.1f} {cy - 48*s:.1f} "
            f"C{cx - 26*s:.1f} {cy - 66*s:.1f} {cx - 4*s:.1f} {cy - 62*s:.1f} {cx:.1f} {cy - 44*s:.1f} "
            f"C{cx + 4*s:.1f} {cy - 62*s:.1f} {cx + 26*s:.1f} {cy - 66*s:.1f} {cx + 36*s:.1f} {cy - 48*s:.1f} "
            f"C{cx + 46*s:.1f} {cy - 28*s:.1f} {cx + 22*s:.1f} {cy - 12*s:.1f} {cx:.1f} {cy:.1f} ")


def puntini(seed, n=10, colore=BLU):
    random.seed(seed)
    b = ""
    for _ in range(n):
        b += f'<circle cx="{random.uniform(20, W-20):.0f}" cy="{random.uniform(20, H-20):.0f}" r="{random.uniform(2, 4):.1f}" fill="{colore}" opacity="{random.uniform(.15, .4):.2f}"/>'
    return b


def svg(body, titolo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{titolo}">'
            f'<title>{titolo}</title><rect width="{W}" height="{H}" fill="{FONDO}"/>{body}</svg>\n')


def salva(nome, body, titolo):
    with open(os.path.join(OUT, nome), "w") as f:
        f.write(svg(body, titolo))


FILO = f'fill="none" stroke="{BLU}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"'

# ===== Percorsi di gruppo: tre macchie che si sovrappongono (il gruppo), un filo che le unisce in un cuore =====
b = puntini(1)
b += f'<path d="{macchia(225, 185, 92, 3)}" fill="{ACQUA}" opacity=".85"/>'
b += f'<path d="{macchia(375, 175, 86, 5)}" fill="{VERDE}" opacity=".85"/>'
b += f'<path d="{macchia(300, 112, 74, 8)}" fill="{ACQUA_T}" opacity=".95"/>'
b += (f'<path d="M40 290 C110 300 120 230 170 236 C230 244 190 300 250 292 C280 288 292 266 300 250 '
      + cuore(300, 250, 1.5) +
      f'C308 266 330 300 380 296 C430 292 420 236 470 240 C520 244 520 300 570 288" {FILO}/>')
salva("astratta-gruppo.svg", b, "Tre forme morbide che si sovrappongono, unite da un filo che disegna un cuore")

# ===== Sessioni individuali: due macchie vicine (te e l'insegnante), il filo fa un solo anello a cuore =====
b = puntini(2, 8)
b += f'<path d="{macchia(250, 170, 108, 11)}" fill="{ACQUA}" opacity=".85"/>'
b += f'<path d="{macchia(372, 196, 66, 13)}" fill="{VERDE}" opacity=".9"/>'
b += (f'<path d="M60 250 C130 250 150 200 210 210 C250 216 280 252 300 250 '
      + cuore(300, 250, 1.75) +
      f'C330 268 380 280 430 262 C480 244 500 210 548 214" {FILO}/>')
salva("astratta-individuale.svg", b, "Due forme morbide vicine, unite da un filo che disegna un cuore")
print("ok")

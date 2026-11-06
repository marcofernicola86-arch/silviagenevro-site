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


def svg(w, h, body, titolo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{titolo}">'
            f'<title>{titolo}</title>{body}</svg>\n')


def salva(nome, contenuto):
    with open(os.path.join(OUT, nome), "w") as f:
        f.write(contenuto)


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

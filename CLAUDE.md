# Sito di Silvia Genevro – istruzioni di lavoro

Sito di Silvia Genevro, istruttrice di Mindfulness (silviagenevro.it).
Eleventy 2 (`src/` → `_site/`), pubblicato da Netlify a ogni push su `main`.
Chi chiede le modifiche: Marco Fernicola (compagno di Silvia). Rispondere in italiano, tono diretto.

## Regole generali
- Lavorare sul ramo di sviluppo, mostrare un'anteprima (screenshot telefono + computer) e **pubblicare su `main` solo dopo un "pubblica" esplicito**.
- Dopo la pubblicazione: verificare sul sito reale (curl) e segnalare le pagine nuove/cambiate a Bing con IndexNow
  (chiave `5f689786bb57f79a900bd2fb34cd96ed`, file nella radice del sito).
- Stile grafico: colori e caratteri sono variabili in `assets/css/style.css` (`:root`). Titoli di sezione Montserrat maiuscolo spaziato, titoli lunghi Lora, testo Lato.
- Illustrazioni: stile "alla Chagall" (cielo blu notte, figure che fluttuano, prato fiorito, uomini e donne insieme) generate da
  `tools/genera-chagall.py` (SVG) e poi convertite in WebP 1200×680 in `assets/img/illustrazioni/chagall-*.webp`.
  Le icone dei benefici e le vecchie illustrazioni piatte restano SVG da `tools/genera-illustrazioni.py`.
- Nessun prezzo sul sito, tranne quelli degli eventi.
- Zone: "Asti, Alessandria, Torino, Pinerolo, Torre Pellice e nel Nord Italia".

## Pubblicare un articolo del blog
Silvia manda un testo (Word o incollato) e di solito un paio di immagini. Procedura:

1. **File**: `src/blog/articoli/AAAA-MM-GG-slug-breve.md` (data di pubblicazione; slug in minuscolo, senza accenti, 3–6 parole chiave).
   L'indirizzo finale sarà `/blog/slug-breve/` (la data nel nome del file viene tolta in automatico).
2. **Intestazione** (front matter):
   ```
   ---
   title: "Titolo dell'articolo"
   description: "Riassunto di 140–160 caratteri con le parole che la gente cerca (es. mindfulness, MBSR, ADHD, stress, città)."
   date: AAAA-MM-GG
   immagine: /assets/img/blog/slug-breve.jpg      # facoltativa: immagine di copertina
   copertina: /assets/img/illustrazioni/chagall-gruppo.webp  # se manca una foto: illustrazione del sito come copertina
   immagine_alt: "Descrizione dell'immagine"       # facoltativa
   cta_testo: "Scopri il percorso MBSR"            # facoltativo: pulsante in fondo (default: Scopri i corsi)
   cta_link: "/mbsr/"                              # facoltativo
   aggiornato: AAAA-MM-GG                          # solo se si modifica un articolo già pubblicato
   ---
   ```
3. **Testo**: Markdown pulito. Non cambiare le parole di Silvia: solo pulizia della formattazione di Word
   (niente caratteri/colori/spaziature incollate), titoletti come `## Titoletto`, elenchi come `- voce`,
   citazioni come `> citazione`. Correggere solo refusi evidenti e segnalarli.
4. **Immagini**: in `assets/img/blog/`, nome = slug (+ `-2`, `-3`…), larghezza massima 1600 px, JPG ~80% o WebP,
   sotto i 300 KB. Nel testo: `![descrizione utile](/assets/img/blog/nome.jpg)`. Sempre il testo alternativo.
5. **SEO**: un collegamento interno pertinente nel testo solo se Silvia è d'accordo, altrimenti usare `cta_link`
   (es. ADHD → pulsante verso la pagina o i corsi; MBSR → `/mbsr/`).
6. **Niente da toccare a mano**: elenco del blog, sitemap e dati per Google (BlogPosting) si aggiornano da soli.
7. **Controlli**: `npx eleventy`, anteprima di `/blog/` e dell'articolo su telefono (390 px) e computer (1366 px),
   nessuno scorrimento orizzontale, nessun errore in console. Mandare gli screenshot e aspettare "pubblica".
8. **Dopo la pubblicazione**: verificare l'URL dal vivo e segnalare a Bing (IndexNow) l'articolo e `/blog/`.
   Ricordare a Marco: Search Console → Controllo URL → Richiedi indicizzazione per il nuovo articolo.

## Pagine fisse e sitemap
La sitemap (`src/sitemap.liquid`) prende le pagine fisse da `src/_data/pagine_sitemap.json`:
quando si modifica una pagina fissa, aggiornare lì la sua `lastmod`.

## Vecchio blog
Il vecchio blog era su Blogger (blog.silviagenevro.it). I due articoli sono stati trasferiti in `src/blog/articoli/`;
i redirect dai vecchi indirizzi sono in `netlify.toml` (blog.silviagenevro.it punta a Netlify dal 1° novembre 2026).

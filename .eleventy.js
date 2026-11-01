module.exports = function (eleventyConfig) {

  // copia 1:1 cartelle statiche nella build
  eleventyConfig.addPassthroughCopy("assets");

  // sitemap e robots vanno pubblicati così come sono, nella radice del sito
  eleventyConfig.addPassthroughCopy({ "src/robots.txt": "robots.txt" });
  // chiave IndexNow (segnalazione pagine a Bing e altri motori)
  eleventyConfig.addPassthroughCopy({ "src/5f689786bb57f79a900bd2fb34cd96ed.txt": "5f689786bb57f79a900bd2fb34cd96ed.txt" });

  // ===== BLOG =====
  // data in formato AAAA-MM-GG (sitemap, dati per Google)
  eleventyConfig.addFilter("dataIso", (d) => new Date(d).toISOString().slice(0, 10));
  // data leggibile in italiano: "7 settembre 2026"
  eleventyConfig.addFilter("dataIt", (d) =>
    new Date(d).toLocaleDateString("it-IT", { day: "numeric", month: "long", year: "numeric", timeZone: "UTC" })
  );
  // minuti di lettura stimati (circa 200 parole al minuto)
  eleventyConfig.addFilter("minutiLettura", (html) => {
    const parole = String(html || "").replace(/<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length;
    return Math.max(1, Math.round(parole / 200));
  });

  return {
    dir: {
      input: "src",
      output: "_site",
      // includes e data li lasciamo di default (src/_includes e src/_data)
    },
  };
};

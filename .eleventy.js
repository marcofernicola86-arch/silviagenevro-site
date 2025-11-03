module.exports = function(eleventyConfig) {
  // Copia pass-through degli asset statici
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("admin");

  return {
    // Leggi TUTTO dalla root (.) così prende sia /index.html sia /src/blog/**
    dir: {
      input: ".",           // <-- chiave
      includes: "layouts",  // i tuoi layout sono in /layouts
      output: "_site"
    },
    templateFormats: ["njk", "html", "md"] // processa .njk e .html
  };
};

module.exports = function (eleventyConfig) {
  // Copia pass-through degli asset statici
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("admin");

  return {
    dir: {
      input: ".",          // <-- prende sia /index.html sia /src/blog/**
      includes: "layouts", // <-- i tuoi layout stanno in /layouts (a fianco di /src)
      output: "_site"
    },
    templateFormats: ["njk", "html", "md"]
  };
};

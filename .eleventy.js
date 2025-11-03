module.exports = function(eleventyConfig) {
  // Copia 1: asset e admin
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("admin");

  // Copia 2: le tue pagine “standalone” (restano com’erano)
  eleventyConfig.addPassthroughCopy("index.html");
  eleventyConfig.addPassthroughCopy("meditazione.html");
  eleventyConfig.addPassthroughCopy("mbsr.html");
  eleventyConfig.addPassthroughCopy("introduttivo.html");
  eleventyConfig.addPassthroughCopy("sessioni.html");
  eleventyConfig.addPassthroughCopy("privacy.html");
  eleventyConfig.addPassthroughCopy("regolamento.html");
  eleventyConfig.addPassthroughCopy("sitemap.xml");

  // Collezione dei post (ordina dal più recente)
  eleventyConfig.addCollection("posts", (collection) =>
    collection.getFilteredByGlob("src/blog/posts/*.md").sort((a,b) => b.date - a.date)
  );

  return {
    dir: { input: "src", output: "_site", includes: "layouts" },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    templateFormats: ["md","njk","html"]
  };
};

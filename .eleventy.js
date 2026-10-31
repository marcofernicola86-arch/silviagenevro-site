module.exports = function (eleventyConfig) {
  // alias layout
eleventyConfig.addLayoutAlias("base.njk", "layouts/base.njk");
eleventyConfig.addLayoutAlias("post.njk", "layouts/post.njk");

  // copia 1:1 cartelle statiche nella build
  // (nel tuo repo sono a livello root: /assets e /admin)
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("admin");

  // sitemap e robots vanno pubblicati così come sono, nella radice del sito
  eleventyConfig.addPassthroughCopy({ "src/sitemap.xml": "sitemap.xml" });
  eleventyConfig.addPassthroughCopy({ "src/robots.txt": "robots.txt" });
  // chiave IndexNow (segnalazione pagine a Bing e altri motori)
  eleventyConfig.addPassthroughCopy({ "src/5f689786bb57f79a900bd2fb34cd96ed.txt": "5f689786bb57f79a900bd2fb34cd96ed.txt" });

  return {
    dir: {
      input: "src",
      output: "_site",
      // includes e data li lasciamo di default (src/_includes e src/_data)
    },
  };
};

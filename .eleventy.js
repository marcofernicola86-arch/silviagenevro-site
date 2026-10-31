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

  return {
    dir: {
      input: "src",
      output: "_site",
      // includes e data li lasciamo di default (src/_includes e src/_data)
    },
  };
};

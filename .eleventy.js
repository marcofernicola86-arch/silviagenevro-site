module.exports = function (eleventyConfig) {
  // alias layout
  eleventyConfig.addLayoutAlias("base", "layouts/base.njk");
  eleventyConfig.addLayoutAlias("post", "layouts/post.njk");

  // copia 1:1 cartelle statiche nella build
  // (nel tuo repo sono a livello root: /assets e /admin)
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("admin");

  return {
    dir: {
      input: "src",
      output: "_site",
      // includes e data li lasciamo di default (src/_includes e src/_data)
    },
  };
};

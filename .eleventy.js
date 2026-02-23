module.exports = function(eleventyConfig) {
  // alias layout come li hai già
  eleventyConfig.addLayoutAlias('base', 'layouts/base.njk');
  eleventyConfig.addLayoutAlias('post', 'layouts/post.njk');

  // copia 1:1 asset e admin nella build
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy("src/admin");

  // filtro date (se lo hai messo)…

return {
  dir: {
    input: "src",
    // lasciare includes NON specificato: Eleventy userà "src/_includes" automaticamente
    data: "_data",
    output: "_site"
  }
};

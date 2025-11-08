module.exports = function (eleventyConfig) {
  // Alias doppi: funzionano sia "base" che "base.njk"
  eleventyConfig.addLayoutAlias('base', 'layouts/base.njk');
  eleventyConfig.addLayoutAlias('base.njk', 'layouts/base.njk');
  eleventyConfig.addLayoutAlias('post', 'layouts/post.njk');
  eleventyConfig.addLayoutAlias('post.njk', 'layouts/post.njk');

  return {
    dir: {
      input: "src",        // <— IMPORTANTE! Così _includes è sotto src
      includes: "_includes",
      data: "_data",
      output: "_site"
    }
  };
};

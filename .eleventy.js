module.exports = function (eleventyConfig) {
  // Alias: permettono di usare "layout: base" o "layout: base.njk" ecc.
  eleventyConfig.addLayoutAlias('base', 'layouts/base.njk');
  eleventyConfig.addLayoutAlias('post', 'layouts/post.njk');

  return {
    dir: {
      input: "src",
      includes: "_includes",
      data: "_data",
      // niente dir.layouts: i layout stanno sotto _includes/layouts (default v2)
      output: "_site"
    }
  };
};

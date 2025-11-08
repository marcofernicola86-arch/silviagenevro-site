module.exports = function(eleventyConfig) {
  // Alias: così puoi continuare a scrivere "layout: base" o "layout: post"
  eleventyConfig.addLayoutAlias('base', 'layouts/base.njk');
  eleventyConfig.addLayoutAlias('post', 'layouts/post.njk');

  return {
    dir: {
      input: "src",
      includes: "_includes",
      data: "_data",
      // niente dir.layouts: i layout stanno sotto _includes/layouts per default
      output: "_site"
    }
  };
};

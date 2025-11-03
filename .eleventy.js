module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("admin");
  return {
    dir: { input: ".", includes: "layouts", output: "_site" },
    templateFormats: ["njk", "html", "md"]
  };
};

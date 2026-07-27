const fs = require('fs');
const md = require('markdown-it')();

module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("src/assets");

  eleventyConfig.addFilter("renderMarkdown", function(slug) {
    const filePath = `./src/assets/cases/${slug}/content.md`;
    if (fs.existsSync(filePath)) {
      const content = fs.readFileSync(filePath, 'utf8');
      return md.render(content);
    }
    return "";
  });

  eleventyConfig.addFilter("parseDate", function(dateString) {
    let parts = dateString.split(/,| - | – /);
    if (parts.length >= 2) {
      return { start: parts[0].trim(), end: parts[1].trim() };
    }
    return { start: dateString.trim(), end: "Present" };
  });

  return {
    dir: {
      input: "src",
      output: "_site"
    }
  };
};

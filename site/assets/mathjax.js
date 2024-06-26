window.MathJax = {
  tex: {
    inlineMath: [['\\(','\\)'], ['$', '$']],  // Cambia esto según tus necesidades
    displayMath: [['\\[','\\]'], ['$$', '$$']],
    tags: 'ams',

  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

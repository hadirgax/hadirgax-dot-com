// import jss from "jss";
// import preset from "jss-preset-default";

// const jss = "jss";
// const preset = "jss-preset-default";

jss.setup(preset());

const styles = {
  wrapper: {
    padding: 40,
    background: "#f7df1e",
    textAlign: "center"
  },
  title: {
    font: {
      size: 40,
      weight: 900
    },
    color: "#24292e"
  },
  link: {
    color: "#24292e",
    "&:hover": {
      opacity: 0.5
    }
  }
};

const { classes } = jss.createStyleSheet(styles).attach();

document.body.innerHTML = `
  <div class="${classes.wrapper}">
    <h1 class="${classes.title}">Hello JSS!</h1>
    <a
      class=${classes.link}
      href="http://cssinjs.org/"
      traget="_blank"
    >
      See docs
    </a>
  </div>
`;
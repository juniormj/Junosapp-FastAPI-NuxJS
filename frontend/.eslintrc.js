module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  parserOptions: {
    parser: "@babel/eslint-parser",
    requireConfigFile: false,
  },
  extends: ["@nuxtjs", "plugin:nuxt/recommended"],
  plugins: [],
  // add your custom rules here
  rules: {
    quotes: ["off"],
    "comma-dangle": ["off"],
    semi: ["off"],
    "space-before-function-paren": ["off"],
    "vue/singleline-html-element-content-newline": ["off"],
    "vue/html-self-closing": ["off"],
    "vue/no-v-html": ["off"],
    "vue/no-lone-template": ["off"],
    "vue/no-mutating-props": ["off"],
    "no-console": "off",
    "object-shorthand": ["off"],
  },
};

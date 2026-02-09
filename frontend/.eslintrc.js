module.exports = {
  extends: ["next", "next/core-web-vitals"],
  parser: "@typescript-eslint/parser",
  plugins: ["@typescript-eslint"],
  rules: {
    // Add custom rules here
    "no-console": "warn",
    "no-unused-vars": "off", // Let TypeScript handle this
    "@typescript-eslint/no-unused-vars": ["error"],
    "prefer-const": "error",
    "no-var": "error",
    "semi": ["error", "always"],
    "comma-dangle": ["error", "always-multiline"],
    "object-curly-spacing": ["error", "always"],
    "array-bracket-spacing": ["error", "never"],
    "arrow-spacing": ["error", { "before": true, "after": true }],
    "keyword-spacing": ["error", { "before": true, "after": true }],
    "space-before-blocks": ["error", "always"],
    "space-before-function-paren": ["error", { "anonymous": "never", "named": "never", "asyncArrow": "always" }]
  },
  overrides: [
    {
      files: ["*.ts", "*.tsx"],
      rules: {
        "@typescript-eslint/explicit-module-boundary-types": "off",
        "@typescript-eslint/no-explicit-any": "warn",
        "@typescript-eslint/no-non-null-assertion": "off"
      }
    }
  ]
};
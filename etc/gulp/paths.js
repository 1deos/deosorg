export const paths = {
  "dirs": {
    "dist": "app",
    "lib": "var/build/es5",
    "es5": {
      "client": "var/build/es5/client",
      "server": "var/build/es5/server",
      "shared": "var/build/es5/shared",
      "test": "build/es5/test"
    }
  },
  "files": {
    "client": {
      "all": "src/client/**/*.js?(x)",
      "bundle": "app/bundle.js?(.map)",
      "entry": "src/client/app.jsx"
    },
    "config": {
      "gulp": "Gulpfile.babel.js",
      "webpack": "etc/gulp/webpack.config.babel.js"
    },
    "server": {
      "all": "src/server/**/*.js?(x)"
    },
    "shared": {
      "all": "src/shared/**/*.js?(x)"
    },
    "tests": {
      "all": "var/build/es5/test/**/*.js"
    }
  }
};

export const allConfigJS = [
  paths.files.config.gulp,
  paths.files.config.webpack
];

export const allSrcJS = 'src/**/*.js?(x)';

export const allJS = [allSrcJS].concat(allConfigJS);

export const buildDeps = ['lint', 'clean'];

export const toClean = [
  paths.files.client.bundle,
  paths.dirs.es5.client,
  paths.dirs.es5.server,
  paths.dirs.es5.shared,
  paths.dirs.es5.test
];

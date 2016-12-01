export const paths = {
  dirs: {
    dist: 'app',
    es5: {
      client: 'var/build/es5/client',
      shared: 'var/build/es5/shared',
      render: 'var/build/es5/render',
      server: 'var/build/es5/server',
      test: 'var/build/es5/test',
    },
    lib: 'var/build/es5',
  },
  files: {
    client: {
      js: {
        all: 'src/client/**/*.js?(x)',
        entry: 'src/client/index.jsx',
        out: 'app/bundle.min.js?(.map)',
      },
      pug: {
        in: 'src/client/index.pug',
        out: 'index.min.html',
      },
    },
    shared: {
      js: {
        all: 'src/shared/**/*.js?(x)',
      },
    },
    config: {
      gulp: 'Gulpfile.babel.js',
      paths: 'src/dejs/config.paths.js',
      webpack: 'src/dejs/webpack.config.babel.js',
    },
    render: {
      js: {
        all: 'src/render/**/*.js?(x)',
      },
    },
    server: {
      js: {
        all: 'src/server/**/*.js?(x)',
      },
    },
    test: {
      js: {
        all: 'src/test/**/*.js?(x)',
        out: 'var/build/es5/test/**/*.js',
      },
    },
  },
};

export const toLint = [
  paths.files.client.js.all,
  paths.files.shared.js.all,
  paths.files.config.gulp,
  paths.files.config.paths,
  paths.files.config.webpack,
  paths.files.render.js.all,
  paths.files.server.js.all,
  paths.files.test.js.all,
];

export const toClean = [
  `app/${paths.files.client.pug.out}`,
  paths.files.client.js.out,
  paths.dirs.es5.client,
  paths.dirs.es5.shared,
  paths.dirs.es5.render,
  paths.dirs.es5.server,
  paths.dirs.es5.test,
];

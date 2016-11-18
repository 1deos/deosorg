/* eslint-disable import/no-extraneous-dependencies */

import gulp from 'gulp';
import babel from 'gulp-babel';
import eslint from 'gulp-eslint';
import flow from 'gulp-flowtype';
import mocha from 'gulp-mocha';
import pug from 'gulp-pug';
import rename from 'gulp-rename';

import * as jetpack from 'fs-jetpack';
import * as yargs from 'yargs';

import webpack from 'webpack-stream';
import webpackMainConfig from './config/webpack.config.electron';
import webpackRendererConfig from './config/webpack.config.prod';

const projectDir = jetpack;
const baseDir = jetpack.cwd('./');
const paths = {
  allSrcJs: 'src/**/*.js?(x)',
  allSrcPug: 'src/**/*.pug?(x)',
  allConfigJs: 'config/**/*.js?(x)',
  allTests: 'test/**/*.js',
  appDir: 'app',
  buildDir: 'build/app',
  entryPointMain: 'src/main.js',
  entryPointRenderer: 'src/index.jsx',
  gulpFile: 'gulpfile.babel.js',
  indexPug: 'src/index.pug',
  gebTest1File: './dojo/git-test.js',
  gebTest2File: './dojo/gittorrentd-test.js',
  allDojoTests: 'dojo/**/*-test.js',
  webpackFileMain: './config/webpack.config.electron.js',
  webpackFileRenderer: './config/webpack.config.prod.js',
};

function getEnvName() {
  return yargs.argv.env || 'dev';
}

gulp.task('env', () => {
  const configFile = `config/env.${getEnvName()}.json`;
  projectDir.copy(configFile,
    baseDir.path('app/env.json'), { overwrite: true });
  projectDir.copy(configFile,
    baseDir.path('src/env.json'), { overwrite: true });
});

gulp.task('pug', () =>
  gulp.src(paths.indexPug)
      .pipe(pug({}))
      .pipe(rename('index.min.html'))
      .pipe(gulp.dest(paths.appDir))
);

gulp.task('lint', () =>
  gulp.src([
    paths.allSrcJs,
    paths.gulpFile,
    paths.webpackFileMain,
    paths.webpackFileRenderer,
  ]).pipe(eslint())
    .pipe(eslint.format())
    .pipe(eslint.failAfterError())
    .pipe(flow({ abort: false }))
);

gulp.task('build', ['lint', 'pug'], () =>
  gulp
    .src(paths.allSrcJs)
    .pipe(babel())
    .pipe(gulp.dest(paths.buildDir))
);

/*gulp .task('dojo-test', () =>
  gulp
    .src(paths.allDojoTests)
    .pipe(mocha())
);*/

gulp.task('test', () =>
  gulp
    .src(paths.allTests)
    .pipe(mocha())
);

gulp.task('main', ['test'], () => {
  gulp
    .src(paths.entryPointMain)
    .pipe(webpack(webpackMainConfig))
    .pipe(gulp.dest(paths.appDir));
  gulp
    .src(paths.entryPointRenderer)
    .pipe(webpack(webpackRendererConfig))
    .pipe(gulp.dest(paths.appDir));
});

gulp.task('watch', () => {
  gulp.watch(paths.allSrcJs, ['main']);
  gulp.watch(paths.allConfigJs, ['main']);
  gulp.watch(paths.allSrcPug, ['pug']);
});

gulp.task('default', ['watch', 'main']);

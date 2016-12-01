/* eslint-disable import/no-extraneous-dependencies */

import gulp from 'gulp';
import babel from 'gulp-babel';
import eslint from 'gulp-eslint';
import flow from 'gulp-flowtype';
import mocha from 'gulp-mocha';
import pug from 'gulp-pug';
import rename from 'gulp-rename';

import del from 'del';
import webpack from 'webpack-stream';

import webpackConfig from './src/dejs/webpack.config.babel';
import { paths, toClean, toLint } from './src/dejs/config.paths';

gulp.task('clean', () => del(toClean));

// .pipe(eslint.failAfterError())
gulp.task('lint', ['clean'], () => gulp.src(toLint)
                            .pipe(eslint())
                            .pipe(eslint.format())
                            .pipe(flow({ abort: false })));

gulp.task('build', ['lint'], () => {
  gulp.src(paths.files.client.js.all)
      .pipe(babel())
      .pipe(gulp.dest(paths.dirs.es5.client));
  gulp.src(paths.files.shared.js.all)
      .pipe(babel())
      .pipe(gulp.dest(paths.dirs.es5.shared));
  gulp.src(paths.files.render.js.all)
      .pipe(babel())
      .pipe(gulp.dest(paths.dirs.es5.render));
  gulp.src(paths.files.server.js.all)
      .pipe(babel())
      .pipe(gulp.dest(paths.dirs.es5.server));
  gulp.src(paths.files.test.js.all)
      .pipe(babel())
      .pipe(gulp.dest(paths.dirs.es5.test));
});

gulp.task('pug', () => gulp.src(paths.files.client.pug.in)
                           .pipe(pug({}))
                           .pipe(rename(paths.files.client.pug.out))
                           .pipe(gulp.dest(paths.dirs.dist)));

gulp.task('main', ['build', 'pug'], () => {
  gulp.src(paths.files.client.js.entry)
    .pipe(webpack(webpackConfig))
    .pipe(gulp.dest(paths.dirs.dist));
});

gulp.task('test', () => gulp.src(paths.files.test.js.out).pipe(mocha()));

gulp.task('watch', () => gulp.watch(toLint, ['main']));

gulp.task('default', ['watch', 'main']);

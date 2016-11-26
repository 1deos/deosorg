/* eslint-disable import/no-extraneous-dependencies, no-console */

import gulp from 'gulp';
import babel from 'gulp-babel';
import del from 'del';
import eslint from 'gulp-eslint';
import flow from 'gulp-flowtype';
import pug from 'gulp-pug';
import mocha from 'gulp-mocha';
import rename from 'gulp-rename';

import webpack from 'webpack-stream';
import webpackMainConfig from './etc/gulp/config.electron';
import webpackRendererConfig from './etc/gulp/config.prod';

import { paths, allJS, allSrcJS, buildDeps, toClean,
} from './etc/gulp/config.paths';

gulp.task('pug', () => gulp.src(paths.files.client.pug.in)
                           .pipe(pug({}))
                           .pipe(rename(paths.files.client.pug.out))
                           .pipe(gulp.dest(paths.dirs.dist)));

gulp.task('lint', () => gulp.src(allJS)
                            .pipe(eslint())
                            .pipe(eslint.format())
                            .pipe(eslint.failAfterError())
                            .pipe(flow({ abort: true })));

gulp.task('clean', () => del(toClean));

gulp.task('build', buildDeps, () => gulp.src(allSrcJS)
                                        .pipe(babel())
                                        .pipe(gulp.dest(paths.dirs.lib)));

gulp.task('test', ['build'], () => gulp.src(paths.files.tests.all)
                                       .pipe(mocha()));

gulp.task('main', ['build'], () => {
  gulp.src(paths.files.config.webpack.electron)
      .pipe(webpack(webpackMainConfig))
      .pipe(gulp.dest(paths.dirs.dist));
  gulp.src(paths.files.config.webpack.prod)
      .pipe(webpack(webpackRendererConfig))
      .pipe(gulp.dest(paths.dirs.dist));
});

gulp.task('watch', () => gulp.watch(allSrcJS, ['main']));

gulp.task('default', ['watch', 'main']);

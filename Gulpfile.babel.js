/* eslint-disable import/no-extraneous-dependencies, no-console */

import gulp from 'gulp';
import babel from 'gulp-babel';
import eslint from 'gulp-eslint';
import flow from 'gulp-flowtype';
import mocha from 'gulp-mocha';
import del from 'del';
import webpack from 'webpack-stream';

import webpackConfig from './etc/gulp/webpack.config.babel';
import { paths, allJS, allSrcJS, buildDeps, toClean } from './etc/gulp/paths';

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

gulp.task('main', ['test'], () => gulp.src(paths.files.client.entry)
                                      .pipe(webpack(webpackConfig))
                                      .pipe(gulp.dest(paths.dirs.dist)));

gulp.task('watch', () => gulp.watch(allSrcJS, ['main']));

gulp.task('default', ['watch', 'main']);

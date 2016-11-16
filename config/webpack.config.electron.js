import webpack from 'webpack';
import validate from 'webpack-validator';
import merge from 'webpack-merge';

import baseConfig from './webpack.config.common';

export default validate(merge(baseConfig, {
  devtool: 'source-map',
  entry: [
    'babel-polyfill',
    './src/main.js',
  ],
  externals: [
    'source-map-support',
  ],
  node: {
    __dirname: false,
    __filename: false,
  },
  output: {
    path: __dirname,
    filename: '../app/main.min.js',
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin({
      compressor: {
        warnings: false,
      },
    }),
    new webpack.BannerPlugin('require("source-map-support").install();',
      {
        raw: true,
        entryOnly: false,
      },
    ),
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('prod'),
      },
    }),
  ],
  target: 'electron-main',
}));

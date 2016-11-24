/* eslint-disable max-len */

import webpack from 'webpack';
import validate from 'webpack-validator';
import merge from 'webpack-merge';
import formatter from 'eslint-formatter-pretty';

import baseConfig from './config.common';

const port = process.env.PORT || 3000;

export default validate(merge(baseConfig, {
  debug: true,
  devtool: 'cheap-module-eval-source-map',
  entry: [
    `webpack-hot-middleware/client?path=http://localhost:${port}/__webpack_hmr`,
    'babel-polyfill',
    './src/index.jsx'
  ],
  output: {
    publicPath: `http://localhost:${port}/`
  },
  module: {
    loaders: [
      {
        test: /\.scss$/,
        loaders: [
          "style",
          "css",
          "sass"
        ]
      },
      {
        test: /\.global\.css$/,
        loaders: [
          'style-loader',
          'css-loader?sourceMap'
        ]
      },
      {
        test: /^((?!\.global).)*\.css$/,
        loaders: [
          'style-loader',
          'css-loader?modules&sourceMap&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]'
        ]
      },
    ]
  },
  eslint: { formatter },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('dev')
    })
  ],
  target: 'electron-renderer'
}));

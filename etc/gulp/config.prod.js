import webpack from 'webpack';
import validate from 'webpack-validator';
import merge from 'webpack-merge';
import ExtractTextPlugin from 'extract-text-webpack-plugin';

import baseConfig from './config.common';

const config = validate(merge(baseConfig, {
  target: 'electron-renderer',
  devtool: 'cheap-module-source-map',
  entry: ['babel-polyfill', './src/client/index.jsx'],
  output: { publicPath: '/' },
  module: {
    loaders: [
      {
        test: /\.scss$/,
        loader: ExtractTextPlugin.extract('style', 'css', 'sass'),
      },
      {
        test: /\.global\.css$/,
        loader: ExtractTextPlugin.extract('style-loader', 'css-loader'),
      },
      {
        test: /^((?!\.global).)*\.css$/,
        loader: ExtractTextPlugin.extract('style-loader',
          'css-loader?modules&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]'),
      },
    ],
  },
  plugins: [
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('prod'),
    }),
    new webpack.optimize.UglifyJsPlugin({
      compressor: {
        screw_ie8: true,
        warnings: false,
      },
    }),
    new ExtractTextPlugin('style.min.css', { allChunks: true }),
  ],
}));

export default config;

import path from 'path';
import validate from 'webpack-validator';

export default validate({
  externals: [
    'bootstrap',
    'font-awesome',
  ],
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        loaders: ['babel-loader'],
        exclude: /node_modules/
      },
      {
        test: /\.json$/,
        loader: 'json-loader'
      }
    ]
  },
  output: {
    filename: 'bundle.min.js',
    libraryTarget: 'commonjs2',
    path: path.join(__dirname, '../../app/')
  },
  plugins: [],
  resolve: {
    extensions: ['', '.js', '.jsx', '.json'],
    packageMains: [
      'webpack',
      'browser',
      'web',
      'browserify',
      ['jam', 'main'],
      'main'
    ]
  }
});

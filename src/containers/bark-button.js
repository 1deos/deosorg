// @flow

import { connect } from 'react-redux';

import { makeBark } from '../actions/dog-actions';
import Button from '../components/button';

const mapDispatchToProps = dispatch => ({
  action: () => {
    dispatch(makeBark());
  },
  actionLabel: 'Bark',
});

export default connect(null, mapDispatchToProps)(Button);

// @flow

import React, { Component, PropTypes }
from 'react';

class Button extends Component {
  static propTypes = {
    action: PropTypes.func.isRequired,
    actionLabel: PropTypes.string.isRequired,
  };
  render() {
    return (
      <button onClick={this.props.action}>
        {this.props.actionLabel}
      </button>
    );
  }
}

export default Button;

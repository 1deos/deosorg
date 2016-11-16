// @flow

import React, { Component, PropTypes } from 'react';

class Message extends Component {
  static propTypes = {
    message: PropTypes.string.isRequired,
  };
  render() {
    return (
      <div>
        {this.props.message}
      </div>
    );
  }
}

export default Message;

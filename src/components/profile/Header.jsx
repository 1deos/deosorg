// @flow
import React, { Component, PropTypes } from 'react';
import styles from './Header.css';

class Header extends Component {
  static propTypes = {
    header_img_url: PropTypes.string.isRequired,
  };
  render() {
    return (
      <img
        className={styles.header_img}
        role="presentation"
        src={this.props.header_img_url}
      />
    );
  }
}

export default Header;

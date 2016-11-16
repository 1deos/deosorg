// @flow

import React, { Component } from 'react';
import { Col } from 'reactstrap';

import styles from './ColLeft.css';

class ColLeft extends Component {
  render() {
    return (
      <Col md="3" id={styles.col_left}>
        <p>left</p>
      </Col>
    );
  }
}

export default ColLeft;

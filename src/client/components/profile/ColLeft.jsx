// @flow

import React, { Component } from 'react';
import { Col } from 'reactstrap';
import styles from './ColLeft.css';

export default class ColLeft extends Component {

  /* Render */
  render() {
    return (
      <Col md="3" id={styles.col_left}>
        <p>left</p>
      </Col>
    );
  }
}

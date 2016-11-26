/* @flow */

/* Import */
import React, { Component } from 'react';
import { Container, Row, Col } from 'reactstrap';
import Tweet from './Tweet';
import CardProfile from './CardProfile';
import CardRight from './CardRight';
import styles from './Body.css';

/* Component */
class Body extends Component {
  render() {
    return (
      <Container>
        <Row>
          <Col md="3" id={styles.atd_col_left}>
            <center>
              <CardProfile />
            </center>
          </Col>
          <Col md="6" id={styles.atd_col_center}>
            <div id={styles.atd_col_center_container}>
              <center>
                <Tweet />
                <Tweet />
                <Tweet />
                <Tweet />
                <Tweet />
                <Tweet />
                <Tweet />
                <Tweet />
                <Tweet />
                <Tweet />
              </center>
            </div>
          </Col>
          <Col md="3" id={styles.atd_col_right}>
            <center>
              <CardRight />
            </center>
          </Col>
        </Row>
      </Container>
    );
  }
}

/* Export */
export default Body;

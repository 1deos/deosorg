// @flow

import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import ColLeft from './ColLeft';
import ColRight from './ColRight';
import Header from './Header';
import Navbar from '../../containers/common/Navbar';
import styles from './App.css';

const HEADER_IMG_URL = 'https://pbs.twimg.com/profile_banners/19844311/1476320409/1500x500';

const TWEETS = [{
  username: 'desantis',
  body: '.@Blockstream Successfully Tests End-to-End #Bitcoin Lightning',
}, {
  username: 'desantis',
  body: 'This is the second tweet',
}];

const App = () => (
  <div>
    <Navbar />
    <Header header_img_url={HEADER_IMG_URL} />
    <Container>
      <Row>
        <ColLeft tweets={TWEETS} />
        <Col md="6" id={styles.col_center}>
          <p>center</p>
        </Col>
        <ColRight />
      </Row>
    </Container>
  </div>
);

export default App;

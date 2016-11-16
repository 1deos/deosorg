/* @flow */

/* Import */
import React, { Component } from 'react';
import { Card, CardBlock } from 'reactstrap';

/* Component */
class CardRight extends Component {

  /* Render */
  render() {
    return (
      <div>
        <Card>
          <CardBlock height="98px">
            <h5>Trending</h5>
          </CardBlock>
        </Card>
      </div>
    );
  }
}

/* Export */
export default CardRight;

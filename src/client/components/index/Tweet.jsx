/* @flow */

/* Import */
import React, { Component } from 'react';
import { Card, Button, CardTitle, CardText } from 'reactstrap';

/* Component */
class Tweet extends Component {

  /* Render */
  render() {
    return (
      <div>
        <Card block className="text-xs-left">
          <CardTitle>Andrew T. DeSantis</CardTitle>
          <CardText>
            .@Blockstream Successfully Tests End-to-End #Bitcoin Lightning
            Micropayment Transaction
          </CardText>
          <Button>➥</Button>
          <Button>⟳</Button>
          <Button>★</Button>
        </Card>
      </div>
    );
  }
}

/* Export */
export default Tweet;

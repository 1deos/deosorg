// @flow

import React, { Component } from 'react';
import { Card, Button, CardTitle, CardText } from 'reactstrap';

class Tweet extends Component {
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

export default Tweet;

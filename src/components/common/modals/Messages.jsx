/* eslint-disable no-console */

import React, { Component }
from 'react';

import { Modal, ModalHeader, ModalBody, NavLink }
from 'reactstrap';

class MessagesModal extends Component {
  constructor(props) {
    super(props);
    this.state = { modal: false };
    this.toggle = this.toggle.bind(this);
  }
  toggle() {
    this.setState({
      modal: !this.state.modal,
    });
  }
  render() {
    return (
      <div>
        <NavLink href="#" onClick={this.toggle}>
          Messages
        </NavLink>
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>
            Direct Messages
          </ModalHeader>
          <ModalBody>
            Modal Body
          </ModalBody>
        </Modal>
      </div>
    );
  }
}

export default MessagesModal;

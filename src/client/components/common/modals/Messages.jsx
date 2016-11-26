/* eslint-disable no-console */

/* Import */
import React, { Component } from 'react';
import { Modal, ModalHeader, ModalBody, NavLink } from 'reactstrap';

/* Component Definition */
class MessagesModal extends Component {

  /* Constructor */
  constructor(props) {
    super(props);
    this.state = { modal: false };
    this.toggle = this.toggle.bind(this);
  }

  /* Toggle */
  toggle() {
    this.setState({
      modal: !this.state.modal,
    });
  }

  /* Render */
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

/* Export */
export default MessagesModal;

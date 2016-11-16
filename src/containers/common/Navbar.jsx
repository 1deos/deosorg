// @flow

import React, { Component } from 'react';
import { Link } from 'react-router';
import { Button,
         Container,
         InputGroup,
         InputGroupAddon,
         Input,
         Navbar as BootstrapNavbar,
         Nav,
         NavItem,
         NavLink
       } from 'reactstrap';

import MessagesModal from '../../components/common/modals/Messages';
import styles from './Navbar.css';

class Navbar extends Component {
  render() {
    return (
      <div>
        <BootstrapNavbar id={styles.atd_navbar} color="faded" light>
          <Container id={styles.atd_navbar_container}>
            <Nav className="pull-xs-left" navbar>
              <NavItem>
                <Link className="nav-link" to="/">Home</Link>
              </NavItem>
              <NavItem>
                <NavLink href="#">Notifications</NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="#">Discover</NavLink>
              </NavItem>
              <NavItem>
                <MessagesModal />
              </NavItem>
            </Nav>
            <Nav className="pull-xs-right" navbar>
              <NavItem id={styles.atd_search}>
                <InputGroup>
                  <Input placeholder="Search" />
                  <InputGroupAddon>🔎</InputGroupAddon>
                </InputGroup>
              </NavItem>
              <NavItem>
                <Link to="/profile">
                  <div id={styles.atd_profile_nav} />
                </Link>
              </NavItem>
              <NavItem>
                <Button>
                  Compose
                </Button>
              </NavItem>
            </Nav>
          </Container>
        </BootstrapNavbar>
      </div>
    );
  }
}

export default Navbar;

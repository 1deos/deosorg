/* @flow */

/* Import */
import React, { Component } from 'react';
import { Card, CardImg, CardLink, CardBlock } from 'reactstrap';
import styles from './CardProfile.css';

/* Component */
class CardProfile extends Component {

  /* Render */
  render() {
    return (
      <div>
        <Card>
          <div id={styles.atd_profile_card_img} />
          <CardImg
            top
            height="96px"
            width="100%"
            src="https://pbs.twimg.com/profile_banners/19844311/1476320409/1500x500"
            alt="Card image cap"
          />
          <CardBlock id={styles.atd_profile_card_block}>
            <div>
              <div id={styles.atd_profile_card_info}>
                <b>Andrew T. DeSantis</b>
                <p>@desantis</p>
              </div>
            </div>
            <div>
              <div id={styles.atd_profile_card_link}>
                <p>Posts</p>
                <CardLink href="#">4,524</CardLink>
              </div>
              <div id={styles.atd_profile_card_link}>
                <p>Following</p>
                <CardLink href="#">409</CardLink>
              </div>
              <div id={styles.atd_profile_card_link}>
                <p>Followers</p>
                <CardLink href="#">8,470</CardLink>
              </div>
            </div>
          </CardBlock>
        </Card>
      </div>
    );
  }
}

/* Export */
export default CardProfile;

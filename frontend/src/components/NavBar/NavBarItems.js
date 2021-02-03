import React from 'react';
import { Label, Menu, Button } from 'semantic-ui-react';
import { Link } from 'react-router-dom';

const leftItems = (config) => {
  const Items = [];
  return Items;
};

const rightItems = (config) => {
  const Items = [];
  if (!config.isLoggedIn) {
    Items.push(
      <Menu.Item name="register">
        <Button as={Link} to="/create-account" primary>
          ساخت حساب
        </Button>
      </Menu.Item>,
    );
  } else {
    Items.push(
    );
  }
  return Items;
};

export default function navbarItems(config) {
  return {
    leftItems: leftItems(config),
    rightItems: rightItems(config),
  };
}
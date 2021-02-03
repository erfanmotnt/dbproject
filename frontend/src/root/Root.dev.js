import React, { Component } from 'react';
import DevTools from '../containers/DevTools';
import { Route, Switch } from 'react-router-dom';
import { connect } from 'react-redux';

import CreateAccount from '../containers/CreateAccount';
import Homepage from '../containers/HomePage';
import ViewProblem from '../containers/ViewProblem';
import Problem from '../containers/Problem';
import ProblemSet from '../containers/ProblemSet';
import NavBar from '../components/NavBar/NavBar';
import NavBarItems from '../components/NavBar/NavBarItems';
import AddAnswer from '../containers/AddAnswer';
import AddTag from '../containers/AddTag';
import AddSubtag from '../containers/AddSubtag';

import '../styles/App.css';
import PrivateRoute from './PrivateRoute';

import { logout } from '../redux/actions/account'


const Root = ({ isLoggedIn, username, logout }) => {
  return (
    <div>
      <NavBar config={NavBarItems({
        isLoggedIn: isLoggedIn,
        username: username,
        logout: logout,
      })}>
        <Switch>
          <Route path="/create-account" component={CreateAccount} />
          <Route path="/answer/:pid?" component={AddAnswer} />
          <Route path="/tag/" component={AddTag} />
          <Route path="/subtag/" component={AddSubtag} />
          <Route path="/problem/:id" component={ViewProblem} />
          <Route path="/makeProblem/" component={Problem} />
          <Route path="/editProblem/:id" component={Problem} />
          <Route path="/problemset/page/:id" render={() => <ProblemSet key={Math.random()} />} />
          <Route path="/" component={Homepage} />
        </Switch>
        <DevTools />
      </NavBar>
    </div>
  );
}

const mapStateToProps = (state) => ({
  isLoggedIn: state.account.token,
})

export default connect(mapStateToProps, { logout })(Root);
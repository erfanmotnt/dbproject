import React, { useEffect } from 'react'
import { connect } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { Slide, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import 'semantic-ui-css/semantic.min.css';
import { ThemeProvider, StylesProvider } from '@material-ui/styles';
import { CssBaseline } from '@material-ui/core';
import { initRedirect } from './redux/actions/redirect';
import RTLMuiTheme from './theme/RTLMuiTheme';
import jss from './utils/jssRTL';
import Root from './root/Root';

const Toast = () => (
  <ToastContainer
    rtl
    position="top-left"
    autoClose={5000}
    transition={Slide}
    hideProgressBar={false}
    pauseOnHover={false}
    pauseOnFocusLoss={false}
    closeOnClick
    limit={3}
  />
);

const App = ({ redirectTo, initRedirect }) => {
  const history = useHistory();
  useEffect(() => {
    if (redirectTo !== null) {
      history.push(redirectTo);
      initRedirect();
    }
  }, [redirectTo, initRedirect, history]);

  return (
    <ThemeProvider theme={RTLMuiTheme}>
      <StylesProvider jss={jss}>
        <CssBaseline />
        <Root />
        <Toast />
      </StylesProvider>
    </ThemeProvider>
  );
};

const mapStateToProps = (state) => ({
  redirectTo: state.redirect.redirectTo,
});

export default connect(mapStateToProps, { initRedirect })(App);

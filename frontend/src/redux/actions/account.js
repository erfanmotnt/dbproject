import * as actionTypes from '../actionTypes';
import * as URLs from './urls';

import { CALL_API } from '../middleware/api/api';

const _getUser = (id) => ({
  [CALL_API]: {
    types: [
      actionTypes.USER_REQUEST,
      actionTypes.USER_SUCCESS,
      actionTypes.USER_FAILURE,
    ],
    url: URLs.GET_USER(id),
    fetchOptions: {
      method: 'GET',
    },
  },
});


export const getUser = (id) => (
  dispatch,
  getState
) => {
  if (getState().account.users && getState().account.users.find(user => user.id == id)) {
    return getState().account.users.find(user => user.id == id);
  }
  return dispatch(_getUser(id));
};


export const login = (username, password) => ({
  [CALL_API]: {
    types: [
      actionTypes.LOGIN_REQUEST,
      actionTypes.LOGIN_SUCCESS,
      actionTypes.LOGIN_FAILURE,
    ],
    url: URLs.LOGIN_USER,
    payload: {
      username,
    },
    fetchOptions: {
      method: 'POST',
      body: { username, password },
    },
  },
});


export const createAccount = (
  username,
  firstname,
  lastname,
  phone,
  email,
  role = 'w',
) => ({
  [CALL_API]: {
    types: [
      actionTypes.CREATE_ACCOUNT_REQUEST,
      actionTypes.CREATE_ACCOUNT_SUCCESS,
      actionTypes.CREATE_ACCOUNT_FAILURE,
    ],
    url: URLs.ACCOUNT,
    fetchOptions: {
      method: 'POST',
      body: {
        username,
        firstname,
        lastname,
        phone,
        email,
        role,
      },
    },
  },
});


export const logout = () => ({
  [CALL_API]: {
    types: [
      actionTypes.LOGOUT_REQUEST,
      actionTypes.LOGOUT_SUCCESS,
      actionTypes.LOGOUT_FAILURE,
    ],
    url: URLs.LOGOUT_USER,
    fetchOptions: {
      method: 'POST',
      dontContentType: true,
    },
  },
});
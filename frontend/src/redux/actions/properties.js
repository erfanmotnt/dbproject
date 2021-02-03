import * as actionTypes from '../actionTypes';
import * as URLs from './urls';

import { CALL_API } from '../middleware/api/api';

const fetchTags = () => ({
  [CALL_API]: {
    types: [
      actionTypes.TAGS_REQUEST,
      actionTypes.TAGS_SUCCESS,
      actionTypes.TAGS_FAILURE,
    ],
    url: URLs.GET_TAGS,
    fetchOptions: {
      method: 'GET',
    },
  },
});

export const getTags = () => (
  dispatch,
  getState
) => {
  const tags = getState().properties.tags;
  if (tags.length === 0) {
    return dispatch(fetchTags());
  }
};

export const createTag = (name) => ({
  [CALL_API]: {
    types: [
      actionTypes.CREATE_TAGS_REQUEST,
      actionTypes.CREATE_TAGS_SUCCESS,
      actionTypes.CREATE_TAGS_FAILURE,
    ],
    url: URLs.TAG,
    fetchOptions: {
      method: 'POST',
      body: {
        cusername: null,
        tname: name,
      }
    },
  },
})

export const createSubtag = (subtagName, tagName) => ({
  [CALL_API]: {
    types: [
      actionTypes.CREATE_SUBTAGS_REQUEST,
      actionTypes.CREATE_SUBTAGS_SUCCESS,
      actionTypes.CREATE_SUBTAGS_FAILURE,
    ],
    url: URLs.SUBTAG,
    fetchOptions: {
      method: 'POST',
      body: {
        cusername: null,
        tname: tagName,
        stname: subtagName,
      }
    },
  },
})

const fetchSubtags = () => ({
  [CALL_API]: {
    types: [
      actionTypes.SUBTAGS_REQUEST,
      actionTypes.SUBTAGS_SUCCESS,
      actionTypes.SUBTAGS_FAILURE,
    ],
    url: URLs.GET_SUBTAGS,
    fetchOptions: {
      method: 'GET',
    },
  },
});

export const getSubtags = () => (
  dispatch,
  getState
) => {
  const subtags = getState().properties.subtags;
  if (subtags.length === 0) {
    return dispatch(fetchSubtags());
  }
};

const fetchEvents = () => ({
  [CALL_API]: {
    types: [
      actionTypes.EVENTS_REQUEST,
      actionTypes.EVENTS_SUCCESS,
      actionTypes.EVENTS_FAILURE,
    ],
    url: URLs.GET_EVENTS,
    fetchOptions: {
      method: 'GET',
    },
  },
});

export const getEvents = () => (
  dispatch,
  getState
) => {
  const events = getState().properties.events;
  if (events.length === 0) {
    return dispatch(fetchEvents());
  }
};

const fetchSources = () => ({
  [CALL_API]: {
    types: [
      actionTypes.SOURCES_REQUEST,
      actionTypes.SOURCES_SUCCESS,
      actionTypes.SOURCES_FAILURE,
    ],
    url: URLs.GET_SOURCES,
    fetchOptions: {
      method: 'GET',
    },
  },
});

export const getSources = () => (
  dispatch,
  getState
) => {
  const sources = getState().properties.sources;
  if (sources.length === 0) {
    return dispatch(fetchSources());
  }
};
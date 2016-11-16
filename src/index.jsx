import React from 'react';
import ReactDOM from 'react-dom';
import createLogger from 'redux-logger';
import thunk from 'redux-thunk';
/* eslint-disable import/no-extraneous-dependencies */
import createHistory from 'history/lib/createHashHistory';
/* eslint-enable import/no-extraneous-dependencies */
import * as Immutable from 'immutable';

import { hashHistory, Router, Route, IndexRoute, useRouterHistory }
from 'react-router';
import { syncHistoryWithStore, routerMiddleware, push }
from 'react-router-redux';
import { combineReducers }
from 'redux-immutable';
import { createStore, compose, applyMiddleware }
from 'redux';
import { Provider }
from 'react-redux';

import * as dogActions from './actions/dog-actions';
import dogReducer from './reducers/dog-reducer';
import customReducer from './reducers/custom-reducer';
import Index from './containers/pages/Index';
import Profile from './containers/pages/Profile';
import App from './containers/App';

import './index.scss';

const initialState = Immutable.Map();
const rootReducer = combineReducers({ dogReducer, routing: customReducer });
const actionCreators = { ...dogActions, push };
const router = routerMiddleware(hashHistory);
const logger = createLogger({ level: 'info', collapsed: true });
/* eslint-disable no-underscore-dangle */
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
                       ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__({ actionCreators })
                       : compose;
/* eslint-enable no-underscore-dangle */
const enhancer = composeEnhancers(applyMiddleware(thunk, router, logger));
const store = createStore(rootReducer, initialState, enhancer);
const createSelectLocationState = () => {
  let prevRoutingState;
  let prevRoutingStateJS;
  return (state) => {
    const routingState = state.get('routing'); // or state.routing
    if (typeof prevRoutingState === 'undefined' || prevRoutingState !== routingState) {
      prevRoutingState = routingState;
      prevRoutingStateJS = routingState.toJS();
    }
    return prevRoutingStateJS;
  };
};
const browserHistory = useRouterHistory(createHistory)({ basename: '/' });
const history = syncHistoryWithStore(browserHistory, store, {
  selectLocationState: createSelectLocationState(),
});

ReactDOM.render(
  <Provider store={store}>
    <div>
      <Router history={history}>
        <Route path="/" component={App}>
          <IndexRoute component={Index} />
          <Route path="profile" component={Profile} />
        </Route>
      </Router>
      </div>
  </Provider>
  , document.getElementById('root')
);

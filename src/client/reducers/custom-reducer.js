import * as Immutable from 'immutable';
import { LOCATION_CHANGE } from 'react-router-redux';

const initialState = Immutable.fromJS({
  locationBeforeTransitions: undefined,
});

const customReducer = (state: Object = initialState, action: Object) => {
  switch (action.type) {
    case LOCATION_CHANGE:
      return state.merge({ locationBeforeTransitions: action.payload });
    default:
      return state;
  }
};

export default customReducer;

export default {
  SET_CURRENT_USER(state, currentUser) {
    state.currentUser = currentUser;
  },
  SET_USERS(state, users) {
    state.users = users;
  },
  PUT_USER(state, userEdit) {
    state.userEdit = userEdit;
  },
  SET_USER(state, userEdit) {
    state.userEdit = userEdit;
  },
  SET_USER_UPDATE(state, userEdit) {
    state.userEdit = Object.assign({}, state.userEdit, userEdit);
  },
};

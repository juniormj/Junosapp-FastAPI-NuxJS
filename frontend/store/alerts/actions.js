export default {
  setError({ commit }, alert) {
    commit("SET_ERROR", alert);
  },
  setSuccess({ commit }, alert) {
    commit("SET_SUCCESS", alert);
  },
};

export const state = () => ({
  logs: {},
});

export const actions = {
  setLogs({ commit }, token) {
    this.$axios
      .$get("/logs/log", {
        headers: { Authorization: "Bearer " + token },
      })
      .then((resp) => {
        commit("SET_LOGS", resp);
      })
      .catch(({ response }) => {
        console.log(response.data);
      });
  },
  setLogsByLogin({ commit }, login) {
    this.$axios
      .$get(`/logs/log/${login}`)
      .then((resp) => {
        commit("SET_LOGS", resp);
      })
      .catch((err) => {
        console.log(err);
        commit("SET_LOGS", err);
      });
  },
};

export const mutations = {
  SET_LOGS(state, logs) {
    state.logs = logs;
  },
};

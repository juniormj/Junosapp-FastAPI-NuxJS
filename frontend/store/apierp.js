export const state = () => ({
  clientServico: {},
  historicoOS: {},
});

export const actions = {
  setClientesServicos({ commit }, login) {
    this.$axios
      .$get(`/api_erps/${login}`, {
        headers: { Authorization: "Bearer " + localStorage.getItem("token") },
      })
      .then((resp) => {
        commit("SET_CLIENTE_SERVICO", resp.dados[0]);
      });
  },
  setHistoricoOS({ commit }, idCliente) {
    this.$axios
      .$get(`/api_erps/os/${idCliente}`, {
        headers: { Authorization: "Bearer " + localStorage.getItem("token") },
      })
      .then((resp) => {
        commit("SET_HISTORICO_CLIENTE", resp);
      });
  },
};

export const mutations = {
  SET_CLIENTE_SERVICO(state, dados) {
    state.clientServico = dados;
  },
  SET_HISTORICO_CLIENTE(state, dados) {
    state.historicoOS = dados;
  },
};

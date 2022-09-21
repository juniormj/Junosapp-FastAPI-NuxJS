export default {
  async getResult({ dispatch }, login) {
    const header = {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    };
    try {
      const resp = await this.$axios.$get(`/clients/${login}`, header);
      return resp;
    } catch ({ response }) {
      dispatch("alerts/setError", response.data.detail, { root: true });
      return response;
    }
  },

  getDesconect(context, dados) {
    this.$axios.$get(`/client/logoff/${dados.login}/${dados.ip_olt}`, {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    });
  },
};

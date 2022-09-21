export default {
  getTraffic(context, dados) {
    return this.$axios.$get(
      `/tests/update/${dados.interface}/${dados.ip_olt}`,
      {
        headers: { Authorization: "Bearer " + localStorage.getItem("token") },
      }
    );
  },

  getExtensivePppoe(context, dados) {
    return this.$axios.$get(`/tests/extensive/${dados.login}/${dados.ip_olt}`, {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    });
  },
};

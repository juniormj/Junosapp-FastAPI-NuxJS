export default {
  // ############################################
  // ##               METODO CADASTRAR
  // ############################################
  async setCadBras({ dispatch }, form) {
    try {
      const resp = await this.$axios.$post("/bras", form, {
        headers: { Authorization: "Bearer " + localStorage.getItem("token") },
      });
      dispatch("alerts/setSuccess", "Dispositivo cadastrado com sucesso", {
        root: true,
      });
      return resp;
    } catch ({ response }) {
      if (response.data.detail[0].msg) {
        dispatch("alerts/setError", response.data.detail[0].msg, {
          root: true,
        });
        return response.data.detail;
      } else {
        dispatch("alerts/setError", response.data.detail, {
          root: true,
        });
        return response.data.detail;
      }
    }
  },
  // ############################################
  // ##          METODO LISTAR DISPOSITIVOS
  // ############################################
  setDevices({ commit }) {
    this.$axios
      .$get("/bras", {
        headers: { Authorization: "Bearer " + localStorage.getItem("token") },
      })
      .then((resp) => {
        commit("SET_BRAS", resp);
      })
      .catch(({ response }) => {
        commit("SET_BRAS", response.data);
      });
  },
  // ############################################
  // ##         METODO LISTAR CONCENTRADOR
  // ############################################
  getDevice({ commit }, id) {
    this.$axios
      .$get(`/bras/${id}`, {
        headers: { Authorization: "Bearer " + localStorage.getItem("token") },
      })
      .then((resp) => {
        commit("PUT_DEVICE", resp);
      });
  },
  // ############################################
  // ##       METODO EDITAR CONCENTRADOR
  // ############################################
  async putDevice({ commit, dispatch }, dados) {
    const header = {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    };
    try {
      dispatch("alerts/setSuccess", "Dispositivo Alterado com Sucesso", {
        root: true,
      });
      const resp = await this.$axios.$put(
        `/bras/${dados.id}`,
        dados.device,
        header
      );
      commit("PUT_DEVICE", resp);
      return resp;
    } catch ({ response }) {
      dispatch("alerts/setError", response.data.detail, { root: true });
      return response;
    }
  },
  // ############################################
  // ##         METODO REMOVER DISPOSITIVO
  // ############################################
  async deleteDevice({ dispatch }, id) {
    const header = {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    };
    try {
      dispatch("alerts/setSuccess", "Dispositivo removido com sucesso", {
        root: true,
      });
      await this.$axios.$delete(`/bras/${id}`, header);
      dispatch("setDevices");
    } catch ({ response }) {
      dispatch("alerts/setError", response.data.detail, { root: true });
      return response;
    }
  },
};

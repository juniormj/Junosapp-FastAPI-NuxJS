export default {
  // ############################################
  // ##               METODO CADASTRAR
  // ############################################
  async setCadRadius({ dispatch }, form) {
    const header = {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    };
    try {
      const resp = await this.$axios.$post("/erps", form, header);
      dispatch("alerts/setSuccess", "ERP cadastrado com sucesso", {
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
  // ##          METODO LISTAR ERPS
  // ############################################
  setRadius({ commit }) {
    this.$axios
      .$get("/erps", {
        headers: { Authorization: "Bearer " + localStorage.getItem("token") },
      })
      .then((resp) => {
        commit("SET_ERPS", resp);
      })
      .catch(({ response }) => {
        commit("SET_ERPS", response.data);
      });
  },
  // ############################################
  // ##         METODO LISTAR CONCENTRADOR
  // ############################################
  getErp({ commit }, id) {
    this.$axios
      .$get(`/erps/${id}`, {
        headers: { Authorization: "Bearer " + localStorage.getItem("token") },
      })
      .then((resp) => {
        commit("PUT_ERP", resp);
      });
  },
  // ############################################
  // ##       METODO EDITAR ERP
  // ############################################
  async putErp({ commit, dispatch }, dados) {
    const header = {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    };
    try {
      dispatch("alerts/setSuccess", "Dispositivo Alterado com Sucesso", {
        root: true,
      });
      const resp = await this.$axios.$put(
        `/erps/${dados.id}`,
        dados.erp,
        header
      );
      commit("PUT_ERP", resp);
      return resp;
    } catch ({ response }) {
      dispatch("alerts/setError", response.data.detail, { root: true });
      return response;
    }
  },
  // ############################################
  // ##         METODO REMOVER DISPOSITIVO
  // ############################################
  async deleteErp({ dispatch }, id) {
    const header = {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    };
    try {
      dispatch("alerts/setSuccess", "ERP removido com sucesso", {
        root: true,
      });
      await this.$axios.$delete(`/erps/${id}`, header);
      dispatch("setRadius");
    } catch ({ response }) {
      dispatch("alerts/setError", response.data.detail, { root: true });
      return response;
    }
  },
};

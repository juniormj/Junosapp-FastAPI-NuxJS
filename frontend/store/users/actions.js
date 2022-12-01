export default {
  // ############################################
  // ##               METODO CADASTRAR
  // ############################################
  async setFormUser({ dispatch }, form) {
    const header = {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    };
    try {
      const resp = await this.$axios.$post("/usuarios/signup", form, header);
      dispatch("alerts/setSuccess", "Usuário cadastrado com sucesso", {
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
  // ##               METODO LOGIN
  // ############################################
  async setLogin({ dispatch }, user) {
    try {
      dispatch("alerts/setSuccess", "Bem vindo ao sistema Junos APP", {
        root: true,
      });
      const dados = await this.$axios.$post("/usuarios/login", user);
      localStorage.setItem("token", dados.access_token);
      dispatch("viewMe");
      return dados;
    } catch ({ response }) {
      dispatch("alerts/setError", response.data.detail, { root: true });
      return response;
    }
  },
  // ############################################
  // ##               METODO ME
  // ############################################
  viewMe({ commit }) {
    this.$axios
      .get("/usuarios/logado", {
        headers: { Authorization: "Bearer " + localStorage.getItem("token") },
      })
      .then((resp) => {
        commit("SET_CURRENT_USER", resp.data);
      });
  },
  // ############################################
  // ##         METODO SETAR USER NULL
  // ############################################
  setNullUser({ commit }, user) {
    commit("SET_CURRENT_USER", user);
  },
  // ############################################
  // ##          METODO LISTAR USUÁRIOS
  // ############################################
  setUsers({ commit }) {
    this.$axios
      .$get("/usuarios", {
        headers: { Authorization: "Bearer " + localStorage.getItem("token") },
      })
      .then((resp) => {
        commit("SET_USERS", resp);
      })
      .catch(({ response }) => {
        commit("SET_USERS", response.data);
      });
  },
  // ############################################
  // ##         METODO LISTAR USUARIO
  // ############################################
  getUser({ commit }, id) {
    this.$axios
      .$get(`/usuarios/${id}`, {
        headers: { Authorization: "Bearer " + localStorage.getItem("token") },
      })
      .then((resp) => {
        commit("PUT_USER", resp);
      });
  },
  // ############################################
  // ##         METODO EDITAR USUÁRIO
  // ############################################
  async putUser({ commit, dispatch }, dados) {
    const header = {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    };
    try {
      dispatch("alerts/setSuccess", "Usuário Alterado com Sucesso", {
        root: true,
      });
      const resp = await this.$axios.$put(
        `/usuarios/${dados.id}`,
        dados.user,
        header
      );
      commit("PUT_USER", resp);
      return resp;
    } catch ({ response }) {
      dispatch("alerts/setError", response.data.detail, { root: true });
      return response;
    }
  },
  // ############################################
  // ##         METODO REMOVER USUÁRIO
  // ############################################
  async deleteUser({ dispatch }, id) {
    const header = {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    };
    try {
      dispatch("alerts/setSuccess", "Usuário removido com sucesso", {
        root: true,
      });
      await this.$axios.$delete(`/usuarios/${id}`, header);
      dispatch("setUsers");
    } catch ({ response }) {
      dispatch("alerts/setError", response.data.detail, { root: true });
      return response;
    }
  },
};

<template>
  <v-col class="my-10">
    <v-toolbar color="#284177" class="mb-2 pa-1 borderLeft" dark>
      <v-toolbar-title class="mx-auto">
        FORMLÁRIO EDITAR USUÁRIO
      </v-toolbar-title>
    </v-toolbar>
    <v-form v-if="userEdit" class="my-5">
      <v-text-field v-model="nome" label="Nome" required></v-text-field>
      <v-text-field
        v-model="sobrenome"
        label="Sobre Nome"
        required
      ></v-text-field>
      <v-text-field v-model="email" label="E-mail" required></v-text-field>
      <v-text-field v-model="senha" label="Senha" required></v-text-field>
      <v-checkbox v-model="eh_admin" label="Admin" required></v-checkbox>
      <v-btn color="success" class="mr-4" @click="enviaForm"> Enviar </v-btn>
    </v-form>
    <v-alert
      v-if="error"
      class="mb-8"
      type="error"
      elevation="4"
      dismissible
      outlined
      @click="errorNull"
    >
      {{ error }}
    </v-alert>
  </v-col>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState("users", ["userEdit"]),
    ...mapState("alerts", ["error"]),
    nome: {
      get() {
        return this.userEdit.nome;
      },
      set(nome) {
        this.$store.commit("users/SET_USER_UPDATE", { nome });
      },
    },
    sobrenome: {
      get() {
        return this.userEdit.sobrenome;
      },
      set(sobrenome) {
        this.$store.commit("users/SET_USER_UPDATE", { sobrenome });
      },
    },
    email: {
      get() {
        return this.userEdit.email;
      },
      set(email) {
        this.$store.commit("users/SET_USER_UPDATE", { email });
      },
    },
    senha: {
      get() {
        return this.userEdit.senha;
      },
      set(senha) {
        this.$store.commit("users/SET_USER_UPDATE", { senha });
      },
    },
    eh_admin: {
      get() {
        return this.userEdit.eh_admin;
      },

      // eslint-disable-next-line camelcase
      set(eh_admin) {
        // eslint-disable-next-line camelcase
        this.$store.commit("users/SET_USER_UPDATE", { eh_admin });
      },
    },
  },
  async created() {
    await this.$store.dispatch("users/getUser", this.$route.params.id);
  },
  methods: {
    async enviaForm() {
      const dados = { id: this.$route.params.id, user: this.userEdit };
      await this.$store.dispatch("users/putUser", dados);
      this.$router.push("/admin");
    },
    async errorNull() {
      await this.$store.dispatch("alerts/setError", null);
    },
  },
};
</script>

<style scoped>
.borderLeft {
  border-radius: 50px 0px 50px 0px !important;
}
.borderRight {
  border-radius: 0px 50px 0px 50px !important;
}
.border {
  border: 2px solid white !important;
}
</style>

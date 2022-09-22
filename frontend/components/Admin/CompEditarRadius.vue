<template>
  <v-col class="my-10">
    <v-toolbar color="#284177" class="mb-2 pa-1 borderLeft" dark>
      <v-toolbar-title class="mx-auto"> FORMLÁRIO EDITAR ERP </v-toolbar-title>
    </v-toolbar>
    <v-form v-if="erpEdit" class="my-5">
      <v-text-field v-model="ip" label="Endereço IP" required></v-text-field>
      <v-text-field
        v-model="login"
        label="Login de acesso ao ERP"
        required
      ></v-text-field>
      <v-text-field
        v-model="senha"
        label="Senha de acesso ao ERP"
        required
      ></v-text-field>
      <v-text-field
        v-model="identificador"
        label="Identificador"
        required
      ></v-text-field>
      <v-text-field v-model="vendor" label="Empresa" required></v-text-field>
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
    ...mapState("erp", ["erpEdit"]),
    ...mapState("alerts", ["error"]),
    ip: {
      get() {
        return this.erpEdit.ip;
      },
      set(ip) {
        this.$store.commit("erp/SET_ERP_UPDATE", { ip });
      },
    },
    login: {
      get() {
        return this.erpEdit.login;
      },
      set(login) {
        this.$store.commit("erp/SET_ERP_UPDATE", { login });
      },
    },
    senha: {
      get() {
        return this.erpEdit.senha;
      },
      set(senha) {
        this.$store.commit("erp/SET_ERP_UPDATE", { senha });
      },
    },
    identificador: {
      get() {
        return this.erpEdit.identificador;
      },
      set(identificador) {
        this.$store.commit("erp/SET_ERP_UPDATE", { identificador });
      },
    },
    vendor: {
      get() {
        return this.erpEdit.vendor;
      },
      set(vendor) {
        this.$store.commit("erp/SET_ERP_UPDATE", { vendor });
      },
    },
  },
  async created() {
    await this.$store.dispatch("erp/getErp", this.$route.params.id);
  },
  methods: {
    async enviaForm() {
      const dados = { id: this.$route.params.id, erp: this.erpEdit };
      await this.$store.dispatch("erp/putErp", dados);
      this.$router.push("/admin/radius");
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

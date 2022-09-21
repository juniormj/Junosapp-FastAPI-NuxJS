<template>
  <v-col class="my-10">
    <v-toolbar color="#284177" class="mb-2 pa-1 borderLeft" dark>
      <v-toolbar-title class="mx-auto">
        FORMLÁRIO EDITAR DISPOSITIVO
      </v-toolbar-title>
    </v-toolbar>
    <v-form v-if="deviceEdit" class="my-5">
      <v-text-field
        v-model="local"
        label="Localidade do concentrador"
        required
      ></v-text-field>
      <v-text-field v-model="ip" label="Endereço IP" required></v-text-field>
      <v-text-field
        v-model="login"
        label="Login de acesso ao concentrador"
        required
      ></v-text-field>
      <v-text-field
        v-model="senha"
        label="Senha de acesso ao concentrador"
        required
      ></v-text-field>
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
    ...mapState("devices", ["deviceEdit"]),
    ...mapState("alerts", ["error"]),
    local: {
      get() {
        return this.deviceEdit.local;
      },
      set(local) {
        this.$store.commit("devices/SET_DEVICE_UPDATE", { local });
      },
    },
    ip: {
      get() {
        return this.deviceEdit.ip;
      },
      set(ip) {
        this.$store.commit("devices/SET_DEVICE_UPDATE", { ip });
      },
    },
    login: {
      get() {
        return this.deviceEdit.login;
      },
      set(login) {
        this.$store.commit("devices/SET_DEVICE_UPDATE", { login });
      },
    },
    senha: {
      get() {
        return this.deviceEdit.senha;
      },
      set(senha) {
        this.$store.commit("devices/SET_DEVICE_UPDATE", { senha });
      },
    },
  },
  async created() {
    await this.$store.dispatch("devices/getDevice", this.$route.params.id);
  },
  methods: {
    async enviaForm() {
      const dados = { id: this.$route.params.id, device: this.deviceEdit };
      await this.$store.dispatch("devices/putDevice", dados);
      this.$router.push("/admin/dispositivo");
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

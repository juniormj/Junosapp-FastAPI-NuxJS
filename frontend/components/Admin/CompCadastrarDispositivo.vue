<template>
  <div>
    <v-form ref="form">
      <v-text-field v-model="form.local" label="Local" required></v-text-field>
      <v-text-field
        v-model="form.ip"
        label="Endereço IP"
        required
      ></v-text-field>
      <v-text-field v-model="form.login" label="Login" required></v-text-field>
      <v-text-field v-model="form.senha" label="Senha" required></v-text-field>
      <v-btn color="success" class="mr-4" @click="enviaForm">
        Enviar Formulário
      </v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        local: "",
        ip: "",
        login: "",
        senha: "",
      },
    };
  },

  methods: {
    async enviaForm() {
      const cad = await this.$store.dispatch("devices/setCadBras", this.form);
      console.log(cad);
      if (cad) {
        this.$router.push("/admin");
      }
    },
  },
};
</script>

<style scoped>
</style>

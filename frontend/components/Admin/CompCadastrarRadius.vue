<template>
  <div>
    <v-form ref="form">
      <v-text-field
        v-model="form.ip"
        label="Endereço IP"
        required
      ></v-text-field>
      <v-text-field v-model="form.login" label="Login" required></v-text-field>
      <v-text-field v-model="form.senha" label="Senha" required></v-text-field>
      <v-text-field
        v-model="form.vendor"
        label="Nome da empresa"
        required
      ></v-text-field>
      <v-text-field
        v-model="form.identificador"
        label="Identificador"
        required
      ></v-text-field>
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
        ip: "",
        login: "",
        senha: "",
        vendor: "",
        identificador: "",
      },
    };
  },

  methods: {
    async enviaForm() {
      const cad = await this.$store.dispatch("erp/setCadRadius", this.form);
      if (cad) {
        this.$router.push("/admin/radius");
      }
    },
  },
};
</script>

<style scoped>
</style>

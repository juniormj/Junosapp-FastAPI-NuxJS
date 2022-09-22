<template>
  <div>
    <v-form ref="form">
      <v-text-field v-model="form.nome" label="Nome" required></v-text-field>
      <v-text-field
        v-model="form.sobrenome"
        label="Sobre Nome"
        required
      ></v-text-field>
      <v-text-field v-model="form.email" label="E-mail" required></v-text-field>
      <v-text-field v-model="form.senha" label="Senha" required></v-text-field>
      <v-checkbox v-model="form.eh_admin" label="Admin?" required></v-checkbox>
      <v-btn color="success" class="mr-4" @click="enviaForm">
        Enviar Formulário
      </v-btn>
      <v-btn color="warning"> Limpar Formulário </v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        nome: "",
        sobrenome: "",
        email: "",
        senha: "",
        eh_admin: false,
      },
    };
  },

  methods: {
    async enviaForm() {
      const cad = await this.$store.dispatch("users/setFormUser", this.form);
      if (cad) {
        this.$router.push("/");
      }
    },
  },
};
</script>

<style scoped>
</style>

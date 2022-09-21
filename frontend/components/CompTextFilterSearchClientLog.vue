<template>
  <v-text-field
    v-model="cliente"
    label="Localizar cliente"
    prepend-inner-icon="fas fa-search"
    filled
    required
    rounded
    color="#284177"
    @keyup.enter="sendlogin"
  />
</template>
<script>
export default {
  data() {
    return {
      cliente: "",
    };
  },
  methods: {
    async sendlogin() {
      await this.$store.dispatch("logs/setLogsByLogin", this.cliente);
    },
  },
};
</script>

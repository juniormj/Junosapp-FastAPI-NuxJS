<template>
  <v-app>
    <v-main>
      <v-container fluid>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "DefaultLayout",

  async mounted() {
    const token = localStorage.getItem("token");
    if (token) {
      await this.$store.dispatch("users/viewMe");
    } else {
      await this.$store.dispatch(
        "alerts/setError",
        "Você não está logado, por favor, faça o login."
      );
      return this.$router.push("/login");
    }
  },
};
</script>

<style scoped>
.v-application {
  background: #eeeeee;
}
</style>

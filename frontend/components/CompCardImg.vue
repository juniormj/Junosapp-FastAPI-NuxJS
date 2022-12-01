<template>
  <v-hover v-if="currentUser" v-slot="{ hover }">
    <v-card
      class="mb-2 pa-1 borderLeft"
      :elevation="hover ? 24 : 10"
      color="#284177"
    >
      <v-toolbar color="#284177" dark flat>
        <v-img
          lazy-src="/ateltelecom.png"
          src="/ateltelecom.png"
          max-width="70"
          class="mx-auto"
        />
      </v-toolbar>
    </v-card>
  </v-hover>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState("users", ["currentUser"]),
  },
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

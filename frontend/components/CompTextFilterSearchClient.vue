<template>
  <v-text-field
    v-if="currentUser"
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
import { mapState } from "vuex";
export default {
  data() {
    return {
      cliente: "",
    };
  },
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
  methods: {
    sendlogin() {
      this.$router.replace(`/result/${this.cliente}`);
    },
  },
};
</script>

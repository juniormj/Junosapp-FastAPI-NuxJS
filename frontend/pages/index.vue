<template>
  <v-row>
    <v-col cols="12" sm="2">
      <CompCardImg />
      <CompCardMenuEsquerdo />
    </v-col>
    <v-col cols="12" sm="7">
      <CompTextFilterSearchClient />
      <v-alert
        v-if="alerts.error"
        type="error"
        elevation="4"
        dismissible
        shaped
        outlined
        @click="errorNull"
      >
        {{ alerts.error }}
      </v-alert>
      <v-alert
        v-if="alerts.sucesso"
        type="success"
        elevation="4"
        dismissible
        shaped
        outlined
        @click="successNull"
      >
        {{ alerts.sucesso }}
      </v-alert>
      <CompCarrosel />
    </v-col>
    <v-col cols="12" sm="3">
      <CompCardPerfil />
    </v-col>
  </v-row>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "IndexPage",
  computed: {
    ...mapState(["alerts"]),
  },
  methods: {
    async errorNull() {
      await this.$store.dispatch("alerts/setError", null);
    },
    async successNull() {
      await this.$store.dispatch("alerts/setSuccess", null);
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

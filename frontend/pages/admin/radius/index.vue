<template>
  <v-row v-if="currentUser">
    <v-col cols="12" sm="2">
      <CompCardImg />
      <CompCardMenuEsquerdoAdmin />
    </v-col>
    <v-col cols="12" sm="7">
      <!-- COMEÇA -->

      <v-tabs v-model="tab" align-with-title color="#284177">
        <v-tab> Lista Radius </v-tab>
        <v-tab> Cadastro de Radius</v-tab>
      </v-tabs>

      <v-alert
        v-if="sucesso"
        type="success"
        elevation="4"
        dismissible
        shaped
        outlined
        @click="successNull"
      >
        {{ sucesso }}
      </v-alert>
      <v-alert
        v-if="error"
        type="error"
        elevation="4"
        dismissible
        shaped
        outlined
        @click="errorNull"
      >
        {{ error }}
      </v-alert>

      <v-tabs-items v-model="tab">
        <v-tab-item>
          <v-card flat>
            <v-card-text><CompTabelaRadius /></v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-card-text><CompCadastrarRadius /></v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs-items>

      <!-- TERMINA -->
    </v-col>
    <v-col cols="12" sm="3">
      <CompCardPerfil />
    </v-col>
  </v-row>
</template>

<script>
import { mapState } from "vuex";
import CompCadastrarRadius from "../../../components/Admin/CompCadastrarRadius.vue";
import CompCardMenuEsquerdoAdmin from "~/components/Admin/CompCardMenuEsquerdoAdmin.vue";
import CompTabelaRadius from "~/components/Admin/CompTabelaRadius.vue";

export default {
  name: "AdminPage",
  components: {
    CompCardMenuEsquerdoAdmin,
    CompTabelaRadius,
    CompCadastrarRadius,
  },
  data() {
    return {
      tab: null,
    };
  },
  computed: {
    ...mapState("erp", ["erps"]),
    ...mapState("users", ["currentUser"]),
    ...mapState("alerts", ["sucesso", "error"]),
  },
  async mounted() {
    if (!this.currentUser.eh_admin) {
      await this.$store.dispatch(
        "alerts/setError",
        "Você não tem permissão, procure um administrador do sistema"
      );
      this.$router.push("/");
    }
    await this.$store.dispatch("erp/setRadius");
  },
  methods: {
    async successNull() {
      await this.$store.dispatch("alerts/setSuccess", null);
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

<template>
  <v-row v-if="currentUser">
    <v-col cols="12" sm="2">
      <CompCardImg />
      <CompCardMenuEsquerdoAdmin />
    </v-col>
    <v-col cols="12" sm="7">
      <CompEditarUsuario />
    </v-col>
    <v-col cols="12" sm="3">
      <CompCardPerfil />
    </v-col>
  </v-row>
</template>

<script>
import { mapState } from "vuex";
import CompEditarUsuario from "~/components/Admin/CompEditarUsuario.vue";
import CompCardMenuEsquerdoAdmin from "~/components/Admin/CompCardMenuEsquerdoAdmin.vue";
export default {
  components: { CompEditarUsuario, CompCardMenuEsquerdoAdmin },
  computed: {
    ...mapState("users", ["currentUser"]),
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

<template>
  <v-row>
    <v-col cols="12" sm="2">
      <CompCardImg />
      <CompCardMenuEsquerdo />
    </v-col>
    <v-col cols="12" sm="10">
      <v-row>
        <v-col cols="12" sm="8">
          <CompTextFilterSearchClientLog />
        </v-col>
        <v-col cols="12" sm="4">
          <CompCardPerfil />
        </v-col>
      </v-row>
      <v-row class="mt-0">
        <v-col cols="12" sm="12" class="pt-0">
          <v-card tile class="rounded-xl pa-1">
            <v-card-title class="text-h6 grey lighten-2">
              Logs do Radius
            </v-card-title>
            <v-list-item
              v-for="(value, name, index) in logs"
              :key="index"
              dense
            >
              <v-list-item-content>
                <v-list-item-subtitle
                  class="text-wrap"
                  v-html="value"
                ></v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-col>
      </v-row>
    </v-col>

    <!-- <v-col cols="12" sm="7">
      <CompTextFilterSearchClientLog />
    </v-col>
    <v-col cols="12" sm="3">
      <CompCardPerfil />
    </v-col> -->
  </v-row>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "LogPage",

  computed: {
    ...mapState("logs", ["logs"]),
  },
  async mounted() {
    await this.$store.dispatch("logs/setLogs");
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
.v-list-item--dense {
  min-height: 2px;
}
</style>

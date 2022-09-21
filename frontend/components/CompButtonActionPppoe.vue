<template>
  <v-dialog v-model="dialogDetalhesPppoe" width="555">
    <template #activator="{ on }">
      <v-btn
        class="ma-2 text-body-2 text-capitalize white--text"
        rounded
        :link="link"
        :color="cor"
        elevation="10"
        v-on="on"
        @click="get_extensive"
      >
        {{ titulo }}
        <v-icon right class="mb-1"> {{ icone }} </v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-title class="text-h6 grey lighten-2">
        Detalhes do PPPoE
      </v-card-title>

      <v-card-text>
        <pre class="text-caption">{{ extensivePppoe.extensive }}</pre>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="dialogDetalhesPppoe = false">
          Fechar
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    ip_olt: {
      type: String,
      default: "",
    },
    titulo: {
      type: String,
      default: "",
    },
    icone: {
      type: String,
      default: "",
    },
    cor: {
      type: String,
      default: "",
    },
    link: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      dialogDetalhesPppoe: false,
      extensivePppoe: {},
    };
  },
  async mounted() {},
  methods: {
    async get_extensive() {
      this.extensivePppoe = await this.$store.dispatch(
        "tests/getExtensivePppoe",
        { login: this.$route.params.login, ip_olt: this.ip_olt }
      );
    },
  },
};
</script>

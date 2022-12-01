<template>
  <v-hover v-slot="{ hover }">
    <v-card
      v-if="clientServico"
      class="rounded-xl pa-1"
      :elevation="hover ? 24 : 10"
    >
      <v-subheader class="font-weight-bold text-caption">
        {{ clientServico.instalacao_nome }}
      </v-subheader>

      <v-list three-line class="mt-n4">
        <v-list-item>
          <v-list-item-content>
            <v-list-item-subtitle
              v-html="
                ` <strong>Uptime:</strong>
                      ${$moment(clientServico.ultimo_acesso).fromNow()}`
              "
            >
            </v-list-item-subtitle>
            <v-list-item-subtitle
              v-html="'<strong>Download:</strong> ' + extraDown"
            >
            </v-list-item-subtitle>
            <v-list-item-subtitle
              v-html="'<strong>Upload:</strong> ' + extraUp"
            ></v-list-item-subtitle>
            <v-list-item-subtitle
              v-html="'<strong>Status:</strong> ' + clientServico.status"
            ></v-list-item-subtitle>
            <v-list-item-subtitle
              v-html="'<strong>Serial:</strong> ' + clientServico.serial"
            ></v-list-item-subtitle>
            <v-list-item-subtitle
              v-html="
                '<strong>perfil:</strong> ' + clientServico.perfil.toLowerCase()
              "
            ></v-list-item-subtitle>
            <v-list-item-subtitle
              v-html="'<strong>IPv4:</strong> ' + clientServico.ultimo_ip"
            ></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-card>
  </v-hover>
</template>
<script>
import { mapState } from "vuex";
export default {
  async asyncData({ store, route }) {
    await store.dispatch("apierp/setClientesServicos", route.params.login);
  },
  computed: {
    ...mapState("apierp", ["clientServico"]),
    extraDown() {
      let downInt = 0;
      const down = this.clientServico.servico_download;
      if (down.includes("K")) {
        downInt = parseInt(down.split("K")[0]);
      }
      return `${downInt / 1000}M`;
    },
    extraUp() {
      let upInt = 0;
      const up = this.clientServico.servico_upload;
      if (up.includes("K")) {
        upInt = parseInt(up.split("K")[0]);
      }
      return `${upInt / 1000}M`;
    },
  },
};
</script>

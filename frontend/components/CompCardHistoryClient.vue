<template>
  <v-hover>
    <template #default="{ hover }">
      <v-card class="rounded-xl" :elevation="hover ? 24 : 10">
        <v-toolbar flat>
          <v-toolbar-title> Historico Cliente </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-badge bordred bottom color="blue-grey" dot offset-x="10">
            <v-icon left color="black">fas fa-file-contract</v-icon>
          </v-badge>
          <div v-if="carregado">
            {{ historicoOS.meta.total }}
          </div>
        </v-toolbar>

        <v-list v-if="carregado" three-line class="mt-n4">
          <v-dialog v-model="dialogModalOrdemServico" width="500">
            <template #activator="{ on, attrs }">
              <v-list-item-group v-model="id">
                <v-list-item
                  v-for="(item, i) in historicoOS.dados"
                  :key="i"
                  v-bind="attrs"
                  v-on="on"
                  @click="getHistorico(item)"
                >
                  <v-list-item-content>
                    <v-list-item-title
                      v-html="item.tecnico"
                    ></v-list-item-title>
                    <v-list-item-subtitle
                      v-text="item.defeito"
                    ></v-list-item-subtitle>
                  </v-list-item-content>
                  <v-list-item-action>
                    <v-list-item-action-text
                      v-text="$moment(item.data + ' ' + item.hora).fromNow()"
                    ></v-list-item-action-text>
                  </v-list-item-action>
                </v-list-item>
              </v-list-item-group>
            </template>
            <v-card tile>
              <v-card-title class="text-h5 grey lighten-2">
                Ordem de Serviço
              </v-card-title>

              <v-list-item>
                <v-list-item-content>
                  <v-list-item-subtitle
                    v-html="`<strong>Cod:</strong> ${osFiltrada.id_cliente}`"
                  ></v-list-item-subtitle>
                  <v-list-item-subtitle
                    class="text-wrap"
                    v-html="`<strong>Defeito:</strong> ${osFiltrada.defeito}`"
                  ></v-list-item-subtitle
                  ><v-list-item-subtitle
                    v-html="`<strong>Plano:</strong> ${osFiltrada.plano}`"
                  ></v-list-item-subtitle
                  ><v-list-item-subtitle
                    v-html="
                      `<strong>Prioridade:</strong> ${osFiltrada.prioridade}`
                    "
                  ></v-list-item-subtitle
                  ><v-list-item-subtitle
                    v-html="`<strong>Endereco:</strong> ${osFiltrada.endereco}`"
                  ></v-list-item-subtitle
                  ><v-list-item-subtitle
                    v-html="`<strong>Numero:</strong> ${osFiltrada.numero}`"
                  ></v-list-item-subtitle>
                  <v-list-item-subtitle
                    v-html="`<strong>Bairro:</strong> ${osFiltrada.bairro}`"
                  ></v-list-item-subtitle>
                  <v-list-item-subtitle
                    v-html="`<strong>Cidade:</strong> ${osFiltrada.cidade}`"
                  ></v-list-item-subtitle>
                  <v-list-item-subtitle
                    v-html="`<strong>UF:</strong> ${osFiltrada.uf}`"
                  ></v-list-item-subtitle>
                  <v-list-item-subtitle
                    v-html="`<strong>Telefone:</strong> ${osFiltrada.telefone}`"
                  ></v-list-item-subtitle>
                  <v-list-item-subtitle
                    v-html="`<strong>Tecnico:</strong> ${osFiltrada.tecnico}`"
                  ></v-list-item-subtitle>
                  <v-list-item-subtitle
                    v-html="
                      `<strong>Categoria:</strong> ${osFiltrada.categoria}`
                    "
                  ></v-list-item-subtitle>
                  <v-list-item-subtitle
                    v-html="`<strong>Base:</strong> ${osFiltrada.base}`"
                  ></v-list-item-subtitle>
                  <v-list-item-subtitle
                    v-html="
                      `<strong>Statusconexao:</strong> ${osFiltrada.statusconexao}`
                    "
                  ></v-list-item-subtitle>
                  <v-list-item-subtitle
                    v-html="`<strong>operador:</strong> ${osFiltrada.operador}`"
                  ></v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>

              <v-divider></v-divider>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="primary"
                  text
                  @click="dialogModalOrdemServico = false"
                >
                  Fechar
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-list>

        <v-app-bar flat color="rgba(0,0,0,0)">
          <strong>Carregar Histórico</strong>
          <v-spacer></v-spacer>
          <v-btn
            class="mx-2"
            fab
            dark
            small
            color="indigo lighten-2"
            @click="getLoadHistory"
          >
            <v-icon dark> mdi-refresh </v-icon>
          </v-btn>
        </v-app-bar>
      </v-card>
    </template>
  </v-hover>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      osFiltrada: {},
      carregado: false,
      id: 0,
      dialogModalOrdemServico: false,
    };
  },
  computed: {
    ...mapState("apierp", ["clientServico", "historicoOS"]),
  },
  watch: {
    historicoOS() {
      this.carregado = true;
    },
  },

  async mounted() {},

  methods: {
    getHistorico(valor) {
      this.osFiltrada = valor;
    },
    async getLoadHistory() {
      await this.$store.dispatch(
        "apierp/setHistoricoOS",
        this.clientServico.id_cliente
      );
    },
  },
};
</script>

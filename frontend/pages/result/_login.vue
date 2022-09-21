<template>
  <v-row>
    <!-- MENU ESQUERDO -->
    <v-col cols="12" sm="2">
      <CompCardImg />
      <CompCardMenuEsquerdo />
      <CompCardInfo />
    </v-col>
    <!-- CONTEUDO CENTRAL -->
    <v-col cols="12" sm="7">
      <CompTextFilterSearchClient />

      <v-row>
        <CompCardItem
          titulo="TOTAL DISCADOS"
          icone="fas fa-network-wired"
          :valor="result.total_client"
          classe="text-caption
          indigo--text text--darken-4
          font-weight-bold"
          cor="#1a237e"
        />
        <CompCardItem
          :titulo="`TOTAL de clientes ${result.vlan}`"
          icone="fas fa-project-diagram"
          :valor="result.total_conn_vlan"
          classe="text-caption
          teal--text text--darken-4
          font-weight-bold"
          cor="#004D40"
        />

        <CompCardItem
          titulo="PLANO DO CLIENTE"
          icone="fas fa-clipboard-list"
          :valor="result.plano"
          classe="text-caption
          orange--text text--darken-4
          font-weight-bold"
          cor="#E65100"
        />
      </v-row>
      <v-row justify="space-between">
        <CompButtonAction
          :titulo="'Abrir Roteador'"
          :icone="'mdi-router-wireless'"
          :cor="'#1a237e'"
          :disable="result.porta_router > 0 ? false : true"
          :href="`http://${result.ip}:${result.porta_router}`"
        />
        <CompButtonAction
          :titulo="'Abrir ONU'"
          :icone="'mdi-router-network'"
          :cor="'#004D40'"
          :disable="result.porta_onu > 0 ? false : true"
          :href="`http://${result.ip}:${result.porta_onu}`"
        />

        <CompButtonActionPppoe
          :titulo="'Detalhes PPPoE'"
          :icone="'mdi-access-point-plus'"
          :cor="'#E65100'"
          :ip_olt="result.ip_olt"
        />

        <v-btn
          class="ma-2 text-body-2 text-capitalize white--text"
          rounded
          color="error"
          elevation="10"
          @click="desconectar"
        >
          {{ "Desconectar PPPoE" }}
          <v-icon right class="mb-1"> {{ "mdi-power-standby" }} </v-icon>
        </v-btn>
      </v-row>

      <v-row class="mx-auto">
        <v-col cols="12" md="6">
          <v-hover>
            <template #default="{ hover }">
              <v-card
                v-if="loaded"
                :elevation="hover ? 24 : 10"
                class="rounded-lg mt-3"
              >
                <CompLineChart
                  :height="250"
                  :chart-data="datacollectionIpv4"
                  :text="'Grafico IPv4'"
                />
                <v-card-subtitle class="pb-1">
                  Download:
                  <span class="font-weight-medium red--text text--darken-4">
                    {{ maior_down_ipv4() }}
                  </span>
                </v-card-subtitle>
                <v-card-subtitle class="pt-0">
                  Upload:
                  <span class="font-weight-medium green--text text--darken-4">
                    {{ maior_up_ipv4() }}
                  </span>
                </v-card-subtitle>
              </v-card>
            </template>
          </v-hover>
        </v-col>
        <v-col cols="12" md="6">
          <v-hover>
            <template #default="{ hover }">
              <v-card
                v-if="loaded"
                :elevation="hover ? 24 : 10"
                class="rounded-lg mt-3"
              >
                <CompLineChart
                  :height="250"
                  :chart-data="datacollectionIpv6"
                  :text="'Grafico IPv6'"
                />
                <v-card-subtitle class="pb-1">
                  Download:
                  <span class="font-weight-medium red--text text--darken-4">
                    {{ maior_down_ipv6() }}
                  </span>
                </v-card-subtitle>
                <v-card-subtitle class="pt-0">
                  Upload:
                  <span class="font-weight-medium green--text text--darken-4">
                    {{ maior_up_ipv6() }}
                  </span>
                </v-card-subtitle>
              </v-card>
            </template>
          </v-hover>
        </v-col>
        <!-- Grafico Total -->
        <v-col cols="12" md="12">
          <v-hover>
            <template #default="{ hover }">
              <v-card
                v-if="loaded"
                :elevation="hover ? 24 : 10"
                class="rounded-lg mt-3"
              >
                <CompLineChart
                  :height="150"
                  :chart-data="datacollectionTotal"
                  :text="'Grafico Total'"
                />
                <v-card-subtitle class="pb-1">
                  Download:
                  <span class="font-weight-medium red--text text--darken-4">
                    {{ maior_down_total() }}
                  </span>
                </v-card-subtitle>
                <v-card-subtitle class="pt-0">
                  Upload:
                  <span class="font-weight-medium green--text text--darken-4">
                    {{ maior_up_total() }}
                  </span>
                </v-card-subtitle>
              </v-card>
            </template>
          </v-hover>
        </v-col>
      </v-row>
    </v-col>
    <!-- MENU DIREITO -->
    <v-col cols="12" sm="3">
      <CompCardPerfil />
      <CompCardHistoryClient />
    </v-col>
  </v-row>
</template>

<script>
import CompLineChart from "~/components/CompLineChart.js";

export default {
  name: "ResultPage",
  components: { CompLineChart },

  async asyncData({ store, route, redirect }) {
    const clientServ = await store.dispatch(
      "apierp/setClientesServicos",
      route.params.login
    );
    const result = await store.dispatch("client/getResult", route.params.login);
    if (result.status === 404) {
      redirect("/");
    }
    return {
      clientServ,
      result,
    };
  },
  data() {
    return {
      intervalTraffic: () => {},
      traffic: [],
      downV4: 0,
      upV4: 0,
      downV6: 0,
      upV6: 0,
      downTotal: 0,
      upTotal: 0,
      loaded: false,
      labelIpv4: [],
      labelIpv6: [],
      labelTotal: [],
      arrayDownIpv4: [],
      arrayDownIpv6: [],
      arrayDownTotal: [],
      arrayUpIpv4: [],
      arrayUpIpv6: [],
      arrayUpTotal: [],
      datacollectionIpv4: null,
      datacollectionIpv6: null,
      datacollectionTotal: null,
    };
  },
  created() {},
  beforeDestroy() {
    clearInterval(this.intervalTraffic);
  },
  mounted() {
    this.loaded = false;
    this.intervalTraffic = setInterval(this.gettrafficInterval, 4000);
  },

  methods: {
    async gettrafficInterval() {
      this.traffic = await this.$store.dispatch("tests/getTraffic", {
        interface: this.result.interface,
        ip_olt: this.result.ip_olt,
      });
      this.getTraffic();
    },

    desconectar() {
      console.log("desconectar");
      // await this.$store.dispatch("tests/getDesconect", {
      //   login: this.result.login,
      //   ip_olt: this.result.ip_olt,
      // });
    },

    maior_down_ipv4() {
      const max = Math.max(...this.arrayDownIpv4);
      if (max > this.downV4) {
        this.downV4 = max;
      }
      return this.calculo(this.downV4, 10);
    },
    maior_down_ipv6() {
      const max = Math.max(...this.arrayDownIpv6);
      if (max > this.downV6) {
        this.downV6 = max;
      }
      return this.calculo(this.downV6, 10);
    },
    maior_down_total() {
      const max = Math.max(...this.arrayDownTotal);
      if (max > this.downTotal) {
        this.downTotal = max;
      }
      return this.calculo(this.downTotal, 10);
    },
    maior_up_ipv4() {
      const max = Math.max(...this.arrayUpIpv4);
      if (max > this.upV4) {
        this.upV4 = max;
      }
      return this.calculo(this.upV4, 10);
    },
    maior_up_ipv6() {
      const max = Math.max(...this.arrayUpIpv6);
      if (max > this.upV6) {
        this.upV6 = max;
      }
      return this.calculo(this.upV6, 10);
    },
    maior_up_total() {
      const max = Math.max(...this.arrayUpTotal);
      if (max > this.upTotal) {
        this.upTotal = max;
      }
      return this.calculo(this.upTotal, 10);
    },

    calculo(trafego) {
      const size = ["b", "kbps", "mbps"];
      if (trafego === 0) {
        return "0 b";
      }
      const i = parseInt(Math.floor(Math.log(trafego) / Math.log(1024)), 10);
      return (trafego / Math.pow(1024, i)).toFixed(2) + " " + size[i];
    },
    getTraffic() {
      const d = new Date();
      if (this.arrayDownIpv4.length <= 5) {
        this.arrayDownIpv4.push(this.traffic.DOWN_IPv4);
        this.arrayDownIpv6.push(this.traffic.DOWN_IPv6);
        this.arrayDownTotal.push(this.traffic.DOWN_TOTAL);
        this.arrayUpIpv4.push(this.traffic.UP_IPv4);
        this.arrayUpIpv6.push(this.traffic.UP_IPv6);
        this.arrayUpTotal.push(this.traffic.UP_TOTAL);
        this.labelIpv4.push(d.toLocaleTimeString());
        this.labelIpv6.push(d.toLocaleTimeString());
        this.labelTotal.push(d.toLocaleTimeString());
        this.loaded = true;
      } else {
        this.arrayDownIpv4.push(this.traffic.DOWN_IPv4);
        this.arrayDownIpv4.shift();
        this.arrayDownIpv6.push(this.traffic.DOWN_IPv6);
        this.arrayDownIpv6.shift();
        this.arrayDownTotal.push(this.traffic.DOWN_TOTAL);
        this.arrayDownTotal.shift();
        this.arrayUpIpv4.push(this.traffic.UP_IPv4);
        this.arrayUpIpv4.shift();
        this.arrayUpIpv6.push(this.traffic.UP_IPv6);
        this.arrayUpIpv6.shift();
        this.arrayUpTotal.push(this.traffic.UP_TOTAL);
        this.arrayUpTotal.shift();
        this.labelIpv4.push(d.toLocaleTimeString());
        this.labelIpv4.shift();
        this.labelIpv6.push(d.toLocaleTimeString());
        this.labelIpv6.shift();
        this.labelTotal.push(d.toLocaleTimeString());
        this.labelTotal.shift();
      }

      this.datacollectionIpv4 = {
        labels: this.labelIpv4,
        datasets: [
          {
            label: "Download",
            fillColor: "rgba(255, 0, 0, 0.2)",
            backgroundColor: "rgba(255, 0, 0, 0.2)",
            strokeColor: "rgba(255, 0, 0, 0.2)",
            pointColor: "rgba(255, 0, 0, 0.2)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(255, 0, 0, 0.2)",
            data: this.arrayDownIpv4,
          },
          {
            label: "Upload",
            fillColor: "rgba(63,191,63,0.2)",
            backgroundColor: "rgba(63,191,63,0.2)",
            strokeColor: "rgba(63,191,63,0.2)",
            pointColor: "rgba(63,191,63,0.2)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(63,191,63,0.2)",
            data: this.arrayUpIpv4,
          },
        ],
      };

      this.datacollectionIpv6 = {
        labels: this.labelIpv6,
        datasets: [
          {
            label: "Download",
            fillColor: "rgba(255, 0, 0, 0.2)",
            backgroundColor: "rgba(255, 0, 0, 0.2)",
            strokeColor: "rgba(255, 0, 0, 0.2)",
            pointColor: "rgba(255, 0, 0, 0.2)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(255, 0, 0, 0.2)",
            data: this.arrayDownIpv6,
          },
          {
            label: "Upload",
            fillColor: "rgba(63,191,63,0.2)",
            backgroundColor: "rgba(63,191,63,0.2)",
            strokeColor: "rgba(63,191,63,0.2)",
            pointColor: "rgba(63,191,63,0.2)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(63,191,63,0.2)",
            data: this.arrayUpIpv6,
          },
        ],
      };

      this.datacollectionTotal = {
        labels: this.labelTotal,
        datasets: [
          {
            label: "Download",
            fillColor: "rgba(255, 0, 0, 0.2)",
            backgroundColor: "rgba(255, 0, 0, 0.2)",
            strokeColor: "rgba(255, 0, 0, 0.2)",
            pointColor: "rgba(255, 0, 0, 0.2)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(255, 0, 0, 0.2)",
            data: this.arrayDownTotal,
          },
          {
            label: "Upload",
            fillColor: "rgba(63,191,63,0.2)",
            backgroundColor: "rgba(63,191,63,0.2)",
            strokeColor: "rgba(63,191,63,0.2)",
            pointColor: "rgba(63,191,63,0.2)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(63,191,63,0.2)",
            data: this.arrayUpTotal,
          },
        ],
      };
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

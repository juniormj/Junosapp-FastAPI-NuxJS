<template>
  <v-hover v-if="currentUser" v-slot="{ hover }">
    <v-card class="rounded-xl mb-2" :elevation="hover ? 24 : 10">
      <v-list>
        <v-subheader inset class="font-weight-bold"> MENU LATERAL </v-subheader>
        <v-list-item-group color="primary">
          <v-list-item
            v-for="(item, i) in items_client"
            :key="i"
            :to="item.link"
            class="ma-1"
          >
            <v-list-item-icon class="mr-2">
              <v-icon v-text="item.icon" />
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-html="item.text" />
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
        <v-subheader class="font-weight-bold text-caption">
          CONECTIVIDADE
        </v-subheader>
        <v-list-item-group color="primary">
          <v-list-item
            v-for="(item, i) in items_conectividade"
            :key="i"
            :to="item.link"
            class="ma-1"
          >
            <v-list-item-icon class="mr-2">
              <v-icon v-text="item.icon" />
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-html="item.text" />
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
        <v-divider />
        <v-list-item-group color="primary">
          <v-list-item
            v-for="(item, i) in items_log"
            :key="i"
            :to="item.link"
            class="ma-1"
          >
            <v-list-item-icon class="mr-2">
              <v-icon v-text="item.icon" />
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-html="item.text" />
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-card>
  </v-hover>
</template>

<script>
import { mapState } from "vuex";
export default {
  data: () => ({
    items_client: [{ text: "Home", icon: "mdi-home", link: "/" }],
    items_conectividade: [
      {
        text: "Teste PPPoE",
        icon: "mdi-access-point-check",
        link: "/getpppoe",
      },
      { text: "Teste Ping", icon: "mdi-connection", link: "/getping" },
    ],
    items_log: [
      { text: "Logs Radius", icon: "mdi-text-box-multiple", link: "/log" },
    ],
  }),
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

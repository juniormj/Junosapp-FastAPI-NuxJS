<template>
  <v-hover v-if="currentUser" v-slot="{ hover }">
    <v-card
      class="mb-2 pa-1 borderRight"
      color="#284177"
      :elevation="hover ? 24 : 10"
    >
      <v-toolbar color="#284177" dark flat>
        <v-avatar class="ml-8 mr-2 border" size="35">
          <img src="/bot.jpeg" alt="alt" />
        </v-avatar>
        <v-toolbar-title class="title white--text pl-0 mr-3">
          {{ currentUser.nome + " " + currentUser.sobrenome }}
        </v-toolbar-title>
        <v-menu bottom left transition="expand-x-transition" offset-y>
          <template #activator="{ on, attrs }">
            <v-btn icon v-bind="attrs" plain v-on="on">
              <v-icon small>fas fa-chevron-down</v-icon>
            </v-btn>
          </template>
          <v-list flat>
            <v-list-item-group v-model="itemSelecionado" color="#284177">
              <v-list-item nuxt to="/admin">
                <v-list-item-icon>
                  <v-icon>mdi-shield-account</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title class="text-subtitle-1">
                    Painel Admin
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
            <v-divider></v-divider>
            <v-list-item-group v-model="itemSelecionado" color="#284177">
              <v-list-item>
                <v-list-item-icon>
                  <v-icon>mdi-account-edit</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title class="text-subtitle-1">
                    Alterar Perfil
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
            <v-divider></v-divider>
            <v-list-item-group v-model="itemSelecionado" color="#284177">
              <v-list-item @click.prevent="userLogout">
                <v-list-item-icon>
                  <v-icon>mdi-power</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title class="text-subtitle-1">
                    Logoff
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-menu>
      </v-toolbar>
    </v-card>
  </v-hover>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      itemSelecionado: 1,
    };
  },
  computed: {
    ...mapState("users", ["currentUser"]),
  },
  methods: {
    userLogout() {
      localStorage.removeItem("token");
      this.$store.dispatch("users/setNullUser", {});
      this.$router.push("/login");
    },
  },
};
</script>

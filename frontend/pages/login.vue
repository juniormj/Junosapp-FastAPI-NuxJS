<template>
  <v-app>
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-alert
              v-if="alerts.error"
              class="mb-8"
              type="error"
              elevation="4"
              dismissible
              outlined
              @click="errorNull"
            >
              {{ alerts.error }}
            </v-alert>
            <v-card class="elevation-12" color="transparent">
              <v-toolbar dark color="#284177">
                <v-toolbar-title>Formulário Login</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <form @submit.prevent="logIn">
                  <v-text-field
                    v-model="login.username"
                    name="username"
                    label="Email"
                    type="text"
                    placeholder="email"
                    prepend-icon="mdi-account-circle"
                    required
                  ></v-text-field>

                  <v-text-field
                    v-model="login.password"
                    name="password"
                    label="Senha"
                    placeholder="senha"
                    prepend-icon="mdi-lock"
                    :append-icon="show_password ? 'mdi-eye' : 'mdi-eye-off'"
                    :type="show_password ? 'text' : 'password'"
                    required
                    @click:append="show_password = !show_password"
                  ></v-text-field>
                  <v-btn
                    type="submit"
                    class="mt-4 white--text"
                    color="#284177"
                    value="log in"
                  >
                    Enviar
                  </v-btn>
                </form>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "PageLogin",

  data() {
    return {
      show_password: false,
      login: {
        username: "",
        password: "",
      },
    };
  },
  computed: {
    ...mapState(["users", "alerts"]),
  },
  methods: {
    async logIn() {
      const User = new FormData();
      User.append("username", this.login.username);
      User.append("password", this.login.password);
      const test = await this.$store.dispatch("users/setLogin", User);

      if (Object.keys(test).length === 2) {
        this.$router.push("/");
      }
    },
    async errorNull() {
      await this.$store.dispatch("alerts/setError", null);
    },
  },
};
</script>

<style  scoped>
</style>

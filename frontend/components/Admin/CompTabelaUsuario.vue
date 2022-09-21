<template>
  <v-card v-if="users.users" class="mb-2 pa-1 borderLeft" color="#284177">
    <v-card-title>
      <v-text-field
        v-model="search"
        dark
        append-icon="mdi-magnify"
        label="Localizar usuário"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-dialog v-model="dialog" max-width="350">
      <v-card>
        <v-card-title class="text-h5"> Deseja realmente remover? </v-card-title>

        <v-card-text>
          Atenção, se confirmar a remoção, esse usuário será removio também do
          banco de dados.
        </v-card-text>
        <v-card-text> Deseja continuar? </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="red darken-4" text @click="handleClickRemUser">
            SIM
          </v-btn>

          <v-btn color="grey darken-3" text @click="dialog = false">
            NÃO
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-data-table
      :headers="tab_users"
      :items="users.users"
      :search="search"
      :footer-props="{
        'items-per-page-text': 'Linhas por página:',
        'page-text': '{0}-{1} de {2}',
      }"
    >
      <template #[`item.action`]="{ item }">
        <v-btn icon color="gray" @click="handleClickEditUser(item.id)">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
        <v-btn icon color="red lighten-1" @click="updateIdUsuario(item.id)">
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      dialog: false,
      id_user: 0,
      search: "",
      tab_users: [
        { text: "Nome", value: "nome" },
        { text: "Sobre Nome", filterable: false, value: "sobrenome" },
        { text: "Email", filterable: false, value: "email" },
        { text: "Admin", filterable: false, value: "eh_admin" },
        { text: "Ação", align: "center", value: "action" },
      ],
    };
  },
  computed: {
    ...mapState(["users"]),
  },
  methods: {
    handleClickEditUser(idUser) {
      this.$router.replace(`/admin/edit/${idUser}`);
    },
    updateIdUsuario(idUser) {
      this.dialog = true;
      this.id_user = idUser;
    },
    async handleClickRemUser() {
      this.dialog = false;
      await this.$store.dispatch("users/deleteUser", this.id_user);
    },
  },
};
</script>

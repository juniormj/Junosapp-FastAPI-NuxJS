<template>
  <v-card v-if="erp.erps" class="mb-2 pa-1 borderLeft" color="#284177">
    <v-card-title>
      <v-text-field
        v-model="search"
        dark
        append-icon="mdi-magnify"
        label="Localizar ERP"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-dialog v-model="dialog" max-width="350">
      <v-card>
        <v-card-title class="text-h5"> Deseja realmente remover? </v-card-title>

        <v-card-text>
          Atenção, se confirmar a remoção, esse dispositivo será removio também
          do banco de dados.
        </v-card-text>
        <v-card-text> Deseja continuar? </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="red darken-4" text @click="handleClickRemERP">
            SIM
          </v-btn>

          <v-btn color="grey darken-3" text @click="dialog = false">
            NÃO
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-data-table
      :headers="tab_erp"
      :items="erp.erps"
      :search="search"
      :footer-props="{
        'items-per-page-text': 'Linhas por página:',
        'page-text': '{0}-{1} de {2}',
      }"
    >
      <template #[`item.action`]="{ item }">
        <v-btn icon color="gray" @click="handleClickEditErp(item.id)">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
        <v-btn icon color="red lighten-1" @click="updateIdErp(item.id)">
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
      id_erp: 0,
      search: "",
      tab_erp: [
        { text: "IP", value: "ip" },
        { text: "Login", value: "login" },
        { text: "Senha", filterable: false, value: "senha" },
        { text: "Identificação", value: "identificador" },
        { text: "vendor", value: "vendor" },
        { text: "Ação", align: "center", value: "action" },
      ],
    };
  },
  computed: {
    ...mapState(["erp"]),
  },
  methods: {
    handleClickEditErp(idErp) {
      this.$router.replace(`/admin/radius/edit/${idErp}`);
    },
    updateIdErp(idErp) {
      this.dialog = true;
      this.id_erp = idErp;
    },
    async handleClickRemERP() {
      this.dialog = false;
      await this.$store.dispatch("erp/deleteErp", this.id_erp);
    },
  },
};
</script>

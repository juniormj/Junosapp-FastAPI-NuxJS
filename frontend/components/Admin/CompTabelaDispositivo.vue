<template>
  <v-card v-if="devices.bras" class="mb-2 pa-1 borderLeft" color="#284177">
    <v-card-title>
      <v-text-field
        v-model="search"
        dark
        append-icon="mdi-magnify"
        label="Localizar Dispositivo"
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

          <v-btn color="red darken-4" text @click="handleClickRemDispositivo">
            SIM
          </v-btn>

          <v-btn color="grey darken-3" text @click="dialog = false">
            NÃO
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-data-table
      :headers="tab_bras"
      :items="devices.bras"
      :search="search"
      :footer-props="{
        'items-per-page-text': 'Linhas por página:',
        'page-text': '{0}-{1} de {2}',
      }"
    >
      <template #[`item.action`]="{ item }">
        <v-btn icon color="gray" @click="handleClickEditDevice(item.id)">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
        <v-btn icon color="red lighten-1" @click="updateIdDevice(item.id)">
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
      id_bras: 0,
      search: "",
      tab_bras: [
        { text: "Local", value: "local" },
        { text: "IP", value: "ip" },
        { text: "Login", filterable: false, value: "login" },
        { text: "Senha", filterable: false, value: "senha" },
        { text: "Ação", align: "center", value: "action" },
      ],
    };
  },
  computed: {
    ...mapState(["devices"]),
  },
  methods: {
    handleClickEditDevice(idDevice) {
      this.$router.replace(`/admin/dispositivo/edit/${idDevice}`);
    },
    updateIdDevice(idDevice) {
      this.dialog = true;
      this.id_bras = idDevice;
    },
    async handleClickRemDispositivo() {
      this.dialog = false;
      await this.$store.dispatch("devices/deleteDevice", this.id_bras);
    },
  },
};
</script>

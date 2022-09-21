<template>
  <v-col>
    <v-hover>
      <template #default="{ hover }">
        <v-card
          :elevation="hover ? 24 : 10"
          class="rounded-lg mx-1"
          :style="{ 'border-left': '5px solid' + cor }"
        >
          <v-list-item three-line>
            <v-list-item-content>
              <div :class="classe">
                {{ titulo }}
              </div>
              <v-list-item-title class="text-h6">
                {{ valor }}
              </v-list-item-title>
            </v-list-item-content>
            <v-icon>{{ icone }}</v-icon>
          </v-list-item>
        </v-card>
      </template>
    </v-hover>
  </v-col>
</template>

<script>
export default {
  props: {
    titulo: {
      type: String,
      default: "",
    },
    icone: {
      type: String,
      default: "",
    },
    valor: {
      type: String,
      default: "",
    },
    classe: {
      type: String,
      default: "",
    },
    cor: {
      type: String,
      default: "",
    },
  },
};
</script>

<style scoped>
/* .v-card.v-sheet.theme--light {
  border-left: 5px solid red !important;
} */
</style>

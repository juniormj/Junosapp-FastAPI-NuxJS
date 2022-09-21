<template>
  <v-btn
    class="ma-2 text-body-2 text-capitalize white--text"
    rounded
    :color="cor"
    target="_blank"
    :disabled="disable"
    :href="href"
    elevation="10"
  >
    {{ titulo }}
    <v-icon right class="mb-1"> {{ icone }} </v-icon>
  </v-btn>
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
    cor: {
      type: String,
      default: "",
    },
    href: {
      type: String,
      default: "",
    },
    disable: {
      type: Boolean,
      default: true,
    },
  },
};
</script>

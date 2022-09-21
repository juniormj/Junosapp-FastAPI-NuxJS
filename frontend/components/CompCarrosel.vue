<template>
  <v-carousel v-if="currentUser" hide-delimiters>
    <v-carousel-item
      v-for="(item, i) in items"
      :key="i"
      :src="item.src"
      contain
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      items: [
        {
          src: require("../assets/planfleto.png"),
        },
      ],
    };
  },
  computed: {
    ...mapState("users", ["currentUser"]),
  },
};
</script>

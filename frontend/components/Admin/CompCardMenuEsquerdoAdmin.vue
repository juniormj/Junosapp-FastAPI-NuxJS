<template>
  <v-hover v-slot="{ hover }">
    <v-card class="rounded-xl mb-2" :elevation="hover ? 24 : 10">
      <v-list flat>
        <v-subheader class="font-weight-bold"> PAINEL ADMIN </v-subheader>
        <v-list-item-group v-model="value" color="#284177">
          <v-list-item
            v-for="(item, i) in items_client"
            :key="i"
            nuxt
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
        <v-list-item-group color="#284177">
          <v-list-item to="/" class="ma-1">
            <v-list-item-icon class="mr-2">
              <v-icon>mdi-home-variant</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-card>
  </v-hover>
</template>

<script>
export default {
  data: () => ({
    value: 1,
    items_client: [
      { text: "Usuário", icon: "mdi-account-plus", link: "/admin" },
      {
        text: "Dispositivo",
        icon: "mdi-router-network",
        link: "/admin/dispositivo",
      },
      {
        text: "Radius",
        icon: "mdi-server-network",
        link: "/admin/radius",
      },
    ],
  }),
};
</script>

<template>
  <div></div>
</template>
<script>
export default {
  name: "IndexPageResult",
  created() {
    if (Object.keys(this.$route.params).length === 0) {
      this.$router.push("/");
    }
  },
};
</script>

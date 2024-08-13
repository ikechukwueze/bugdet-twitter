<template>
  <ThreeColumnLayout>
    <template #left-sidebar>
      <MenuVue />
    </template>
    <template #main>
      <HomeTimeLine />
    </template>
    <template #right-sidebar>
      <TrendList />
    </template>
  </ThreeColumnLayout>
</template>



<script>
import ThreeColumnLayout from "@/layouts/ThreeColumnLayout.vue"
import MenuVue from "@/components/Menu.vue";
import HomeTimeLine from "@/components/HomeTimeLine.vue";
import TrendList from "@/components/TrendList.vue";

export default {
  name: "HomeVue",
  components: {
    ThreeColumnLayout,
    MenuVue,
    HomeTimeLine,
    TrendList
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
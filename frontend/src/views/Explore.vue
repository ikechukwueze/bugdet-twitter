<template>
  <ThreeColumnLayout>
    <template #left-sidebar>
      <MenuVue />
    </template>
    <template #main>
      <TrendList :limit=10 />
    </template>
    <template #right-sidebar>
    </template>
  </ThreeColumnLayout>
</template>



<script>
import ThreeColumnLayout from "@/layouts/ThreeColumnLayout.vue"
import MenuVue from "@/components/Menu.vue";
import TrendList from "@/components/TrendList.vue";


export default {
  name: "ExploreVue",
  components: {
    ThreeColumnLayout,
    MenuVue,
    TrendList
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
<template>
  <ThreeColumnLayout>
    <template #left-sidebar>
      <MenuVue />
    </template>
    <template #main>
      <SearchBar :placeholder="$route.params.search_query" />
      <SearchResults :search_query="$route.params.search_query" />
    </template>
    <template #right-sidebar>
      <TrendList />
    </template>
  </ThreeColumnLayout>
</template>



<script>
import ThreeColumnLayout from "@/layouts/ThreeColumnLayout.vue"
import MenuVue from "@/components/Menu.vue";
import SearchBar from "@/components/SearchBar.vue";
import SearchResults from "@/components/SearchResults.vue";
import TrendList from "@/components/TrendList.vue";

export default {
  name: "ThreadVue",
  components: {
    ThreeColumnLayout,
    MenuVue,
    SearchBar,
    SearchResults,
    TrendList
  },
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
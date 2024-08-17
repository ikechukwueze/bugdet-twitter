<template>
  <ThreeColumnLayout>
    <template #left-sidebar>
      <MenuVue />
    </template>
    <template #main>
      <SearchBar :placeholder="$route.params.trend_term" />
      <TrendTweets :trend_term="$route.params.trend_term" />
    </template>
    <template #right-sidebar>
      <TrendList />
    </template>
  </ThreeColumnLayout>
</template>



<script>
import ThreeColumnLayout from "@/layouts/ThreeColumnLayout.vue"
import MenuVue from "@/components/Menu.vue";
import TrendTweets from "@/components/TrendTweets.vue";
import SearchBar from "@/components/SearchBar.vue";
import TrendList from "@/components/TrendList.vue";


export default {
  name: "ThreadVue",
  components: {
    ThreeColumnLayout,
    MenuVue,
    SearchBar,
    TrendTweets,
    TrendList
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
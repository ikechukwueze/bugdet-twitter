<template>
  <ThreeColumnLayout>
    <template #left-sidebar>
      <MenuVue />
    </template>
    <template #main>
      <TweetThread :tweet_id="$route.params.tweet_id"/>
    </template>
    <template #right-sidebar>
      <TrendList />
    </template>
  </ThreeColumnLayout>
</template>



<script>
import ThreeColumnLayout from "@/layouts/ThreeColumnLayout.vue"
import MenuVue from "@/components/Menu.vue";
import TweetThread from "@/components/TweetThread.vue";
import TrendList from "@/components/TrendList.vue";


export default {
  name: "ThreadVue",
  components: {
    ThreeColumnLayout,
    MenuVue,
    TweetThread,
    TrendList
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
<template>
  <ThreeColumnLayout>
    <template #left-sidebar>
      <MenuVue />
    </template>
    <template #main>
      <UserFollowingVue :username="$route.params.username"/>
    </template>
    <template #right-sidebar>
      <TrendList />
    </template>
  </ThreeColumnLayout>
</template>



<script>
import ThreeColumnLayout from "@/layouts/ThreeColumnLayout.vue"
import MenuVue from "@/components/Menu.vue";
import UserFollowingVue from "@/components/UserFollowing.vue";
import TrendList from "@/components/TrendList.vue";

export default {
  name: "FollowersVue",
  components: {
    ThreeColumnLayout,
    MenuVue,
    UserFollowingVue,
    TrendList
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
<template>
  <ThreeColumnLayout>
    <template #left-sidebar>
      <MenuVue />
    </template>
    <template #main>
      <UserProfileVue :username="$route.params.username"/>
    </template>
    <template #right-sidebar>
      <TrendList />
    </template>
  </ThreeColumnLayout>
</template>



<script>
import ThreeColumnLayout from "@/layouts/ThreeColumnLayout.vue"
import MenuVue from "@/components/Menu.vue";
import UserProfileVue from "@/components/UserProfile.vue"
import TrendList from "@/components/TrendList.vue";


export default {
  name: "ProfileVue",
  components: {
    ThreeColumnLayout,
    MenuVue,
    UserProfileVue,
    TrendList
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
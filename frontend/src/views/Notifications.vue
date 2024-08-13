<template>
  <ThreeColumnLayout>
    <template #left-sidebar>
      <MenuVue />
    </template>
    <template #main>
      <UserNotificationVue />
    </template>
    <template #right-sidebar>
      <TrendList />
    </template>
  </ThreeColumnLayout>
</template>



<script>
import ThreeColumnLayout from "@/layouts/ThreeColumnLayout.vue"
import MenuVue from "@/components/Menu.vue";
import UserNotificationVue from "@/components/UserNotification.vue";
import TrendList from "@/components/TrendList.vue";

export default {
  name: "NotificationVue",
  components: {
    ThreeColumnLayout,
    MenuVue,
    UserNotificationVue,
    TrendList
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
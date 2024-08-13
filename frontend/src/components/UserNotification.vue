<template>
  <div class="col-9 mt-4 w-100 text-start">
    <nav>
      <div class="nav nav-pills nav-fill" id="nav-tab" role="tablist">
        <button class="nav-link active" id="nav-home-tab" data-bs-toggle="tab" data-bs-target="#nav-home" type="button"
          role="tab" aria-controls="nav-home" aria-selected="true">New</button>
        <button class="nav-link" id="nav-profile-tab" data-bs-toggle="tab" data-bs-target="#nav-profile" type="button"
          role="tab" aria-controls="nav-profile" aria-selected="false">Older</button>
      </div>
    </nav>
    <div class="tab-content px-3" id="nav-tabContent">
      <div class="tab-pane fade show active" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab" tabindex="0">
        <NotificationCard v-for="(notification_item, key) in current_notifications" :key="key" :notification="notification_item"/>
      </div>
      <div class="tab-pane fade show" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab" tabindex="0">
        <NotificationCard v-for="(notification_item, key) in all_notifications" :key="key" :notification="notification_item"/>
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NotificationCard from "./NotificationCard.vue";


export default {
  name: "UserNotificationVue",
  components: {
    NotificationCard,
  },
  props: {
    username: String
  },
  data() {
    return {
      current_notifications: [],
      all_notifications: []
    };
  },
  methods: {
    get_current_notifications() {
      axios({
        method: "get",
        url: '/notifications/current/',
      })
        .then((response) => {
          this.current_notifications = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    get_all_notifications() {
      axios({
        method: "get",
        url: '/notifications/',
      })
        .then((response) => {
          this.all_notifications = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    mark_notification_as_read(notification_id) {
      axios({
        method: "put",
        url: `/notifications/${notification_id}/mark-as-read/`,
      })
        .catch((error) => {
          console.log(error);
        });
    },




  },
  created() {
    this.get_current_notifications()
    this.get_all_notifications()
  },

};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>

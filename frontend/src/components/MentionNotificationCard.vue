<template>
  <div class="row">
    <div class="d-flex p-3 my-2 border rounded-3">
      <div class="flex-shrink-0">
        <img class="rounded-circle profile-pic" :src="notification.sender.profile_pic" />
      </div>
      <div class="card ms-1 w-100 border-0">
        <div class="card-header border-0 bg-white">
          <div class="d-flex justify-content-between">
            <div>
              <span class="fw-bold">
                {{ notification.sender.display_name }} <i class="bi bi-patch-check-fill"></i></span>
            </div>
            <div>
              <span>
                <i class="bi bi-at"></i>
              </span>
            </div>
          </div>
        </div>
        <div class="card-body py-1">
          <p>@{{ notification.sender.username }} mentioned you in a tweet.</p>
          <p class="card-text text-muted fst-italic">{{ notification.sender_tweet.content }}</p>
        </div>
        <div class="card-footer text-muted d-flex justify-content-around border-0 bg-white">
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "MentionNotificationCard",
  components: {
  },
  props: {
    notification: {}
  },
  data() {
    return {
    }
  }
}

</script>

<style scoped>
.bi-patch-check-fill {
  color: blue;
  font-size: 1rem;
}

.profile-pic {
  width: 30px;
  height: 30px;
  border-radius: 50%;
}
</style>

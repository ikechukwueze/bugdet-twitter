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
                <i :class="notification_type_icon[notification.notification_type]"></i>
              </span>
            </div>
          </div>
        </div>
        <div class="card-body py-1">
          <p>@{{ notification.sender.username }} {{ notification_type_dict[notification.notification_type] }} your post
          </p>
          <p class="card-text text-muted fst-italic">{{ notification.tweet.content }}</p>
        </div>
        <div class="card-footer text-muted d-flex justify-content-around border-0 bg-white">
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "NotificationCard",
  components: {
  },
  props: {
    notification: {
      sender: {},
      recipient: {},
      notification_type: String,
      tweet: {}
    }
  },
  data() {
    return {
      notification_type_dict: {
        'LIKE': 'liked',
        'DISLIKE': 'disliked',
        'RETWEET': 'reposted',
        'QUOTE': 'quoted',
        'REPLY': 'replied to'
      },
      notification_type_icon: {
        'LIKE': 'bi bi-patch-check-fill text-primary text-bold',
        'DISLIKE': 'bi bi-hand-thumbs-down-fill text-primary text-bold',
        'RETWEET': 'bi bi-repeat text-primary text-bold',
        'QUOTE': 'bi bi-chat-quote-fill text-primary text-bold',
        'REPLY': 'bi bi-chat text-bold'
      }
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

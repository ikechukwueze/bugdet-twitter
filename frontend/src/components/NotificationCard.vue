<template>
  <div class="row">
    <div class="d-flex p-3 my-2 border rounded-3">
      <div class="flex-shrink-0">
        <ProfilePic :profile_pic_url="notification.sender.profile_pic" :username="notification.sender.username" />
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
          <p>@{{ notification.sender.username }} {{ notification_message_dict[notification.notification_type] }}
          </p>
          <p class="card-text text-muted fst-italic">{{ notification.recipient_tweet.content }}</p>
        </div>
        <div class="card-footer text-muted d-flex justify-content-around border-0 bg-white">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProfilePic from './ProfilePic.vue';


export default {
  name: "NotificationCard",
  components: {
    ProfilePic
  },
  props: {
    notification: {}
  },
  data() {
    return {
      notification_message_dict: {
        'LIKE': 'liked your tweet.',
        'DISLIKE': 'disliked your tweet',
        'RETWEET': 'reposted your tweet.',
        'QUOTE': 'quoted your tweet',
        'FOLLOW': 'followed you.'
      },
      notification_type_icon: {
        'LIKE': 'bi bi-heart-fill text-primary text-bold',
        'DISLIKE': 'bi bi-hand-thumbs-down-fill text-primary text-bold',
        'RETWEET': 'bi bi-repeat text-primary text-bold',
        'QUOTE': 'bi bi-chat-quote-fill text-primary text-bold',
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

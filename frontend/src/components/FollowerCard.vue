<template>
  <div class="row">
    <div class="d-flex p-3 my-2 border rounded-3">
      <div class="flex-shrink-0">
        <ProfilePic :profile_pic_url="follower.profile_pic" :username="follower.username" />
      </div>
      <div class="card ms-1 w-100 border-0">
        <div class="card-header border-0 bg-white">
          <div class="d-flex justify-content-between">
            <div>
              <span class="fw-bold">
                {{ follower.display_name }} <i class="bi bi-patch-check-fill"></i></span>
              <span> &#183; </span>
              <span class="text-muted"> @{{ follower.username }} </span>
            </div>
            <div>
              <span>
                <template v-if="follows_user">
                  <button class="btn btn-sm btn-primary" @click="unfollow">Following</button>
                </template>
                <template v-else>
                  <button class="btn btn-sm btn-primary" @click="follow">Follow back</button>
                </template>
              </span>
            </div>
          </div>
        </div>
        <div class="card-body py-1">
          <p class="card-text">{{ follower.bio }}</p>
        </div>
        <div class="card-footer text-muted d-flex justify-content-around border-0 bg-white">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ProfilePic from './ProfilePic.vue';

export default {
  name: "FollowerCard",
  components: {
    ProfilePic
  },
  props: {
    follower: {
      username: String,
      display_name: String,
      profile_pic: String,
      bio: String,
    },
    is_following: Boolean
  },
  data() {
    return {
      follows_user: false
    };
  },

  methods: {
    follow() {
      axios({
        method: "post",
        url: `/followers/${this.follower.username}/follow/`,
      })
        .then(() => {
          this.follows_user = true
        })
        .catch((error) => {
          console.log(error);
        });
    },
    unfollow() {
      axios({
        method: "post",
        url: `/followers/${this.follower.username}/unfollow/`,
      })
        .then(() => {
          this.follows_user = false
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  created() {
    this.follows_user = this.is_following
  },
};
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

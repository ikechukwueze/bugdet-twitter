<template>
  <div class="col-9 mt-4 w-100 text-start">
    <nav>
      <div class="nav nav-pills nav-fill" id="nav-tab" role="tablist">
        <button class="nav-link active" id="nav-home-tab" data-bs-toggle="tab" data-bs-target="#nav-home" type="button"
          role="tab" aria-controls="nav-home" aria-selected="true">Followers</button>
        <button class="nav-link" id="nav-profile-tab" data-bs-toggle="tab" data-bs-target="#nav-profile" type="button"
          role="tab" aria-controls="nav-profile" aria-selected="false">Following</button>
      </div>
    </nav>
    <div class="tab-content px-3" id="nav-tabContent">
      <div class="tab-pane fade show active" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab" tabindex="0">
        <FollowerCard v-for="(follower, key) in followers" :key="key" :follower="follower.follower" :is_following="follower.is_following" />
      </div>
      <div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab" tabindex="0">
        <FollowingCard v-for="(account, key) in following" :key="key" :account="account.account" :follows_back="account.follows_back" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import FollowerCard from "./FollowerCard.vue";
import FollowingCard from "./FollowingCard.vue";


export default {
  name: "UserFollowingVue",
  components: {
    FollowerCard,
    FollowingCard
  },
  props: {
    username: String
  },
  data() {
    return {
      following: [],
      followers: []
    };
  },
  methods: {
    get_following(username) {
      axios({
        method: "get",
        url: `followers/${username}/following`,
      })
        .then((response) => {
          this.following = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    get_followers(username) {
      axios({
        method: "get",
        url: `followers/${username}/followers`,
      })
        .then((response) => {
          this.followers = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },



  },
  async created() {
    this.get_followers(this.username)
    this.get_following(this.username)
  },
  watch: {
    username(val) {
      this.get_timeline(val)
    }
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>

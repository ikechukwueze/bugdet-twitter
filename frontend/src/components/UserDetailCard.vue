<template>
  <div class="row">
    <div class="d-flex p-3 my-2 border rounded-3">
      <div class="flex-shrink-0">
        <img class="rounded-circle profile-pic" :src="user_details.profile_pic" />
      </div>
      <div class="card ms-1 w-100 border-0">
        <div class="card-header border-0 bg-white">
          <div class="d-flex justify-content-between">
            <div>
              <span class="fw-bold fs-5">
                {{ user_details.display_name }} <i class="bi bi-patch-check-fill"></i></span>
              <span> &#183; </span>
              <span class="text-muted"> @{{ user_details.username }} </span>
            </div>
            <div v-if="is_current_user">
              <span><button class="btn btn-primary btn-sm" id="edit-profile-btn">Edit profile</button></span>
            </div>
          </div>
        </div>
        <div class="card-body py-1">
          <div>
            <p class="card-text">{{ user_details.bio }}</p>
          </div>
          <div class="my-2">
            <p class="card-text"><i class="bi bi-calendar3"></i> Joined {{ user_details.short_signup_date }}</p>
          </div>
          <div class="card-text border-0 bg-white my-1">
            <span class="fw-bold">{{ following_count }}</span><span class="text-muted me-2"> Following  </span>
            <span class="fw-bold">{{ follower_count }}</span><span class="text-muted"> Followers  </span>
          </div>

        </div>

        <div class="card-footer text-muted d-flex justify-content-around border-0 bg-white">
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import axios from 'axios';

export default {
  name: "UserDetailCard",
  components: {
  },
  props: {
    username: String
  },
  data() {
    return {
      user_details: {
        username: "",
        bio: "",
        display_name: "",
        profile_pic: "",
        short_signup_date: ""
      },
      following_count: 0,
      follower_count: 0,
      is_current_user: false
    };
  },

  methods: {
    get_user_details(username) {
      axios({
        method: "get",
        url: `/accounts/${username}/detail/`,
      })
        .then((response) => {
          this.user_details = response.data;
          console.log(this.user_details)
        })
        .catch((error) => {
          console.log(error);
        });
    },
    get_follower_count(username) {
      axios({
        method: "get",
        url: `/followers/${username}/follower-count/`,
      })
        .then((response) => {
          this.follower_count = response.data.followers;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    get_following_count(username) {
      axios({
        method: "get",
        url: `/followers/${username}/following-count/`,
      })
        .then((response) => {
          this.following_count = response.data.following;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  created() {
    this.get_user_details(this.username)
    this.get_follower_count(this.username)
    this.get_following_count(this.username)
    this.is_current_user = this.user_details.username === this.$store.state.username
  },
  watch: {
    username(val){
      this.get_user_details(val)
      this.get_follower_count(val)
      this.get_following_count(val)
    }
  }
};
</script>

<style scoped>
.bi-patch-check-fill {
  color: blue;
  font-size: 1rem;
}

.profile-pic {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}

#edit-profile-btn {
  background-color: blue; 
  color: white
}
</style>

<template>
  <div class="row">
    <div class="d-flex p-3 my-2 border rounded-3">
      <div class="flex-shrink-0">
        <ProfilePic :profile_pic_url="account.profile_pic" :username="account.username" />
      </div>
      <div class="card ms-1 w-100 border-0">
        <div class="card-header border-0 bg-white">
          <div class="d-flex justify-content-between">
            <div>
              <span class="fw-bold">
                {{ account.display_name }} <i class="bi bi-patch-check-fill"></i></span>
              <span> &#183; </span>
              <span class="text-muted"> @{{ account.username }} </span>
            </div>
            <div>
              <template v-if="follows_back">
                  <button class="btn btn-sm btn-primary disabled">Follows you</button>
                </template>
                <template v-else>
                  <button class="btn btn-sm btn-primary disabled">Following</button>
                </template>
            </div>
          </div>
        </div>
        <div class="card-body py-1">
          <p class="card-text">{{ account.bio }}</p>
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
  name: "FollowingCard",
  components: {
    ProfilePic
  },
  props: {
    account: {
      username: String,
      display_name: String,
      profile_pic: String,
      bio: String,
    },
    follows_back: Boolean
  },
  data() {
    return {
    };
  },

  methods: {
  },

  created() {
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

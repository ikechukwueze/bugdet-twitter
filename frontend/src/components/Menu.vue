<template>
    <div class="d-flex flex-column flex-shrink-0 py-3 text-dark vh-100">
        <ul class="nav nav-pills flex-column mb-auto text-start">
            <li class="nav-item mb-4">
                <a href="#" class="nav-link fw-bold" aria-current="page">
                    <span class="me-0"><i class="bi bi-feather"></i></span> Budget Twitter
                </a>
            </li>
            <li class="nav-item">
                <RouterLink :to="{name: 'HomePage'}" class="nav-link">
                    <span class="me-2"><i class="bi bi-house-door"></i></span> Home
                </RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{name: 'ProfilePage', params: {username: this.$store.state.username}}" class="nav-link">
                    <span class="me-2"><i class="bi bi-person"></i></span> Profile
                </RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{name: 'FollowersPage', params: {username: this.$store.state.username}}" class="nav-link">
                    <span class="me-2"><i class="bi bi-person-walking"></i></span> Following
                </RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{name: 'NotificationsPage'}" class="nav-link">
                    <span class="me-2"><i class="bi bi-bell"></i></span> 
                    Notifications <span v-if="notification_count > 0" class="badge text-bg-primary">{{ notification_count }}</span>
                </RouterLink>
                <!-- <a href="#" class="nav-link ">
                    <span class="me-2"><i class="bi bi-bell"></i></span> 
                    Notifications <span v-if="notification_count > 0" class="badge text-bg-primary">{{ notification_count }}</span>
                </a> -->
            </li>
            <li class="nav-item">
                <a href="#" class="nav-link ">
                    <span class="me-2"><i class="bi bi-search"></i></span> Explore
                </a>
            </li>
            <li class="nav-item" @click="sign_out">
                <a href="#" class="nav-link ">
                    <span class="me-2"><i class="bi bi-door-open"></i></span> Sign out
                </a>
            </li>
        </ul>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    name: 'MenuVue',
    props: {
    },
    data() {
        return {
            notification_count: 0,
        }
    },
    methods: {
        sign_out() {
            this.$store.commit('removeAuthState')
            location.reload()
        },
        get_notification_count() {
            axios({
                method: "get",
                url: `/notifications/count/`,
            })
                .then((response) => {
                    this.notification_count = response.data.notification_count;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

    },
    created() {
        this.get_notification_count()
    }
}


</script>

<style>
.nav-link {
    font-size: large;
}
.badge {
    font-size: 9px;
}

.nav-link {
    color: black
}
</style>
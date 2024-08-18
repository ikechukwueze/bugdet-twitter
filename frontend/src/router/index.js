import { createWebHistory, createRouter } from "vue-router"
import HomeVue from "@/views/Home.vue"
import LoginVue from "@/views/Login.vue"
import ProfileVue from "@/views/Profile.vue"
import FollowersVue from "@/views/Followers.vue"
import NotificationsVue from "@/views/Notifications.vue"
import ThreadVue from "@/views/Thread.vue"
import ExploreVue from "@/views/Explore.vue"
import TrendFeed from "@/views/TrendFeed.vue"
// import LostPup from "@/views/404.vue"
import store from "@/store"
//import NProgress from 'nprogress';



const routes = [
    {
        path: "/login",
        name: "LoginPage",
        component: LoginVue,
    },
    {
        path: "/",
        name: "HomePage",
        component: HomeVue,
    },
    {
        path: "/profile/:username",
        name: "ProfilePage",
        component: ProfileVue,
        props: true
    },
    {
        path: "/profile/:username/following/",
        name: "FollowersPage",
        component: FollowersVue,
        props: true
    },
    {
        path: "/notifications/",
        name: "NotificationsPage",
        component: NotificationsVue,
    },
    {
        path: "/tweet/:tweet_id/",
        name: "ThreadPage",
        component: ThreadVue,
        props: true
    },
    {
        path: "/explore/",
        name: "ExplorePage",
        component: ExploreVue,
        props: true
    },
    {
        path: "/explore/trends/:trend_term",
        name: "TrendFeedPage",
        component: TrendFeed,
        props: true
    },
    // {
    //     path: '/:catchAll(.*)*',
    //     name: "page-404",
    //     component: LostPup,
    // },
    // {
    //     path: '/:catchAll(.*)*',
    //     name: "Home",
    //     component: HomeVue,
    // },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


router.beforeEach((to, from, next) => {
    if (to.name !== 'LoginPage' && !store.getters.isAuthenticated) next({ name: 'LoginPage' })
    else next()
})

// ...

// router.beforeResolve((to, from, next) => {
//     // If this isn't an initial page load.
//     if (to.name) {
//         // Start the route progress bar.
//         NProgress.start()
//     }
//     next()
// })

// router.afterEach((to, from) => {
//     // Complete the animation of the route progress bar.
//     NProgress.done()
// })


export default router 
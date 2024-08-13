import { createStore } from 'vuex'
import axios from 'axios'

const store = createStore({
    state: {
        token: null,
        username: null,
        display_name: null,
        profile_pic: null,
        isAuthenticated: false
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('auth_data')) {
                var auth_data = JSON.parse(localStorage.getItem('auth_data'))
                state.token = auth_data.token
                state.username = auth_data.username
                state.display_name = auth_data.display_name
                state.profile_pic = auth_data.profile_pic
                state.isAuthenticated = true
            } else {
                state.token = null
                state.username = null
                state.display_name = null
                state.profile_pic = null
                state.isAuthenticated = false
            }
        },
        setAuthState(state, data) {
            var auth_data = JSON.parse(data)
            state.token = auth_data.token
            state.username = auth_data.username
            state.display_name = auth_data.display_name
            state.profile_pic = auth_data.profile_pic
            state.isAuthenticated = true
            axios.defaults.headers.common['Authorization'] = 'Token ' + state.token
            localStorage.setItem('auth_data', data)
        },
        removeAuthState() {
            localStorage.removeItem('auth_data')
        }
    },
    actions: {},
    getters: {
        isAuthenticated(state) {
            return state.isAuthenticated;
        },
    },
})

export default store
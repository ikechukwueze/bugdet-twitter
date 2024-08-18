<template>
    <div class="col-9 mt-4 w-100 text-start">
        <nav>
            <div class="nav nav-pills nav-fill" id="nav-tab" role="tablist">
                <button class="nav-link active" id="nav-search-toptweets-tab" data-bs-toggle="tab"
                    data-bs-target="#nav-search-toptweets" type="button" role="tab" aria-controls="nav-search-toptweets"
                    aria-selected="true">Top</button>

                <button class="nav-link" id="nav-search-latesttweets-tab" data-bs-toggle="tab"
                    data-bs-target="#nav-search-latesttweets" type="button" role="tab" aria-controls="nav-search-latesttweets"
                    aria-selected="false">Latest</button>
            </div>
        </nav>
        <div class="tab-content px-3" id="nav-tabContent">
            <div class="tab-pane fade show active" id="nav-search-toptweets" role="tabpanel"
                aria-labelledby="nav-search-toptweets-tab" tabindex="0">
                <TweetList :tweets="top_search_results" />
            </div>
            <div class="tab-pane fade" id="nav-search-latesttweets" role="tabpanel" aria-labelledby="nav-search-latesttweets-tab"
                tabindex="0">
                <TweetList :tweets="latest_search_results" />
            </div>
        </div>
    </div>
</template>



<script>
import axios from 'axios';
import TweetList from './TweetList.vue';


export default {
    name: 'SearchResults',
    components: {
        TweetList
    },
    props: {
        search_query: String
    },
    data() {
        return {
            top_search_results: [],
            latest_search_results: []
        };
    },
    methods: {
        get_search_top_results(query) {
            axios({
                method: "get",
                url: `search/tweets/?search=${query}&ordering=-interactions&limit=100`,
            })
                .then((response) => {
                    this.top_search_results = response.data.results;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        get_search_latest_results(query) {
            axios({
                method: "get",
                url: `search/tweets/?search=${query}&ordering=-created_at&limit=100`,
            })
                .then((response) => {
                    this.latest_search_results = response.data.results;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },

    created() {
        this.get_search_top_results(this.search_query)
        this.get_search_latest_results(this.search_query)
    },
    watch: {
        search_query(new_query) {
            this.get_search_top_results(new_query)
            this.get_search_latest_results(new_query)
        }
    }

}
</script>

<style>
.list-group-item {
    border: 0px;
}

.trend-topic {
    margin-bottom: 0px;
}

.list-group-item {
    text-align: left
}
</style>
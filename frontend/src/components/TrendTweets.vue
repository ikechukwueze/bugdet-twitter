<template>
    <div class="col-9 mt-4 w-100 text-start">
        <nav>
            <div class="nav nav-pills nav-fill" id="nav-tab" role="tablist">
                <button class="nav-link active" id="nav-toptweets-tab" data-bs-toggle="tab"
                    data-bs-target="#nav-toptweets" type="button" role="tab" aria-controls="nav-toptweets"
                    aria-selected="true">Top</button>

                <button class="nav-link" id="nav-latesttweets-tab" data-bs-toggle="tab"
                    data-bs-target="#nav-latesttweets" type="button" role="tab" aria-controls="nav-latesttweets"
                    aria-selected="false">Latest</button>
            </div>
        </nav>
        <div class="tab-content px-3" id="nav-tabContent">
            <div class="tab-pane fade show active" id="nav-toptweets" role="tabpanel"
                aria-labelledby="nav-toptweets-tab" tabindex="0">
                <TweetList :tweets="top_tweets" />
            </div>
            <div class="tab-pane fade" id="nav-latesttweets" role="tabpanel" aria-labelledby="nav-latesttweets-tab"
                tabindex="0">
                <TweetList :tweets="latest_tweets" />
            </div>
        </div>
    </div>
</template>



<script>
import axios from 'axios';
import TweetList from './TweetList.vue';


export default {
    name: 'TrendList',
    components: {
        TweetList
    },
    props: {
        trend_term: String
    },
    data() {
        return {
            top_tweets: [],
            latest_tweets: []
        };
    },
    methods: {
        get_trend_top_tweets(trend_term) {
            axios({
                method: "get",
                url: `/trends/${trend_term}/top-tweets?limit=100`,
            })
                .then((response) => {
                    this.top_tweets = response.data.results;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        get_trend_latest_tweets(trend_term) {
            axios({
                method: "get",
                url: `/trends/${trend_term}/latest-tweets?limit=100`,
            })
                .then((response) => {
                    this.latest_tweets = response.data.results;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },

    created() {
        this.get_trend_top_tweets(this.trend_term)
        this.get_trend_latest_tweets(this.trend_term)
    },
    watch: {
        trend_term(new_trend) {
            this.get_trend_top_tweets(new_trend)
            this.get_trend_latest_tweets(new_trend)
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
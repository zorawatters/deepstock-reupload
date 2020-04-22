<template>
  <div>
    <div class="card text-center">
<<<<<<< HEAD
      <div class="card-body">
        <h5 class="card-title">INSERT TITLE HERE</h5>
        <p class="card-text">INSERT TWEET HERE</p>
        <a href="#" class="btn btn-info">Link to tweet/bio?</a>
=======

      <div class="card-body twitter-card-body" style = "max-height: 250px; overflow-y: scroll;">
        <div class = "tweet-card-tweet" style = "background: #f1f1f1; padding: 10px; border-radius: 5px;margin-bottom: 15px;box-shadow: 0px 2px 1px -1px rgba(0,0,0,0.2), 0px 1px 1px 0px rgba(0,0,0,0.14), 0px 1px 3px 0px rgba(0,0,0,0.12);" v-for="tweet in tweets" :key="tweet">
          {{ tweet }}
        </div>
>>>>>>> a485fb473c64d78d59511ad64619c8c0892c005d
      </div>
      <div class="card-footer text-muted">
       Recent {{ticker}} Tweets
      </div>
    </div>
  </div>
</template>
<script>
import {mapGetters} from 'vuex'

export default {
  name: 'twitter-card',
  props: {
    custom: {
      type: String,
      default: ''
    },
    ticker: {
      type: String,
      default: ''
    }
  },
  data(){
    return {
    }
  },
  computed: mapGetters({tweets: 'getTweetText', ticker: 'getTicker'})
}
</script>

<template>
  <div>
    <div class="card text-center">

      <div class="card-body">
        <h5 class="card-title">INSERT TITLE HERE</h5>
        <p class="card-text">INSERT TWEET HERE</p>
        <a href="#" class="btn btn-info">Link to tweet/bio?</a>
      </div>
      <div class="card-footer text-muted">
        {{ tweets ? tweets[0] : ''}}
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
  computed: mapGetters({tweets: 'getTweetText'})
}
</script>

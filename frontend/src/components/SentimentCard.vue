<template>
<div :class = "custom">
  <b>Sentiment Analysis:</b>
  <p style="color:red">{{pred}}</p>
  <p>{{tweet_sent}}</p>
</div>
</template>
<script>
import {mapGetters} from 'vuex'
export default {
  name: 'sentiment-card',
  props: {
    custom: {
      type: String,
      default: ''
    }
  },
  data(){
    return {
    }
  },
  computed: mapGetters({
    pred: 'getPrediction',
    tweet_sent: 'getTweetSent'
  })
}
</script>

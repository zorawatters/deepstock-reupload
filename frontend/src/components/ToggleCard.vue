<template>
<div :class = "custom" @click="setTicker">
  <!-- <p>{{ticker}} - {{name}} <t> <a style="color:28a745"> {{high}} </a>|<a style="color:dc3545"> {{low}} </a></p> -->
    <p> <a style = "color:dc3545">{{ticker}}</a> {{metadata.shortName}} <img :src="metadata.logo_url" width = "50" height = "50"></p>
</div>
</template>
<script>

  export default {
    name: 'toggle-card',
    props: {
      custom: {
        type: String,
        default: ''
      },

      ticker: {
        type: String,
        default: ''
      },

    },
    data(){
      return {
        metadata: {
          shortName : '',
          logo_url : '',
          website : ''
        }
      }
    },
    methods:{
      setTicker:function(){
        console.log("ticker")
        this.$store.commit('setTicker', this.ticker)
        console.log("Called")
      }
    },
    async mounted(){
      var tick = '/'
      tick = tick + this.ticker
      this.metadata = (await this.$http(this.$backendUrl + tick +'/metadata')).data
    }
  }
</script>
